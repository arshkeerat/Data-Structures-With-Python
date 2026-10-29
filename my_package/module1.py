def check_prime(num):
    if num ==1:
        print(" prime no")
        return
    if num==2 or num==3:
        print("prime no")
        return
    if num%2==0 or num%3==0:
        print("Not prime")
        return
    count=5
    for count in range(5,num,count+6):
        if (num % count) == 0 or ((num) % count+2==0):
            print("Not prime")
            return
    print("prime no")

def calculate_factorial(num):
    fact = 1
    if num > 0:
        for count in range(1, num + 1):
            fact *= count
        print("\nFactorial of ", num, " is", fact)
    elif num == 0:
        print("\nFactorial of 0 is 1")
    else:
        print("\nPlease enter a non-negative integer !")