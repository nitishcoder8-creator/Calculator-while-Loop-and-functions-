def calculation(num1,num2):
    sign = input("enter operation(+,-,*,/) : ")
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1/num2
    elif sign == '**':
        square = (f"{num1**2} , {num2**2}")
        return square
    else :
        print("\nsign not matched.")    
active = True
while active :
    print("\nThis is calculator.")
    A = int(input("enter num1 : "))
    B = int(input("enter num2 : "))
    calculated_number = calculation(A,B)
    print(f"\nexpression result = {calculated_number}\n")
    energy = input("kya aapke pass energy hai aur karne ka? (yes/no) : ")
    if energy == 'no':
        active = False
