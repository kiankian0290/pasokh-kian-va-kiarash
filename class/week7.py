from sklearn.datasets import fetch_openml
titanic = fetch_openml("titanic", version=1, as_frame=True)
df = titanic.frame
df.head()
