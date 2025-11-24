import re

def validate(id_, pw_):

    email_pattern = re.compile(r"^[a-zA-Z]+\.[a-zA-Z0-9]+@university\.com$")
    pw_pattern = re.compile(r"^[A-Z][a-zA-Z]{5,}\d{3,}$")

    if not email_pattern.fullmatch(id_):
        return False

    if not pw_pattern.fullmatch(pw_):
        return False
    
    return True