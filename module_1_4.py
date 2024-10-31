#Организуйте программу:
my_string = input("YO, whats up? ")
print ("Вы ввели:" , len(my_string), "символа(ов).")  #Вывести количество символов введённого текста

#Работа с методами строк:
print("YO, whats up? " .upper())  #Выведите строку my_string в верхнем регистре.
print("YO, whats up? " .lower())  #Выведите строку my_string в нижнем регистре.
print("YO, whats up? " .replace(" ", "#"))  #Измените строку my_string, удалив все пробелы.
my_string = "YO, whats up? "  #Выведите первый символ строки my_string.
print(my_string [0])
my_string = "YO, whats up? " #Выведите последний символ строки my_string.
print(my_string [-2]) #последний символ пробел поэтому для наглядности вывел "?"
