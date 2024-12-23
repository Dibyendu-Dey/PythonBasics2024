def rev_digit_of_num(num=12345):
    """
    Function responsible for reversing digit of numbers
    :param num: provides a number to reverse
    :return: return the reverse number
    """
    assert len(str(num)) > 1, "number of digit must be greater than 1"
    rev_num = 0
    while num > 0:
        rem = num % 10  # returns the remainder of the division
        rev_num = rev_num * 10 + rem
        num = num // 10  # returns the quotient of the division
    return rev_num


def check_even_odd(num=5):
    """
    Function to check whether a number is even or odd.
    :param num: provide a number to check even odd.
    :return: returns True if a number is even number, otherwise returns False
    """
    return num % 2 == 0


def count_digit_in_a_number_way1(num=123):
    """
    WAY1
    Function to count the number of digits in an integer
    :param num: provide to number to get the count
    :return: return the count of digits
    """
    # Here we are converting the integer to string and returning the length of the string
    return len(str(num))


def count_digit_in_a_number_way2(num=123):
    """
    WAY2
    Function to count the number of digits in an integer
    :param num: provide to number to get the count
    :return: return the count of digits
    """
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

