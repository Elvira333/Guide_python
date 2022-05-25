path_to_file = 'log.csv'
 
with open (path_to_file) as file:                            # вывод через разделитель пробел
    for num_line, line in enumerate(file):
        num_line = 1 + num_line
        with open('separator_whitespace.csv','a') as file:
            if num_line%4!=0:
                file.write(line)
            else:
                file.write(line)
                file.write('\n')

with open (path_to_file) as file:                           # вывод через запятую
    for num_line, line in enumerate(file):
        num_line = 1 + num_line
        with open('separator_comma.csv','a') as file:
            if num_line%4!=0:
                a = line.replace('\n',', ')
                file.write(a)
            else:
                a = line.strip()
                file.write(a)
                file.write('\n')
                
        
   
                       

        

            
               



