def divisors(number):
    divisors = []
    # Test from 1 to number if the number is divisible and collect al divisors
    for divisor in range(1, number+1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors

def run():
    try:
        # Ask for a number
        number = int(input("Give me a number to show its divisors: "))
        # Error if number is negative
        if number < 0:
            raise ValueError("Your number cant be negative")
        print(divisors(number))
    except ValueError as value_error:
        print("Error: " + value_error.__str__())

if __name__ == '__main__':
    run()