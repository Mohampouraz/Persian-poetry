def cleanize_tZext(data):
    import re

    # مرحلهٔ آماده‌سازی داده
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

            # پاکسازی Unicode‌های مزاحم
            s = s.replace('\u200c', ' ') \
                 .replace('\u200d', '') \
                 .replace('\ufeff', '') \
                 .replace('\u202a', '').replace('\u202b', '').replace('\u202c', '') \
                 .replace('ي', 'ی').replace('ك', 'ک').replace('ۀ', 'ه')

            # حذف علائم و اعداد
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
