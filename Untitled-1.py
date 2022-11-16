import webbrowser
import pandas as pd
import os 
import time
import urllib.request
import ast
image_set = "D:\image_set"
file = pd.read_csv('abc.csv', sep=',', encoding='cp949')


names = []
url = []

for i in range(len(file.index)):
    for j in range(len(file.columns)):
        if j == 0:
            names.append(file.iloc[i][j])
        else:
            url.append(file.iloc[i][j])


total_percent = 0
error_cnt = 0
for n in range(len(names)):
    try :
        file_path = "D:/image_set/"
        line = list(names[n])
        for k in range(len(line)):
            if line[k] == '/' :
                line[k] = ','
            
        names[n] = line
        name = ''.join(names[n])+ '.jpg'
        path = file_path+name
    
        url_link = ''.join(url[n])
    
    
        urllib.request.urlretrieve(url_link, path)
        time.sleep(1)
        os.system('cls')
        total_percent += 0.004
        print("Percent : {0:.2f} %".format(total_percent))
    except:
        error_cnt +=1
        os.system('cls')
        print("{}개의 이미지 소실".format(error_cnt))
        

    
    
    