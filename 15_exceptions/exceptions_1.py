# specific exceptions
# total = 0 # not necessary
try:
    num1 = float(input("enter a number"))
    num2 = float(input("enter a number"))
    total = num1 / num2
    # print(total) # better in an else as in itself it won't throw an error
# except ValueError as e:
#     print("Error: something went wrong", e)
#     # Error: something went wrong could not convert string to float: 'one'
except ZeroDivisionError as e:
    print("Error: something went wrong", e)
    # Error: something went wrong float division by zero
except Exception as e:
    print("Something else went wrong", e)
else:
    print(total) # if no exception
finally:
    print("Thankyou and goodbye") # regardless of exception

print("end program")

