# Coding Syntax Problem 1
# Given a list of n numbers, determine 
# if it contains any duplicate numbers.

def locate_duplicates(arr):
    dictionary = {}

    for element in arr:
        try:
            #get dictionary element and add one to it
            dictionary[element] += 1
        except:
            #dictionary if it already has an element of 1
            dictionary[element] = 1
    
    for element in dictionary:
        #if element is seen more than once
        if(dictionary[element] > 1):
            print(element, end=" ")
    print("\n")

# ----------------------------------------------------------
# ----------------------------------------------------------
# COMMUNICATION STEPS:

# I create an empty dictionary to store any range of numbers
# I make two loops to check for the ammount of times a number
# appears in the dictionary and if it appears more than once,
# it is therefore a duplicate and is printed

# ----------------------------------------------------------
# ----------------------------------------------------------


# Coding Syntax Problem 2
# You are given two non-empty linked lists representing 
# two non-negative integers. The digits are stored in 
# reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
            print(ret)
        return ret

# ----------------------------------------------------------
# ----------------------------------------------------------
# COMMUNICATION STEPS:

# First, I set the two numbers to variables. Then, 
# I get the modulo of those numbers and store it to ret (return)
# Then, a test case to make sure that numbers are not None or 0 runs
# in the form of if statements

# ----------------------------------------------------------
# ----------------------------------------------------------



if __name__ == "__main__":
    random_list = [40, 93, 82, 34, 50, 83, 48, 14, 
        20, 99, 11, 29, 65, 6, 37, 62, 97, 85, 81, 63, 15, 86,
        53, 71, 55, 96, 49, 45, 94, 77, 16, 10, 3, 31, 75, 78, 
        26, 71, 55, 31, 97]
    locate_duplicates(random_list)

    sol = Solution()
    sol.addTwoNumbers(ListNode(5), ListNode(6))