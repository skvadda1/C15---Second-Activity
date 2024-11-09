new_file = open('the_essay2.txt' , 'x')
new_file.close()

import os
print("Checking if file exists or not.....")
if os.path.exists("the_essay2.txt"):
    os.remove("the_essay2.txt")
else:
    print("This file does not exist")


new_file = open("the_essay2.txt" , "w")
new_file.write("this is the second_essay")
new_file.close()

os.remove('the_essay2.txt')
