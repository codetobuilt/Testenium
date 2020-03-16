from bs4 import BeautifulSoup
import requests

s = requests.Session()
url = 'http://www.uwindsor.ca' #url to retrieve data from
page = s.get(url).text
file_object = open('report.txt', 'w+')

soup = BeautifulSoup(page, "html.parser")
images = []
for div in soup.find_all('div'): #lists all image alt text
    for img in div.find_all('img', alt=True,src=True):
        images.append(img)
        #print(img['src']+'->'+img['alt'])

myset = set(images)

for e in myset: 
	print(e['src']+'->'+e['alt'])
	file_object.write(e['src']+'->'+e['alt'])
	file_object.write("\n")

print('<---------------------------- Images with empty text alternative -------------------------->')
file_object.write('<---------------------------- Images with empty text alternative -------------------------->')
file_object.write("\n")
print('According to Ontario accessibility law, it is advisable to have text alternatives for all non-text media')
file_object.write('According to Ontario accessibility law, it is advisable to have text alternatives for all non-text media')
file_object.write("\n")
for e in myset: 
	if(len(e['alt'])==0):
		print(e['src']+'->'+e['alt'])
		file_object.write(e['src']+'->'+e['alt'])
		file_object.write("\n")

file_object.close()

