# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        # Your code goes here
        temp = num
        sum = 0
        while(num > 0):
                m = num % 10
                sum = sum + m ** 3
                num = num//10
        if(sum == temp):
                return True
        else:
                return False
