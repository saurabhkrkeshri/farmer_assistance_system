import pandas as pd
index = 0
df = pd.read_csv("/home/saurabh/Documents/Mini_Project/Raw_Data_Cotton.csv")
df.dropna(inplace=True)
for index in df.index:
    if (df.loc[index,"N"] > 99) or (df.loc[index,"N"] < 60) or (df.loc[index,"K"] > 45) or (df.loc[index,"K"] < 16) or (df.loc[index,"P"] > 60) or (df.loc[index,"P"] < 35) or (df.loc[index,"temperature"] > 45) or (df.loc[index,"temperature"] < 16) or (df.loc[index,"humidity"] > 84.96) or (df.loc[index,"humidity"] < 63.69) or (df.loc[index,"ph"] > 7.86) or (df.loc[index,"K"] < 5.005) or (df.loc[index,"rainfall"] > 298) or (df.loc[index,"rainfall"] < 66.72):
        df.drop(index,axis = 0, inplace=True)
df.to_csv(r'/home/saurabh/Documents/Mini_Project/cleaned_data.csv',index = False)
print(df.to_string())