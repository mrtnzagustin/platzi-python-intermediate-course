def read():
    numbers = []
    with open("files/numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Agustin", "Florencia", "Ramiro", "Santiago"]
    with open("files/names.txt", "w", encoding="utf-8") as file:
        for name in names:
            file.write(name)
            file.write("\n")

def run():
    read()
    write()

if __name__ == '__main__':
    run()