'''


67. Add Binary

Given two binary strings a and b, return their sum as a binary string. 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''




def addBinary(a,b):
        # Convert the binary strings to integers, add them, and convert back to binary
    result = bin(int(a, 2) + int(b, 2))[2:]   # [2:] removes the "0b" prefix

    
    print (result)


addBinary("1010","1011")