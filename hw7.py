# Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer
def reverse(number):
    stack = []
    num_len = len(str(number))
    result = ""

    for num_char in str(number):
       stack.append(num_char)

    for i in range(len(stack)):
        result += stack.pop()

    print(result)
    return int(result)

"""
Variable table:

----------------------------------------------------------
|      Variable          |           Value               |
----------------------------------------------------------
|       number           |      [34, 5784, 286, 3479]    |
----------------------------------------------------------
|       stack            |  [3,4,5,7,8,4,2,8,6,3,4,7,9]  |
----------------------------------------------------------
|       num_len          |           [2, 4, 3, 4]        |
----------------------------------------------------------
|       result           |       each integer [:1]       |

"""

# Palindrome Number
# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the 
# same backward as forward.

def palindrome(num):
    num = str(num)
    if (num == num[:: - 1]):
        print("{} is a palidrome".format(num))
    else:
        print("{} not a palindrome".format(num))

"""
Variable table:

----------------------------------------------------------
|      Variable          |           Value               |
----------------------------------------------------------
|       num              |      [33, 56, 25, 30303]      |
----------------------------------------------------------

"""


reverse(34)
reverse(5784)
reverse(286)
reverse(3479)

palindrome(33)
palindrome(56)
palindrome(25)
palindrome(30303)