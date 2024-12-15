print("hello world")
name = "Jharna Dey"
value = 10

print(value)


def check_even_odd(num):
    """
    A number is an even number if it is divisible by 2 else odd
    :param num: provide a number to be verified
    :return: NONE
    """
    if num % 2 == 0:
        print(f"{num} is a even number.")
    else:
        print(f"{num} is a odd number.")


check_even_odd(num=1)
