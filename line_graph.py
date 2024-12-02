import matplotlib.pyplot as plt

plt.style.use("ggplot")

years = [2018, 2019, 2020, 2021, 2022, 2023]

python_position = [7,4,4,3,4,3]

js_position = [1, 1, 1, 1, 1, 1]

sql_position = [4, 3, 3, 4, 3, 4]

ts_position = [12, 10, 9, 7, 5, 5]

plt.plot(years, python_position, label = "Python", linestyle = "dashed")
plt.plot(years, js_position, label = "JavaScript", linestyle = "dotted")
plt.plot(years, sql_position, label = "SQL", linestyle = "dashdot")
plt.plot(years, ts_position, label = "TypeScript")

plt.title("Rankings of Various Programming Languages over the Years")
plt.xlabel("Year")
plt.ylabel("Ranking")

plt.ylim(bottom = 14, top = 0)

plt.legend()
plt.show()