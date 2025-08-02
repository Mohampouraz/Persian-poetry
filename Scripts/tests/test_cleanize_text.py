# test_cleanize_text.py


from cleanize_text import cleanize_text


def test_clean_string_input():
    tokens, cleaned = cleanize_text("اوست کتاب، ۱۲۳؟")
    assert tokens == ['اوست', 'کتاب']
    assert cleaned == 'اوست کتاب'

def test_clean_token_list():
    tokens, cleaned = cleanize_text(['ف«صل»', '۱۲۳۴', 'به412ار'])
    assert tokens == ['فصل', 'بهار']
    assert cleaned == 'فصل بهار'

