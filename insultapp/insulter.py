from random import choice


def insult() -> str:
    return f"Thou {generate_insult()}!"


def named_insult(name: str) -> str:
    return f"{name}, thou {generate_insult()}!"


def generate_insult() -> str:
    first_adjective_list = ["artless", "bawdy", "beslubbering", "bootless", "churlish"]
    second_adjective_list = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained"]
    nouns = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig"]

    return f"{choice(first_adjective_list)} {choice(second_adjective_list)} {choice(nouns)}"
