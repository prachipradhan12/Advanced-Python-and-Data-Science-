import matplotlib.pyplot as plt
import numpy as np


products=['Laptop','Printer','Router']
reena=[10,25,15]
veena=[5,30,12]
x=np.arange(len(products))
plt.bar(x,reena,width=0.30,label='Reena')
plt.bar(x+0.30,veena,width=0.30,label='Veena')
plt.xticks(x,products)
plt.xlabel("Products")
plt.ylabel("Prices")
plt.grid()
plt.legend()
plt.show() 