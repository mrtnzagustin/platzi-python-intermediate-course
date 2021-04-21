def run():
    # numbers up to 5 digits that are divisible by 4, 6 and 9
    list = [ i for i in range(1, 100000) if i % 4 == 0 == i % 6 == i % 9 ]

    print(list)

if __name__ == '__main__':
    run()