db_list = []

def read_db(path: str) -> list:
	global db_list
	with open(path, 'r', encoding='UTF-8') as file:
		my_list = file.readlines()
		for line in my_list:
			id_dict = dict()
			line = line.strip().split(",")
			id_dict['lastname'] = line[0]
			id_dict['firstname'] = line[1]
			id_dict['phone'] = line[2]
			id_dict['comment'] = line[3]
			db_list.append(id_dict)



def get_new_contact(contact: dict) -> str:
	s = '\n'
	for i in contact.values():
		s += i + ','
	return s[:-1]



def write_file(new_contact):
	print(f'Вы ввели >: {new_contact}')
	print("Нажмите 1, чтобы записать контакт, или нажмите любую клавишу, чтобы выйти >:")
	save = input()
	if save == "1":
		print("Контакт записан.")
		with open('database.txt', 'a+', encoding='UTF-8') as file:
			file.write(new_contact)
	else:
		print('Завершение программы')
		exit()

def change_contact():
	with open ('database.txt', 'r', encoding='UTF-8') as f:
		old_data = f.read()

	new_data = old_data.replace('что_меняем', 'на_что_меняем')

	with open ('database.txt', 'w', encoding='UTF-8') as f:
		f.write(new_data)


