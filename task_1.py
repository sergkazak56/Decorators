"""
Задание 1:
Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
"""
import datetime

def logger(func):
    def inner(*args, **kwargs):
        with open('files/first_file.txt', 'w', encoding='utf-8') as ff:
            date_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            output_str = f'Дата и время запуска функции: {date_time};\nИмя функции:{" " * 18}"{func.__name__}";\n'
            output_str += f'Аргументы функции:{" " * 12}{args}, {kwargs};\nРезультат функции:{" " * 12}{result};'
            ff.write(output_str)
        return result
    return inner

@logger
def summator(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

if __name__ == '__main__':
    summator(1, 2, 3, d=4, e=5, f=15)

