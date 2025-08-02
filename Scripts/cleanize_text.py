def cleanize_text(data):
    try:
        tokens = data.split() if isinstance(data, str) else list(data)
    except Exception as e:
        raise ValueError("Input must be a string or iterable of strings") from e

    clean_tokens = []
    for token in tokens:
        try:
            # اطمینان از رشته بودن و تمیزسازی
            s = str(token)

            # Unicode cleanup
            s = s.replace('ا\u200cست', 'است') \
                 .replace('\u200c ', ' ') \
                 .replace('\u200c', ' ') \
                 .replace('\ufeff', '') \
                 .replace('\u202a', '') \
                 .replace('\u202b', '') \
                 .replace('\u202c', '') \
                 .replace('\u200d', '') \
                 .replace('ي', 'ی') \
                 .replace('ك', 'ک') \
                 .replace('ۀ', 'ه')

            import re
            s = re.sub(r'[،:ًٌٍَُِّ!?؟ٔ«»؛)(ـ+\-*]', '', s)
            s = ''.join(ch for ch in s if not ch.isdigit())
            for pd in '۰۱۲۳۴۵۶۷۸۹':
                s = s.replace(pd, '')

            s = ' '.join(s.split()).strip()
            if s:
                clean_tokens.append(s)

        except Exception as e:
            print(f"Skipped token due to error: {token} → {e}")
            continue

    cleaned_string = ' '.join(clean_tokens)
    return clean_tokens, cleaned_string
