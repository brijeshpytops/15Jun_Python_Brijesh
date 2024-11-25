# print("start")
# try:
#     a = 10
#     b = input("Enter a B: ")
#     res = a/b
# except ZeroDivisionError:
#     print("ZeroDivisionError: Division by zero is not allowed.")
# # except TypeError:
# #     print("TypeError: Invalid operand type(s) for division.")
# except NameError:
#     print("NameError: Something is not defined.")
# except Exception as err:
#     print(f"Error: {err}")
# else:
#     print(res)
# finally:
#     print("This block will always execute.")
# print("end")



# print(10/"hjdsg")

bal = 1000
wb = 5000

# if wb <= bal:
#     print("Withdrawal successful")
#     bal -= wb
#     print(f"Remaining balance: {bal}")
# else:
#     raise ValueError("Insufficent balance")

# assert:

assert wb <= bal, "Insufficent balance"