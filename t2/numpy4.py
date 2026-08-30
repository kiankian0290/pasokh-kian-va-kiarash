import numpy as np
import time

n = 1_000_000  # ۱ میلیون
x = np.random.rand(n)

# ---------- روش برداری (NumPy) ----------
start = time.perf_counter()
result_vec = x**2 + 2*x + 1
vec_time = time.perf_counter() - start

# ---------- روش حلقهٔ پایتون (لیست‌کامپریشن) ----------
start = time.perf_counter()
result_loop = [xi**2 + 2*xi + 1 for xi in x]
loop_time = time.perf_counter() - start

# چاپ نتایج
print(f"زمان روش برداری (NumPy): {vec_time:.4f} ثانیه")
print(f"زمان روش حلقه (Python): {loop_time:.4f} ثانیه")
print(f"سرعت NumPy حدود {loop_time / vec_time:.0f} برابر سریع‌تر است!")