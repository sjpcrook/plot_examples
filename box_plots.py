import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

dev_ages=[
        45, 23, 57, 27, 37, 39, 61, 48, 23, 27, 
        59, 60, 28, 41, 25, 39, 22, 46, 48, 52, 
        38, 41, 52, 30, 46, 62, 25, 34, 52, 35, 
        48, 43, 21, 40, 22, 22, 57, 25, 21, 30, 
        55, 50, 54, 30, 43, 40, 53, 46, 36, 61, 
        35, 39, 40, 31, 29, 65, 28, 57, 39, 36, 
        20, 49, 42, 29, 62, 52, 29, 57, 39, 32, 165
        ]
df = pd.DataFrame({"Dev Ages": dev_ages})

# print(df.describe())

plt.boxplot(dev_ages, vert=0)
plt.xlabel("Age")
plt.title("Ages of our Developers")
plt.show()