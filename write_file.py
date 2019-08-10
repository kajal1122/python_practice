''' Open a file and write something to it '''

import keyword_parameters
import add_fun

with open('sample.txt', 'w') as write_file:
    print(keyword_parameters.say_hi("Ag"), file = write_file)
    print("hiii", file = write_file)


with open('sample2.txt','w') as write1_file:
    print(add_fun.add_num(2,3), file = write1_file)
