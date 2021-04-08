#5번, B835193 석채원
import random

lotteryNumber = random.randint(10, 99)
Pinput = int(input("복권 번호(10-99사이)를 입력하시오:"))
print("복권번호는",lotteryNumber,"입니다.")

Lten = lotteryNumber//10
Pten = Pinput//10
Lone = lotteryNumber%10
Pone = Pinput%10

if  Lten==Pten or Lone==Pone:
    if Lten==Pten and Lone==Pone:
         print("상금은 100만원!")
    else:
        print("상금은 50만원.")
else:
    print("상금은 없습니다.")
   

    