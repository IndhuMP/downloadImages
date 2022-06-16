import os
import urllib.request

news = ['sf_chronicles','newyork_times']
days = ['01', '02', '03', '04']
for new in news:

    try:
        print("NO")
        for day in days:
            print("now",day)
            url = 'https://img.kiosko.net/2022/06/'+day+'/us/'+new+'.200.jpg'
            name = new+day+'.jpg'
            urllib.request.urlretrieve(url, name)
            print("Yes")

    except:
        pass
