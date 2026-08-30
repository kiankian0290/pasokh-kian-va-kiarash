import numpy as np

# ۱۰ نمونه با ۳ ویژگی (اعداد تصادفی بین ۰ تا ۱۰۰)
data = np.random.randint(0, 100, size=(10, 3)).astype(float)
print("دادهٔ اولیه:\n", data)

# کمترین و بیشترین مقدار هر ستون (هر ویژگی) رو پیدا کن
min_vals = data.min(axis=0)  # خروجی: ۳ عدد (مینیمم هر ستون)
max_vals = data.max(axis=0)  # خروجی: ۳ عدد (ماکزیمم هر ستون)

# فرمول نرمال‌سازی: (x - min) / (max - min)
normalized = (data - min_vals) / (max_vals - min_vals)

print("دادهٔ نرمال‌شده:\n", normalized)