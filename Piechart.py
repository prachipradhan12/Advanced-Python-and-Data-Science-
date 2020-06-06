import matplotlib.pyplot as plt

country=['India','Srilanka','Nepal','Bhutan','Myanmar']
medals=[50,20,2,30,25]
explode=[0,0,0,0.1,0]

plt.pie(medals,labels=country,explode=explode,shadow=True,autopct='%.2f%%')

plt.show()