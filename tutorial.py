#message="hello world"
#print(message)
#print(len(message))#prints len of string from 1
#print(message[0:5])#prints the range from 0 to 4th index of the message
#def hello_func(greeting,name):
#    return '{},{}'.format(greeting,name)
#print(len('Test'))
#print(hello_func('hi',name='Corey'))


#def student_info(*args,**kwargs):#single star for list and double star for dictionary
#    print(args)
#    print(kwargs)
#student_info('math','art',name='john',age=22)

month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)\

def days_in_month(year,month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month==2 and is_leap(year):
        return 29
    return month_days[month]
print(days_in_month(2017,2))
