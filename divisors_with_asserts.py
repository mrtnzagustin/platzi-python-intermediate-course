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
        number = input("Give me a number to show its divisors: ")
        # Error if number is negative or if no number
        assert number.isnumeric(), "You must give me a positive number"
        print(divisors(int(number)))
    except Exception as error:
        print("Error: " + error.__str__())

if __name__ == '__main__':
    run()