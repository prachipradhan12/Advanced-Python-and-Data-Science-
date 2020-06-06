import matplotlib.pyplot as plt
months=['june','july','aug','sep','oct','nov','dec']
mumbai=[82.5,83.06,83.61,85.6,90.75,85.24,84.06]

plt.plot(months,mumbai)
plt.title("Petrol Prices")
plt.xlabel("months")
plt.ylabel("mumbai")
plt.grid()
plt.plot(months,mumbai,color='blue',linewidth=3,marker='o',markersize=10,label='Mumbai')
plt.legend()

plt.show()