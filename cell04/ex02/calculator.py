num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
div = num1 / num2

if div == int(div):
    # ถ้าใช่ แสดงผลลัพธ์เป็นจำนวนเต็ม
    print(f"{num1} / {num2} = {int(num1 / num2)}")
else:
    # ถ้าไม่ใช่ แสดงผลลัพธ์ที่มีทศนิยม
    print(f"{num1} / {num2} = {div}")

print(f"{num1} * {num2} = {num1 * num2}")
