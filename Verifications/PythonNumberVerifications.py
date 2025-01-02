from DataTypes.PythonNumbersPractice import *

# call the check_even_odd function and store the output
outp = check_even_odd(num=3)

print("EVEN") if outp else print("ODD")

# call the rev_digit_of_num and store the output in an object/variable
phone_number = 7979
rev_phone_number = rev_digit_of_num(num=phone_number)
print(f"The reverse of {phone_number} is {rev_phone_number}.")
