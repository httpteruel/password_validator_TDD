# tests/test_validator.py
from src.validator import is_strong_password

def test_should_reject_password_less_than_8_chars():
    assert is_strong_password("Ab1!def") is False

def test_should_reject_password_without_uppercase():
    assert is_strong_password("lowercas1!") is False

def test_should_reject_password_without_lowercase():
    assert is_strong_password("UPPERCAS1!") is False