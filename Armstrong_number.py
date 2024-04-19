def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = 0
    for digit in num_str:
        digit = int(digit)
        sum_of_powers += digit ** num_digits
    return sum_of_powers == number 
num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")