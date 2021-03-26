import calc_bmi

weight = int(input("体重:"))
height = int(input("身長:"))
bmi = calc_bmi.calc_bmi(weight, height)

if bmi < 18.5:
    print("あなたはやせ気味です")
    print("あなたはやせ気味です")
elif bmi < 24.9:
    print("あなたは標準です")
    print("あなたは標準です")
elif bmi < 29:
    print("あなたはやや太り気味です")
    print("あなたはやや太り気味です")
elif bmi >= 30:
    print("あなたは太っています")
    print("あなたは太っています")
