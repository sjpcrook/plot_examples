import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df = pd.DataFrame({
    "Locations" : [
    "Twitter",
    "Facebook",
    "LinkedIn",
    "Indeed",
    "Instagram"
],
    "Responses" : [3,11,16,13,2],
})

df = df.sort_values("Responses", ascending=False)
bar_colours = ["red" if x==df["Responses"].max() else "blue" for x in df["Responses"]]


# plt.bar("Locations", "Responses", data = df, color=bar_colours)
# plt.xlabel("Advert Location")
# plt.ylabel("Applications Received")


# plt.barh("Locations", "Responses", data = df, color = bar_colours)
# plt.ylabel("Advert Location")
# plt.xlabel("Applications Received")


plt.title("Return from Job Postings by Location")
plt.show()