import numpy as np

# نمرات ۱۰ نمونه برای ۳ کلاس (تصادفی)
scores = np.random.rand(10, 3)
print("نمرات کلاس‌ها:\n", scores)

# برچسب‌های واقعی (عدد ۰ یا ۱ یا ۲)
true_labels = np.random.randint(0, 3, size=10)
print("برچسب‌های واقعی:", true_labels)

# پیش‌بینی: اندیس ستونی که بیشترین نمره رو داره (همون کلاس پیش‌بینی‌شده)
predicted = np.argmax(scores, axis=1)
print("برچسب‌های پیش‌بینی‌شده:", predicted)

# دقت: چندتاشون درست بودن؟ (مقایسهٔ برداری)
accuracy = np.mean(predicted == true_labels)
print(f"دقت مدل: {accuracy * 100:.2f}%")