def division(a, b):
    if b == 0:
        raise ValueError("You cant divide a number by zero")
    return a / b


def run():
    try:
        division(1, 0)
    except Exception as exception:
        print("Error from except: " + exception.__str__())
    else:
        print("This line is executed only if no exception is raised")
    finally:
        print("This line is always executed")


if __name__ == '__main__':
    run()