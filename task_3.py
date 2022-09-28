"""
Задание 3
Применить логгер к приложению из любого предыдущего д/з.
"""
import json
import os

PATH = "files/employees.json"

def logger_path(path):
	def logger(func):
		def inner(*args, **kwargs):
			if os.path.getsize(path):
				with open(path, 'r', encoding='utf-8') as f:
					json_data = json.load(f)
			else:
				json_data = []
			json_data.append(func(*args, **kwargs))
			with open(path, "w", encoding='utf-8') as f:
				json.dump(json_data, f, ensure_ascii=False, indent=4)
			return json_data
		return inner
	return logger

@logger_path(PATH)
def add_employee():
	empl_dict = {}
	empl_dict['first_name'] = input('Имя: ')
	empl_dict['lastname'] = input('Фамилия: ')
	empl_dict['age'] = int(input('Возраст: '))
	children_quantity = int(input('Кол-во детей: '))
	children_list = []
	for i in range(children_quantity):
		child_dict = {}
		child_dict['first_name'] = input('Имя ребенка: ')
		child_dict['age'] = int(input('Возраст ребенка: '))
		children_list.append(child_dict)
	empl_dict['children'] = children_list
	return empl_dict

if __name__ == '__main__':
	add_employee()

