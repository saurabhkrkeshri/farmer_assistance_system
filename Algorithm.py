import pandas as pd
import range
df = pd.read_csv('/home/saurabh/Documents/Mini_Project/test_set_1_copy.csv')
for index in df.index:
    if df.loc[index,"N"] < range.min_N:
        print("Add Nitrogeneous fertilizer")
        print("Current Nitrogen content:",df.loc[index,"N"])
        print("Permissiable Range:",range.min_N,"-",range.max_N)
        print("Shortage of:",range.min_N - df.loc[index,"N"])
    if df.loc[index,"N"] > range.max_N:
        print("Current Nitrogen content:",df.loc[index,"N"])
        print("Permissiable Range:",range.min_N,"-",range.max_N)
        print("Excess of:",df.loc[index,"N"] - range.max_N)
    if df.loc[index,"P"] < range.min_P:
        print("Add Phosphorus fertilizer")
        print("Current Phosphorus content:",df.loc[index,"P"])
        print("Permissiable Range:",range.min_P,"-",range.max_P)
        print("Shortage of:",range.min_P - df.loc[index,"P"])
    if df.loc[index,"P"] > range.max_P:
        print("Current Phosphorus content:",df.loc[index,"P"])
        print("Permissiable Range:",range.min_P,"-",range.max_P)
        print("Excess of:",df.loc[index,"P"] - range.max_P)
    if df.loc[index,"K"] < range.min_K:
        print("Add Potassium fertilizer")
        print("Current Potassium content:",df.loc[index,"K"])
        print("Permissiable Range:",range.min_K,"-",range.max_K)
        print("Shortage of:",range.min_K - df.loc[index,"K"])
    if df.loc[index,"K"] > range.max_K:
        print("Current Potassium content:",df.loc[index,"K"])
        print("Permissiable Range:",range.min_K,"-",range.max_K)
        print("Excess of:",df.loc[index,"K"] - range.max_K)
    

