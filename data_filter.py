DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = list(filter(lambda dev: dev['language'] == 'python', DATA))
    all_python_devs = [dev for dev in DATA if dev['language'] == 'python']
    print(all_python_devs)

    all_platzi_workers = list(filter(lambda dev: dev['organization'] == 'Platzi', DATA)) # high order variant
    all_platzi_workers = [dev for dev in DATA if dev['organization'] == 'Platzi'] # comprehensive variant
    print(all_platzi_workers)

    all_adults = list(filter(lambda dev: dev['age'] > 17, DATA)) # high order variant
    all_adults = [dev for dev in DATA if dev['age'] > 17] # comprehensive variant
    all_adults_just_names = list(map(lambda dev: dev['name'], all_adults)) # high order variant
    all_adults_just_names = [dev['name'] for dev in all_adults] # comprehensive variant
    print(all_adults_just_names)

    data_with_old_people_flag = list(map(lambda dev: dev | { 'old': dev['age'] > 70 }, DATA)) # high order variant
    data_with_old_people_flag = [dev | { "old": dev['age'] > 70} for dev in DATA ] # comprehensive variant
    old_people = list(filter(lambda dev: dev['old'], data_with_old_people_flag)) # high order variant
    old_people = [dev for dev in data_with_old_people_flag if dev['old']] # comprehensive variant
    print(old_people)

if __name__ == '__main__':
    run()