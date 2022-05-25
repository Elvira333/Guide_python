def get_surname():
    surname = input('Фамилия: ')
    return surname

def get_name():
    name = input('Имя: ')
    return name

def get_number():
    number = input('Номер телефона: ')
    return number
def get_description():
    description = input('Описание: ')
    return description

def data_collection():
    return(get_surname(),get_name(),get_number(), get_description())

    