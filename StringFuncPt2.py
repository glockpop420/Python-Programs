sentence="Transforming life through excellence in education and research. Excellence in education, grounded in ethics and critical thinking, for improvement of life. An innovation ecosystem to extend knowledge and solve critical problems. Happy, accountable, caring and effective workforce and students. Active collaboration with national and international industries and universities for productivity and economic development. Service to the region and world through knowledge and compassion."
word="welcome"
word_UC=word.capitalize()
print(word_UC)
sentence_UC=sentence.upper()
sentence_TT=sentence.title()
sentence_SC=sentence.swapcase()
test="    Example   "
test_SR=test.strip()
sentence_SP=sentence.split()
sentence_RS=sentence.rsplit("a")
print(sentence_RS)
word_count=sentence.count("in")
print(word_count)
eFlag=sentence.find("in")
word_sample="Transforming"
words_EW=word_sample.endswith("a")
word_index=sentence.index("Harleys")
print(word_index)
Mob_no="900358777"
print(Mob_no.isdigit())
print(Mob_no.isdecimal())
print(Mob_no.isalnum())
name="ANBALAGAN"
if name.isalpha():
    print("Name is validated")
else:
    print("Name is invalid")

if len(Mob_no)==10:
    if Mob_no.isnumeric():
        print("Mobile number is valid")
    else:
        print("Invalid mobile number")
else:
    print("Invalid mobile number")

Pancard="AAAAC6573E"#this should be the original format of the pancard id
if Pancard.isalnum():
    print("Pan card number id valid")
else:
    print("Invalid Pan Card Number")


