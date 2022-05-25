def add_surname(d):
    
    with open ('log.csv', 'a') as file:
        file.write('Фамилия: {}\n'
                    .format(d))
def add_name(d):
    
    with open ('log.csv', 'a') as file:
        file.write('Имя: {}\n'
                    .format(d))
def add_number(d):
    
    with open ('log.csv', 'a') as file:
        file.write('Номер телефона: {}\n'
                    .format(d))
def add_description(d):
    
    with open ('log.csv', 'a') as file:
        file.write('Описание: {}\n'
                    .format(d))

