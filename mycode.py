import pandas as pd 
import os

data = {'name':['Alice','Bob','Charlie'],'age':[25,30,40],'city':['New York','Delhi','Mumbai']}

df=pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#define the file path
file_path= os.path.join(data_dir,"sample_data.csv")

df.to_csv(file_path,index=False)

print(f"CSV file printed to {file_path}")