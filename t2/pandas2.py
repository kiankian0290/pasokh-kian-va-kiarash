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

df['petal_area'] = df['petal_length'] * df['petal_width']
df['is_big'] = df['petal_area'] > 10
big_count = df['is_big'].value_counts()
print(big_count)