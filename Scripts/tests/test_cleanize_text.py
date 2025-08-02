# test_cleanize_text.py

from cleanize_text import cleanize_text

def test_clean_string_input():
    tokens, cleaned = cleanize_text("او‌ست کتابی، ۱۲۳؟")
    assert tokens == ['اوست', 'کتابی']
    assert cleaned == 'اوست کتابی'

def test_clean_token_list():
    tokens, cleaned = cleanize_text(['سلام', '۱۲۳۴', '؟کجایی؟'])
    assert tokens == ['سلام', 'کجایی']
    assert cleaned == 'سلام کجایی'

def test_noisy_input():
    tokens, cleaned = cleanize_text([None, 'کجا؟', 42, 'بهار'])
    assert tokens == ['کجا', 'بهار']
    assert cleaned == 'کجا بهار'
