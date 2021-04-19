"""parse this file to display the frequency of
occurrence of each word in this text file. Find the 3 most frequent
words as well."""

import re

def countWordFreq():
    result={}
    file=open('LICENSE.txt','r')
    content=file.read().strip()

    words=[word  for word in re.split("[^\w+\d+]+",content) if not word.isdigit()]


    for item in words:
        if item.lower() in result:
            result[item.lower()]+=1
        else:
            result[item.lower()]=1

    return dict(sorted(result.items(),key=lambda x:x[1],reverse=True))

def topN(result,n):
    return list(result.items())[:n]

print("****************")
print("The frequnecy of a words are as follows")
print(countWordFreq())
result=countWordFreq()
print("top 3 words",topN(result,3))



