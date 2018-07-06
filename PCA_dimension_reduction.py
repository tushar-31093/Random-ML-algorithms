from sklearn.decomposition import PCA
import pandas as pd
pca = PCA(n_components=2, svd_solver='full')
df = pd.read_csv('E:/DAT210x-master/DAT210x-master/Module3/Datasets/students.data')
df.drop(['id'],axis=1, inplace=True)

pca.fit(df)
PCA(copy=True, n_components=2, whiten=False)

T = pca.transform(df)


print(df.shape)
#(430, 6) # 430 Student survey responses, 6 questions..
print(T.shape)