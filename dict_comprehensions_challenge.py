import math

def run():
    # stores the first 1000 natural numbers (as key) and their square as value
    dict_comprehension = { str(i): math.sqrt(i) for i in range(1, 1001) }

    print(dict_comprehension)

if __name__ == '__main__':
    run()