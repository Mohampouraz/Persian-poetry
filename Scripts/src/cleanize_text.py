def cleanize_text(data):
    """
    Cleans and standardizes a list of Persian poetic texts for linguistic and metrical analysis.

    This function processes each item in the provided list and applies the following operations:
    - Removes problematic Unicode characters (e.g., zero-width non-joiners, directional marks, BOM)
    - Normalizes Arabic characters (e.g., transforms 'ي' to 'ی', 'ك' to 'ک')
    - Replaces special cases like 'ا‌ست' with standard forms like 'است'
    - Removes punctuation and diacritical marks that interfere with text processing
    - Standardizes spacing and strips unnecessary whitespace

    Output: A list of cleaned verses, optimized for downstream analysis such as metrical classification, NLP tasks, or corpus preparation.
    """
    import re

    # Check Data Type...
    if isinstance(data, str):
        tokens = data.split()
    elif isinstance(data, (list, tuple)):
        tokens = [str(t) for t in data if isinstance(t, str)]
    else:
        raise ValueError("Input must be a string or a list/tuple of strings.")

    clean_tokens = []
    for token in tokens:
        try:
            s = token

            # Unicode Cleanup...
            s = s.replace('\u200c', ' ') \
                 .replace('\u200d', '') \
                 .replace('\ufeff', '') \
                 .replace('\u202a', '').replace('\u202b', '').replace('\u202c', '') \
                 .replace('ي', 'ی').replace('ك', 'ک').replace('ۀ', 'ه')

            # Digits and Diacritics Cleanup...
            s = re.sub(r'[،:ًٌٍَُِّ!?؟ٔ«»؛)(ـ+\-*]', '', s)
            s = ''.join(ch for ch in s if not ch.isdigit())
            for pd in '۰۱۲۳۴۵۶۷۸۹':
                s = s.replace(pd, '')

            s = s.strip()
            if s:
                clean_tokens.append(s)
        except Exception as e:
            print(f"Skipped token due to error: {token} → {e}")
            continue

    cleaned_string = ' '.join(clean_tokens)
    return clean_tokens, cleaned_string
