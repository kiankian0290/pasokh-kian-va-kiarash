# imports لازم
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# بارگذاری Iris مانند فصل ۱
iris_data = load_iris()
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
df['species'] = iris_data.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
df_small = pd.DataFrame({
    'weight': [2.5, 3.1, np.nan, 4.0, 3.8, np.nan, 5.2],
    # ستون‌های دیگر ...
})

# برای راحتی، نام ستون‌ها را کوتاه می‌کنیم (اختیاری)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# پر کردن با میانه
median_weight = df_small['weight'].median()
df_small['weight'].fillna(median_weight, inplace=True)

# تأیید عدم وجود NaN
no_nan = df_small['weight'].isna().sum() == 0
print(f"آیا هیچ NaN باقی نمانده؟ {no_nan}")