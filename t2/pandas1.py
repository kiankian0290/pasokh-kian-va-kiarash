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

# برای راحتی، نام ستون‌ها را کوتاه می‌کنیم (اختیاری)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

mean_petal_length = df['petal_length'].mean()
filtered = df[df['petal_length'] > mean_petal_length][['species', 'petal_length']]
count_rows = len(filtered)
print(f"تعداد سطرها: {count_rows}")