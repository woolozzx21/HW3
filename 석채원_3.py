#3번, B835193 석채원
weight=int(input("무게(킬로그램):"))
height=float(input("키(미터):"))
BMI = weight/(height**2)
print("당신의 BMI:%f" %BMI)

if BMI>=20 and BMI<=24.9:
    print("정상입니다.")
elif BMI>=25 and BMI<=29.9:
    print("과체중입니다.")
elif BMI>=30:
    print("비만입니다.")
           