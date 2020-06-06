import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("petrol_prices.csv")
month=data['MONTH'].tolist()
mumbai=data['MUMBAI'].tolist()
delhi=data['DELHI'].tolist()
chennai=data['CHENNAI'].tolist()

plt.plot(month,mumbai,label="Mumbai",linewidth=3,marker='o',markersize=10)
plt.plot(month,delhi,label="Delhi",linewidth=3,marker='o',markersize=10)
plt.plot(month,chennai,label="Chennai",linewidth=3,marker='o',markersize=10)
plt.title("Petrol Prices")
plt.xlabel("Months")
plt.ylabel("Prices")
plt.savefig('line.png')
plt.legend()
plt.grid()
plt.show()