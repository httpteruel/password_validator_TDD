def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    return True