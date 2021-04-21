def run():
    # Traditional list
    my_list = [1, "Hello", True, 4.5]
    
    # Traditional dict
    my_dict = {
        "firstname": "Agustin",
        "lastname": "Martinez"
    }
    
    # List with dict inside
    super_list = [
        {
            "country": "Argentina",
            "population": 57000000
        },
        {
            "country": "Brazil",
            "population": 120000000
        }
    ]

    # Dict with list values
    super_dict = {
        "numbers": [1, 2, 3, 4, 5],
        "characters": ['a', 'b', 'c', 'd']
    }

    # Dict print
    for key, value in super_dict.items():
        print(key, ":", value)

if __name__ == '__main__':
    run()