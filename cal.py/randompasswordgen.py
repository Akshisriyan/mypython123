import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits

len_characters = int(input("How long should the password be?"))

for x in range(len_characters):
    password =  "".join(choice(characters))
    print (password, end="")

#For length to be random, we can use the below code:
import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
for x in range(randint(8, 16)):
    password =  "".join(choice(characters))
    print (password, end="")