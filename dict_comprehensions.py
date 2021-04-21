def run():
    dict_cube_numbers = {}
    # stores the cube of numbers from 1 to 100 that are not divisible by 3
    for i in range (1, 101):
        if i % 3 != 0:
            dict_cube_numbers[str(i)] = i**3
    
    # variant using comprehensions
    dict_cube_numbers_variant = { str(i): i**3 for i in range(1, 101) if i % 3 != 0 }
    
    print(dict_cube_numbers)
    print(dict_cube_numbers_variant)
        

if __name__ == '__main__':
    run()