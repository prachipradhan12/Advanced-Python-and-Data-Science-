import bs4
import requests
res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
print(res)
soup=bs4.BeautifulSoup(res.html,'lxml')
quote=soup.find