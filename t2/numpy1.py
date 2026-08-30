import numpy as np

# ساخت آرایه
arr = np.random.randint(0, 101, size=(5, 5))
print("آرایهٔ اولیه:\n", arr)

# ماسک بولین: هر جای که مقدار > 50 است، آن را 0 کن
arr[arr > 50] = 0

print("آرایهٔ نهایی (اعداد > 50 صفر شدن):\n", arr)