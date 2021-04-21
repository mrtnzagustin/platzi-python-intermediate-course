# List of 100 first natural numbers to the square

def run():
    squared_natural_numbers = []
    # iteration from 1 to 100
    for i in range(1, 101):
        # Just store the squared number, if the number is divisible by 3
        if i % 3 != 0:
            squared_natural_numbers.append(i**2)
    
    # [element (for element in iterable) if condition]
    squared_natural_numbers_variant = [ i**2 for i in range(1,101) if i % 3 != 0]

    # print of elements
    print(squared_natural_numbers)
    print(squared_natural_numbers_variant)

if __name__ == '__main__':
    run()