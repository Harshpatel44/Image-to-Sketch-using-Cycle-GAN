import csv
import requests
f=open("phone_dataset .csv","r")
csv_reader = csv.reader(f, delimiter=',')
count=0
for row in csv_reader:
    if(count==0):
        print('heading')
    if(count>0 and count<1000):
        image_link=row[-1]
        ext=image_link.split('.')[-1]
        with open('dataset/phone'+str(count)+'.'+str(ext),'wb') as f:
            f.write(requests.get(image_link).content)
    if(count>1000):
        break
    count += 1
print(count)