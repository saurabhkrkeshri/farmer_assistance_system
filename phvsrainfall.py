import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/home/saurabh/Downloads/Files/Crop_recommendation.csv")
cotton = df.head(103)
N = cotton["N"]
P = cotton["P"]
K = cotton["K"]
temperature = cotton["temperature"]
humidity = cotton["humidity"]
ph = cotton["ph"]
rainfall = cotton["rainfall"]
max_N = N.max()
min_N = N.min()
max_K = K.max()
min_K = K.min()
max_P = P.max()
min_P = P.min()
max_temp = temperature.max()
min_temp = temperature.min()
max_humidity = humidity.max()
min_humidity = humidity.min()
max_ph = ph.max()
min_ph = ph.min()
max_rainfall = rainfall.max()
min_rainfall = rainfall.min()
print("max N:",max_N)
print("min N:",min_N)
print("max K:",max_K)
print("min K:",min_K)
print("max P:",max_P)
print("min p:",min_P)
print("max temp:",max_temp)
print("min temp:",min_temp)
print("max humidity:",max_humidity)
print("min humidity:",min_humidity)
print("maxph:",max_ph)
print("min_ph:",min_ph)
print("max rainfall:",max_rainfall)
print("min rainfall:",min_rainfall)
#df.plot(x = 'rainfall', y = "humidity")
#plt.show()
#print(df.corr())