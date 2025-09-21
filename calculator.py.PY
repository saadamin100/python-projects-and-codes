def calculator():
 try:
    num1 = int(input("Enter the num1 "))
    num2 = int(input("Enter the num2 "))

    operator = input("Enter the operator(+, -, /, *, %) ")

    if operator == '+':
     print(num1 + num2)
    elif operator == '*':
     print(num1 * num2)
    elif operator == '/':
     print(num1 /num2)
    elif operator == '-':
     print(num1 - num2)
    elif operator == '%':
      print(num1 % num2)
    else:
     print(f"The operator is incorrect!!!")

    if num1 == 0 or num2 == 0:
          raise ZeroDivisionError("hey zero will not allowed")

 except ValueError:
     print("Invalid input. Please enter numbers only.")
    
calculator() 


   