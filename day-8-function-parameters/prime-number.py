#Write your code below this line 👇

#solution in the video
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
    
def prime_checker(number):
    test_complete = False
    divisor = 2
    while not test_complete:
        if number == 1:
            print("It's a prime number.")
            test_complete = True
        result = number % divisor
        if (result == 0) and (divisor != number):
            print("It's not a prime number.")
            test_complete = True
        divisor += 1
        if divisor == number:
            print("It's a prime number.")
            test_complete = True




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
