Val_x=7 #global value
def test_func():
    print(Val_x)
    return 0
def glob_var():
    print(Val_x)
def print_pat(n): 
    #global Val_x-changes the variable evrywhere in the program
    Val_x=3 #local variable
    print(Val_x)
    for i in range(n+1):
        print("#"*i)
        print("*"*i)
        print("$"*i)
    test_func()
    return 0
test_func()
n=int(input())
print_pat(n)
print(Val_x)



