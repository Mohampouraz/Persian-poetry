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

    clean_verse = []
    for item in data:
        if is isinstance(item, str):
            print("Non-string item:", item)
        
        else:
            s = item
            # Text normalization and character replacement
            s = s.replace('ا\u200cست', 'است')     # Fix form of 'است'
            s = s.replace('\u200c ', ' ')         # ZWNJ + space
            s = s.replace('\u200c', ' ')          # Zero-width non-joiner
            s = s.replace('\ufeff', '')           # BOM character
            s = s.replace('\u202a', '')           # LRE
            s = s.replace('\u202b', '')           # RLE
            s = s.replace('\u202c', '')           # PDF
            s = s.replace('\u200d', '')           # Zero-width joiner

            # Arabic to Persian character normalization
            s = s.replace('ي', 'ی')
            s = s.replace('ك', 'ک')
            s = s.replace('ۀ', 'ه')

            # Remove punctuation and extraneous symbols
            for ch in ['،', ':', 'ّ', 'َ', 'ُ', 'ِ', 'ً', 'ٌ', 'ٍ',
                    '!', '?', '؟', 'ٔ', '«', '»', '؛', ')', '(', 'ـ',
                    '+', '-', '*']:
                s = s.replace(ch, '')

            # Remove digits (English and Persian)
            s = ''.join(ch for ch in s if not ch.isdigit())  # Removes 0-9
            for num in ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']:
                s = s.replace(num, '')

            # Final whitespace normalization
            s = ' '.join(s.split())
            s = s.strip()

            clean_verse.append(s)

    return clean_verse

