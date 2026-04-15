import re

def is_strong_password(password: str) -> bool:
    rules = [
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        bool(re.search(r"[!@#$%^&*]", password)),
        " " not in password
    ]
    
    return all(rules)