from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
import  numpy as np

cancer=load_breast_cancer()
# print(cancer)
print(len(cancer))
print(type(cancer))
cancer_data=cancer['data']
cancer_target=cancer['target']
cancer_name=cancer['feature_names']
cancer_descr=cancer['DESCR']
# print(cancer_data)
# print(cancer_target)
# print(cancer_name)
# print(cancer_descr)
print(cancer_data.shape)
print(cancer_target.shape)
cancer_data_train=cancer_data[:400,1]
cancer_data_test=cancer_data[:400,1]
Scaler=MinMaxScaler().fit(cancer_data_train)
cancer_trainScaler=Scaler.transform(cancer_data_train)
cancer_trainScaler=Scaler.transform(cancer_data_test)