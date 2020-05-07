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


# Palindrome Number
# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the 
# same backward as forward.

def palindrome(num):
    left = 0
    right = range(int(num)) - 1

    while right > left:
        if (num[right] != num[left]):
            print("incorrect input")
            return False
        left += 1
        right -= 1
    return True

    if left is None:
        left = 0
    if right is None:
        right = len(num) - 1
    
    return palindrome(num, "Is a Palindrome")


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

reverse(34)
reverse(5784)
reverse(286)
reverse(3479)

palindrome(33)