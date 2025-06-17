num1 = int(input("Enter the first nunber:"))
num2 = int(input("Enter the second nunber:"))

print(f"{num1} x {num2} = {num1 * num2}")

# หากผลคูณของเลขทั้งสองตัวมากกว่า 0: ให้ทำงานตรงนี้
if num1 * num2 > 0:
	print("The result is positive.")
	
# หากผลคูณของเลขทั้งสองตัวน้อยกว่า 0: ให้ทำงานตรงนี้
elif num1 * num2 < 0:
	print("The result is negative.")

# หากทั้งสองเงื่อนไขไม่เป็นจริง: ให้ทำงานตรงนี้แทน
else:
	print("The result is positive and negative.")