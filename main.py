#Program to find the number of 0 bits and 1 bits present in a number
#function taking our number input
def numberofbits(n):
    ones=0
    zeros=0
    #While our number is greater than 0 check lastbit
    while(n):
        #Use the and operator to check if lastbit is 1 or 0
        if(n&1==1):
            ones+=1
        else :
            zeros+=1
        #Right shift the number remove the last bit that was checked above
        n>>=1
    print('\nOnes=',ones,'Zeros=',zeros)
number=int(input('Enter your number'))
numberofbits(number)    
