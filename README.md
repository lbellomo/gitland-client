# gitland-client
Code to play with [gitland](https://github.com/programical/gitland/), and a excuse to play with Asyncio.

## Install

```
pip install -r requeriments.txt
```

## Config

You only need to copy `config_sample.py`, complete it and rename to `config.py`.
What you need to complete is:
- **player_name**: your github user.
- **secret**: your secret token, you can get it [here](from https://github.com/settings/tokens).
- **step**: the function to decide the next step. All the logic of the agent lives here.

## Play
```
python main.py
```
