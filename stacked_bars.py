import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")
df = pd.DataFrame({
    "Engineering":[56,13,1],
    "Computer Science":[77,23,4],
    "English Lit":[35,48,9],
    "Economics": [65,45,19]
}, index=["Male", "Female", "Non-Binary"])

df = df.T

my_plot = df.plot.barh(stacked = True, colormap = "plasma")
plt.xlabel("Frequency")
# plt.ylabel("Subject")
plt.ylabel("Gender")
plt.title("Gender Variation between Subjects")


plt.show()