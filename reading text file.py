#reading text file

file1= open("Test File.txt","a+")

print(file1.read())
print()

file1.seek(0)
print(file1.readlines())
print()

file1.seek(0)
print(file1.readline(9))

lines= file1.readlines()
listt=[]


from textblob import TextBlob

import matplotlib.pyplot as plt

for i in lines:
    blob= TextBlob(i)
    listt.append(blob.sentiment.polarity)
    
countp=0
countn=0
countneu=0

for i in listt:
     if i>0:
        countp=countp+1
     elif i<0:
        countn=countn+1
     else:
        countneu=countneu+1

l1=[countp,countn,countneu]

# labels= ['positive','negative','neutral']

plt.pie(l1,autopct='%1.1f%%')
plt.show()

