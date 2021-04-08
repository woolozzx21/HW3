#6번, B835193 석채원
num1 = int(input("숫자 1:"))
num2 = int(input("숫자 2:"))
num3 = int(input("숫자 3:"))
List = [num1,num2,num3]

mini = min(num1,num2)
mini = min(mini,num3)
List.remove(mini)

big = max(num1,num2)
big = max(big,num3)
List.remove(big)

print("중간값은",List[0])

