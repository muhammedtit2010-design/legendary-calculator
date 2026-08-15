print("=== الآلة الحاسبة ===")

num1 = float(input("أدخل الرقم الأول: "))
operator = input("أدخل العملية (+ - * /): ")
num2 = float(input("أدخل الرقم الثاني: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "لا يمكن القسمة على صفر"
else:
    result = "عملية غير صحيحة"

print("النتيجة:", result)
 
 
