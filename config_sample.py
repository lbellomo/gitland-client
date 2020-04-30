# github username
player_name = ""

# github token from https://github.com/settings/tokens
secret = ""

def step(x, y, team, board):
    """
    Function to decide the next step. All the logic of the agent lives here.
    
    Parameters
    ----------
    x : int
      Position in the x axis of the agent.
    y : int
      Position in the y axis of the agent.
    team : str
      Agent team.
    board : list
      State of the game. Useful to decide the next step.
      Element [x, y] is borad[y][x].

    Returns
    -------
    next_step : str
      The next step of the agent.
      Valid opcions are: ["up", "down", "left", "right", "idle"]
      
    """
    from random import choice
    next_step = choice(["up", "down", "left", "right", "idle"])
    return next_step
