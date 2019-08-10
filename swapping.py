""" Swaping with help of tuple return """
a=int(input())
b=int(input())

def swap(a,b):
    return(a,b)

b,a= swap(a,b)
print(a)
print(b)
