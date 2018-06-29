from config import data_file
from check import import_data, save
import check

def is_playing(user_id,csv_file = data_file):
    for participant in import_data(csv_file):
        if str(participant[0]) == str(user_id):
            return True
    return False

def amount_of_players(csv_file = data_file):
    return len(import_data(csv_file))

def game_going_on(csv_file = data_file):
    if import_data(csv_file) == []:
        return False
    return True

def set(user_id,position,value,csv_file = data_file):
    old_table = import_data(csv_file)

    for user in old_table:
        if int(user[0]) == int(user_id):
            user[position] = value
            save(old_table,csv_file)
            return True
    raise NameError("User not found in database!")
