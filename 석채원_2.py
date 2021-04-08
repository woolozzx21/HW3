#2번, B835193 석채원
from random import randint
a = randint(1,100)
b = randint(1,100)
answer = int(input("%d + %d의 값은?"%(a,b)))
if answer==a+b:
    print("맞았습니다.")
else :
    print("틀렸습니다.")
             