import requests

url = "https://raw.githubusercontent.com/enikolaev/IT-and-Programming/main/data/pract8/pr8.txt"
response = requests.get(url)
with open("pr8.txt", "wb") as f:
    f.write(response.content)


import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = np.loadtxt('pr8.txt')  
x = data[:, 0].reshape(-1, 1)
y = data[:, 1]

model = LinearRegression()  
model.fit(x, y)

plt.scatter(x, y, color='blue')
plt.plot(x, model.predict(x), color='red')
plt.title('Linear Regression')
plt.show()