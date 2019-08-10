""" To check if sequence is distinct or not using set """

def is_unique(list):
    n = len(list)
    n2 =len(set(list))
    if ( n == n2):
        return True
    else:
        return False


list = [3,3,8,5,7]
print(is_unique(list))
