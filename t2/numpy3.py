import numpy as np

# دو بردار تصادفی به طول ۵ (میتونی n رو هر عددی بذاری)
n = 5
a = np.random.rand(n)
b = np.random.rand(n)

# فاصلهٔ اقلیدسی به روش برداری خودمون: ریشهٔ مجموع مربع اختلاف‌ها
my_distance = np.sqrt(np.sum((a - b) ** 2))

# فاصله با تابع آمادهٔ NumPy
lib_distance = np.linalg.norm(a - b)

print("بردار a:", a)
print("بردار b:", b)
print("فاصلهٔ محاسبه‌شده با دستور خودمون:", my_distance)
print("فاصله با تابع linalg.norm:", lib_distance)

# بررسی میکنیم که آیا هر دو تقریباً برابر هستند؟ (بله)
print("آیا برابرند؟", np.allclose(my_distance, lib_distance))