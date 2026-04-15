# tests/test_validator.py
from src.validator import is_strong_password

def test_should_reject_password_less_than_8_chars():
    assert is_strong_password("Ab1!def") is False