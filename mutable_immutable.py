
def scale(data, factor):
    for val in data :
        val *= factor
    return data

data = [2,6,8]
factor = 2

print(scale(data,factor))
