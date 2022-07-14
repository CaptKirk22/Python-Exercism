"""
have name in string and if blank replace with you
"""
def two_fer(name = ""):
    """
    enter name
    """
    if not name:
        return "One for you, one for me."
    else:
        return f"One for {name}, one for me."
