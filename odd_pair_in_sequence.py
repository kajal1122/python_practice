""" To find a distinct pair , whose product is odd """

def odd_pair(list):
    count = 0
    for i in range(len(list)):
        if(i % 2 != 0):
            count += 1
    if(count >= 2):
        return True
    else:
        return False

list = [2,8,9,11,45]
print(odd_pair(list))
