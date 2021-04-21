from functools import reduce

def run():
    # Example with FILTER
    # The argument function must return true or false to add or not the actual item
    
    # Numbers from 1 to 10
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Lambda function that check if a number is pair
    is_pair = lambda number: number % 2 == 0
    
    # use filter function with is_pair and numbers and convert from an iterable to a list
    pairs_numbers = list(filter(is_pair, numbers))

    # Prints
    print(numbers)
    print(pairs_numbers)

    # Example with MAP
    # The argument function must return the value that must override the actual item
    
    # Lambda function that multiplies a number by 2
    double = lambda number: number * 2
    
    double_numbers = list(map(double, numbers))

    print(double_numbers)


    # Example with REDUCE
    # The argument function recieves two parameters and must return the value that must integrate the actual two items
    character_list = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

    # lambnda function that concat two characters
    concat = lambda a, b: a+b

    string = reduce(concat, character_list)

    print(string)


if __name__ == '__main__':
    run()