def func(sentence):  
    count={}
    for i in sentence:
        if i in count:
            count[i]+=1
        elif i==" ":
            continue
        elif i=="'":
            continue
        else:
            count[i]=1
    return count
sentence=input()
sentence=sentence.strip("'")
sentence_split=sentence.split()
length=len(sentence_split)
char={}
for i in range(length):
    char[sentence_split[i]]=func(sentence_split[i])
print(char)
