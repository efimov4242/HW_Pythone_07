import model
import view

model.read_db('database.txt')


def input_handler(inp: int):
	match inp:
		case 1:
			view.show_all(model.db_list)
		case 2:
			model.read_db('database.txt')
			view.db_success(model.db_list)
		case 3:
			model.db_list.append(view.new_contact())
		case 4:
			new_contact = model.get_new_contact(view.new_contact())
			model.write_file(new_contact)
		case 5:
			model.change_contact()
		case 6:
			view.show_all(model.db_list)
		case 8:
			view.exit_program()


while True:
	user_inp = view.main_menu()
	input_handler(user_inp)