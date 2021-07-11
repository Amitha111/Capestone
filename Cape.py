import pandas as pd
import numpy as np
import os 
if os.path.isfile('C:\\Users\\13148\\Desktop\\US_Unemployment_data_CSV.csv'):
    print('The file is available.')
else:
    print('The file is not available.')

df = pd.read_csv('C:\\Users\\13148\\Desktop\\US_Unemployment_data_CSV.csv')
#print(df)
df.to_excel('C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\US_Unemployment_data_CSV.xlsx', index = None, header= True)


if os.path.isfile('C:\\Users\\13148\\Desktop\\US_Unemployment_Men.csv'):
    print('The file is available')
else:
    print('The fie is unavailable')

df_1 = pd.read_csv('C:\\Users\\13148\\Desktop\\Unemployment_Men.csv')
#print(df_1)
df_1.to_excel('C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\Unemployment_Men.xlsx', index = None, header= True)
if os.path.isfile('C:\\Users\\13148\\Desktop\\Unemployment_Women.csv'):
    print('The file is available')
else:
    print('The fie is unavailable')
df_2 = pd.read_csv('C:\\Users\\13148\\Desktop\\Unemployment_Women.csv')
print(df_2)
df_2.to_excel('C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\Unemployment_Women.xlsx', index = None, header= True)    

# reading the files
file_1 = pd.read_excel("C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\US_Unemployment_data_CSV.xlsx")
file_2 = pd.read_excel("C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\Unemployment_Men.xlsx")
  
# merging the files
file_3 = file_1[["DATE", 
         "UNRATE"]].merge(file_2[["DATE","LNS14000001"]], on = "DATE", how = "left")
  
# creating a new file
file_3.to_excel("C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\Changed.xlsx", index = False)


file_4 =  pd.read_excel("C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\Unemployment_Women.xlsx")

file_5 = file_3[["DATE", "UNRATE","LNS14000001"]].merge(file_4[["DATE", "LNS14000002"]], on = "DATE", how = "left")

file_5.to_excel("C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\Master_Data.xlsx", index = False)

df = pd.read_excel("C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\Master_Data.xlsx")
data_select = pd.DataFrame(df)
print(data_select)
column_rename = data_select.rename(columns={'DATE':'DATE','UNRATE':'UnEmploymentRateUS','LNS14000001':'Unemployment_Rate_Men','LNS14000002':'Unemployment_Rate_Women'},inplace=True)
data_select.to_excel("C:\\Users\\13148\\Google Drive\\Capestone\\Unemployment_Project\\Master_Data_rename_Col.xlsx", index = False)
print(data_select)
print(column_rename)