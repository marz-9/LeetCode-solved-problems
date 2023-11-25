class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if (num == 1):
            return False
        summ=1
        #we started from 2, because 1 cannot be a perfect number
        #and because if we made the range starts from 1 the case 1 to get the output as True will be False
        #in the range we iterate from 2 up to the square root of the given number
        for i in range (2, int(num**0.5)+1):
            #Checking if the given number is a divisor of the given number
            if(num%i == 0):
                summ+=i + num//i
        #if the comparision is equal to each other return True
        return summ == num