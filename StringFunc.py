import re
sentence="Transforming life through excellence in education and research. Excellence in education, grounded in ethics and critical thinking, for improvement of life. An innovation ecosystem to extend knowledge and solve critical problems. Happy, accountable, caring and effective workforce and students. Active collaborationwith national and international industries and universities for productivity and economic development. Service to the region and world through knowledge and compassion."  
print(sentence)
#words=re.sub("[&,:.]","",sentence)
words=sentence.replace("&","")
words=words.replace(",","")
words=words.replace(".","")
words=words.replace("a","")
words=words.replace("an","")
words=words.replace("the","")
words=words.replace("would","")
words=words.replace("should","")
words=words.replace("could","")

print("----------------------------------------------")
print(words)
wordsList=words.split()
print(wordsList)      
