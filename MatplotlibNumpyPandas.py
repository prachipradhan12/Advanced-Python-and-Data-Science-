import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("language.csv")
lan=data['LANGUAGE'].tolist()
job17=data['JOBS_2017'].tolist()
job18=data['JOBS_2018'].tolist()


x=np.arange(len(lan))
plt.bar(x,job17,width=0.30,label='JOBS_17')
plt.bar(x+0.30,job18,width=0.30,label='JOBS_18')
plt.xticks(x,data)
plt.xlabel("JOBS")
plt.ylabel("LANGUAGES ")
plt.grid()
plt.legend()
plt.show() 