"""
Provides insult functions.
"""

from random import choice

from insultapp.insults import first_adjective_list, second_adjective_list, nouns


def generate_insult() -> str:
    """
    Generates insult based on first and second adjectives, and a noun.

    Returns:
    str: The insult
    """
    return f"{choice(first_adjective_list)} {choice(second_adjective_list)} {choice(nouns)}"


def insult() -> str:
    """
    Generates a generic insult.

    Returns:
    str: The insult
    """
    return f"Thou {generate_insult()}!"


def named_insult(name: str) -> str:
    """
    Generates an insult with a given name.

    Parameters:
    name (str): The name to be insulted

    Returns:
    str: The insult
    """
    return f"{name}, thou {generate_insult()}!"
