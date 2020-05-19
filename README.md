# gitland-client
Code to play with [gitland](https://github.com/programical/gitland/), and a excuse to play with Asyncio.

Gitland was a game where automata cross a 2D board, coloring the positions they pass by the color of their team. You have info about the state of the game looking at the main repo and you change the actions by committing in your repo.

As the main repo went missing, this repo is archived.

## Install

```
pip install -r requeriments.txt
```

## Config

You only need to copy `config_sample.py`, complete it and rename to `config.py`.
What you need to complete is:
- **player_name**: your github user.
- **secret**: your secret token, you can get it [here](https://github.com/settings/tokens).
- **step**: the function to decide the next step. All the logic of the agent lives here.

Be careful not to commit your config.py anywhere! You shouldn't post or share your token.

## Play
```
python main.py
```
