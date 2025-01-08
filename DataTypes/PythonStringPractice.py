def is_symmetrical_or_palindrome(mystr="KhoKho"):
    """
    Method responsible for checking if a given string is symmetrical or palindrome.
    NOTE:
    Symmetrical: A string is said to be symmetrical if both halves of the string are same
    Palindrome: A string is said to be palindrome if the actual string and the reverse of the string are equal
    :param mystr: provide a string to check
    :return: NONE
    """
    if mystr[0:len(mystr) // 2] == mystr[len(mystr) // 2:]:
        print(f"{mystr} is symmetrical.")
    elif mystr == mystr[::-1]:
        print(f"{mystr} is palindrome.")
    else:
        print(f"{mystr} is neither symmetrical nor palindrome.")


def get_length_of_string_way1(mystr=' geeks '):
    """
    Method to get the length of the string
    :param mystr: Provide a string to get the length
    :return: returns the length of the string
    """
    return len(mystr)  # Here we have used the built-in function len


def get_length_of_string_way2(mystr=' geeks '):
    length = 0
    for char in mystr:
        if char != " ":
            length += 1
    return length


# enumerate function is used to loop over the iterable and keep track of the index and value associated with the
# iterable

for index, item in enumerate(range(1, 10, 2)):
    print(index, ":", item)

# count method is used to get the count occurrence of a sub-string
myname = "DibyenduDib"
print(myname.count('Dib'))


def reverse_words_in_a_string(mystr="geeks quiz practice code"):
    """
    Method to reverse words in a string.
    :param mystr: -
    :return: -
    """
    return " ".join(reversed(mystr.split(" ")))


outp = reverse_words_in_a_string()
print(outp)
