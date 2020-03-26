!pip install matplotlib

import matplotlib.pyplot as plt
x=[2,9,4,6]
y=[7,3,4,5]
plt.xlabel("distance")
plt.ylabel("time")
plt.plot(x,y)
plt.scatter(x,y,s=200,label="distance and time")
plt.grid(color="green")
plt.legend()
#plt.show()
plt.bar(x,y,label="height of stations")

scores=[123,332,21,312,443]
players=["sehwag","dhoni","bhubhneshwar","sachin","virat"]
plt.pie(scores,labels=players, explode=(0.2,0,0,0,0.1),shadow="True",autopct=('%1.1ff%%'))


#from urllib.request import Request ,urlopen
#from bs4 import BeautifulSoup
#url=Request('https://corona.help')
#data= urlopen(url)
#data.read()
#print(data)

import requests
page=requests.get('https://corona.help')    
print(page.content)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')
print('Total number of confirmed cases are:')
number = soup.find_all('h2')[1].get_text()
print(number)

print('out of which confirmed cases today are:')
numbertoday=soup.find_all('h2')[4].get_text()
print(numbertoday)
print('number of cases in turkey are:')
numturkey=soup.find_all('td',class_="text-warning")[41]
for i in numturkey:
  print(i)
#print(soup.prettify())
#list(soup.children)
