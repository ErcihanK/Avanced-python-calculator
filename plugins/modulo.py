"""
Plugin for calculating the modulo of two numbers.
"""

def modulo(a, b):
    """
    Calculate the remainder when one number is divided by another.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The remainder after division.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a % b

def register_commands(commands):
    """
    Register the modulo command in the given commands dictionary.

    Args:
        commands (dict): The dictionary of available commands.
    """
    commands['modulo'] = modulo
