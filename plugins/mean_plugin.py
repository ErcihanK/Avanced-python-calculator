"""
Plugin for calculating the mean of two numbers.
"""

def mean(a, b):
    """
    Calculate the mean of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The mean of the two numbers.
    """
    return (a + b) / 2

def register_commands(commands):
    """
    Register the mean command in the given commands dictionary.

    Args:
        commands (dict): The dictionary of available commands.
    """
    commands['mean'] = mean
