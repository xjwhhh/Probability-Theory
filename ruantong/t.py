
import urllib.request
import csv


oldlist2=[]
totallist2=[]
res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/population/population_old.csv")

lines=res.readlines()
for i  in range(3,len(lines)):
    ii=lines[i].decode("gbk")

    print(ii)
    oldlist2.append(int(ii.split(",")[1]))


res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/population/population_total.csv")

lines=res.readlines()
for i  in range(5,len(lines)):
    ii=lines[i].decode("gbk")

    print(ii)
    totallist2.append(int(ii.split(",")[1]))

print(oldlist2)
# print(len(oldlist2))
print(totallist2)

