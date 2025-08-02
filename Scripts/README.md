## 🧪 مثال‌هایی از استفاده تابع `cleanize_text`

تابع `cleanize_text` برای تمیزسازی متون فارسی (شعر، گفتار، داده‌های نویزدار) طراحی شده. خروجی شامل توکن‌های تمیز و متن نهایی است.

### 🔹 ورودی به صورت رشته

```python
from cleanize_text import cleanize_text

text = "مَن‌ از آن روز که در بندِ توام آزادم؛ ۱۲۳۴۵!"
tokens, cleaned = cleanize_text(text)

print("Tokens:", tokens)
print("Cleaned Text:", cleaned)
Tokens: ['من', 'از', 'آن', 'روز', 'که', 'در', 'بند', 'توام', 'آزادم']
Cleaned Text: من از آن روز که در بند توام آزادم

