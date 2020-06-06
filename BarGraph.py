import socket
import requests
import matplotlib.pyplot as plt
city_name=['Mumbai','Dubai','Singapore']
city_temp=[]
for c in city_name:
	try:
		socket.create_connection(("www.google.com",80))
		print("u r connected")
		city=input("Enter location name ")
		a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2="&q="+ city
		a3="&appid=c6e315d09197cec231495138183954bd"
		api_address=a1+a2+a3
		res1=requests.get(api_address)
		print(res1)
		data=res1.json()
		print(data)
		main=data['main']
		print(main)
		temp=main['temp']
		print("temp =",temp)
		city_temp.append(temp)
	
	except OSError as e:
		print("check network",e)
plt.bar(city_name,city_temp,color=["r","g","b"],width=0.20)
plt.title("Weather Report")
plt.xlabel("City Names")
plt.ylabel("City Temp")
plt.grid()
plt.show()















