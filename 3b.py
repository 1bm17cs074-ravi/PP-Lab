from random import randint
from string import printable

str1 = printable[:70]
print(str1)
for i in range(6):
    print(str1[randint(0,70)],end="")

    
