try:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the Second number : "))
    num3 = num1/num2
    print(num3)
except ZeroDivisionError:
    print("Please Enter Valid Denominator")
except ValueError:
    print("Enter the Valid Number")
except Exception as e:
    print("Error occurred : ", e)
