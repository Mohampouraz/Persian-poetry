def cleanize_text(data):
    """
    Cleans and standardizes Persian poetic text for linguistic and metrical analysis.

    Accepts:
    - str: a single string input
    - list: a list of string tokens

    Performs:
    - Unicode cleanup
    - Arabic-to-Persian letter normalization
    - Punctuation and digit removal
    - Whitespace normalization

    Returns:
    - cleaned_tokens: list of cleaned tokens
    - cleaned_string: joined string from cleaned tokens
    """

    import re

    # Tokenization based on input type
    if isinstance(data, str):
        tokens = data.split()
    elif isinstance(data, list):
        tokens = data
    else:
        raise ValueError("Input must be a string or list of strings")

    clean_tokens = []
    for token in tokens:
        if not isinstance(token, str):
            continue  # Skip non-string tokens

        s = token

        # Unicode cleanup
        s = s.replace('ا\u200cست', 'است')
        s = s.replace('\u200c ', ' ')
        s = s.replace('\u200c', ' ')
        s = s.replace('\ufeff', '')
        s = s.replace('\u202a', '')
        s = s.replace('\u202b', '')
        s = s.replace('\u202c', '')
        s = s.replace('\u200d', '')

        # Arabic-to-Persian normalization
        s = s.replace('ي', 'ی')
        s = s.replace('ك', 'ک')
        s = s.replace('ۀ', 'ه')

        # Remove punctuation and symbols
        s = re.sub(r'[،:ًٌٍَُِّ!?؟ٔ«»؛)(ـ+\-*]', '', s)

        # Remove digits (English & Persian)
        s = ''.join(ch for ch in s if not ch.isdigit())
        for pd in '۰۱۲۳۴۵۶۷۸۹':
            s = s.replace(pd, '')

        # Normalize whitespace
        s = ' '.join(s.split()).strip()

        if s:
            clean_tokens.append(s)

    # Join cleaned tokens into a single string
    cleaned_string = ' '.join(clean_tokens)

    return clean_tokens, cleaned_string
