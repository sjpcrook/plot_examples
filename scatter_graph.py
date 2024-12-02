import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

number_of_placements=list(range(1,11))
responses_received = [14, 21, 34, 36, 45, 51, 54, 63, 78, 92]

plt.scatter(number_of_placements, responses_received)
plt.xlabel("Number of Placements")
plt.ylabel("Responses Received")
plt.title("Job Posting Junior Dev Role")


number_of_placements=np.array(number_of_placements)
responses_received=np.array(responses_received)

m,c = np.polyfit(number_of_placements, responses_received, 1)
# print(m,c)

plt.plot(number_of_placements, m*number_of_placements+c)
plt.show()