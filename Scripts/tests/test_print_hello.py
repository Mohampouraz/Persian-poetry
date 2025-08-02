# tests/test_print_hello.py

from src.print_hello import say_hello

def test_say_hello():
    assert say_hello() == "hello github"
