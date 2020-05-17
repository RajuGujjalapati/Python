import requests
import os

#os.mkdir(r'C:\Users\New\OneDrive\Desktop\PYTHON\PYTHON CLASS\REQUEST MODULE/file')


#x = requests.get('https://www.w3schools.com/colors/default.asp')
#print(x.status_code)#to get status code like 200,300,400
#print(x.text)#to get the html code
#p=open(r'C:\Users\New\OneDrive\Desktop\PYTHON\PYTHON CLASS\REQUEST MODULE/rs.html','w')
#p.write(x.text)#('content')this will gives you the images
#p.close()

#print(x.headers)#entire pag info. like server,image type,content type,/setc...


api_key=('trnsl.1.1.20200215T044716Z.7cd85b38a3f4513a.3e7334afa999682d654de84264c04c18174a092f')
url=('https://translate.yandex.net/api/v1.5/tr.json/translate')
trans=('hello good bye how are you now ')
parame=dict(key=api_key, text=trans, lang='en-te')
res=requests.get(url, params=parame)
print(res.text)#this is enough to get text
print(res.headers)#entire page info.
json=res.json()#it a method which conversts the response to json object
print(json['text'][0])


