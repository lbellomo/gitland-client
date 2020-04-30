import asyncio
from base64 import b64encode
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from aiohttp import ClientSession

from config import secret, player_name, step


# commit message
message = "update move"

team = None
old_step = None
timeout = 60

headers = {"Authorization": f"token {secret}"}
url_act = f"https://api.github.com/repos/{player_name}/gitland-client/contents/act"
base_url = "https://github.com/programical/gitland/blob/master/"
base_url_players = urljoin(base_url, f"players/{player_name}/")
url_x = urljoin(base_url_players, "x")
url_y = urljoin(base_url_players, "y")
url_team = urljoin(base_url_players, "team")
url_board = urljoin(base_url, "map")


def html2text(text: str):
    """Util to parse the requets."""
    soup = BeautifulSoup(text, "lxml")
    text = [tr.find_all("td")[-1].text for tr in soup.find_all("tr")]
    if len(text) == 1:
        return text[0]

    return text


async def fetch(session: ClientSession, url: str, json: bool = False):
    """Util to fetch (get) the urls."""
    async with session.get(url) as response:
        if json:
            return await response.json()
        else:
            text = await response.text()
            return html2text(text)


async def iteration():
    global team, old_step
    async with ClientSession() as session:
        # Download data
        tasks = [fetch(session, url) for url in [url_x, url_y, url_board]]

        # The team does not change, we only bring it once
        if not team:
            tasks += [fetch(session, url_team)]

        results = await asyncio.gather(*tasks)

        if not team:
            x, y, board, team = results
        else:
            x, y, board = results

        board = [i.split(",") for i in board]
        print(f"x: {x}, y: {y}")

        # determine new step
        next_step = step(x, y, team, board)
        print(f"next step: {next_step}")

        print("commit new step")
        if old_step != next_step:
            old_act_json = await fetch(session, url_act, json=True)
            sha = old_act_json["sha"]
            content = b64encode(next_step.encode()).decode()
            act_json = {"message": message, "content": content, "sha": sha}
            r = await session.put(url_act, headers=headers, json=act_json)
            old_step = next_step

        await asyncio.sleep(timeout)


async def main():
    print("Starting main")
    while True:
        try:
            await asyncio.wait_for(iteration(), timeout)
        except asyncio.TimeoutError:
            print("timeout in step")
        except Exception as e:
            print("Exception:", e)
            await asyncio.sleep(timeout)


asyncio.run(main())
