import csv
import sys
import re

def extract_wnumber(ID):
	'''A function used to extract a WNumber from the mag strip'''

	#Regex used for extraction
	regex_pattern = "[W]\d{8,10}"
	return_value = re.search(regex_pattern, ID)
	
	#Checks if we found a string to extract
	if return_value:
		return return_value.group(0)
	else:
		print("Couldn't extract W number. We were given " + ID)


def check_admin(wnumber):
	try:
		input_file = open("user_list.csv", "rt") 	
		reader = csv.reader(input_file)
		for row in reader:
			if (row[0] == wnumber and row[1] == "admin"):
				print("Admin found.")
				return True
		return False
	except Exception as e:
		print(e.args)
		print(e)

def add_access(ID):
	try:
		input_file = open("user_list.csv", "a") 	
		writer = csv.writer(input_file)
		writer.writerow( (ID, "student") )
	except Exception as e:
		print(e.args)
		print(e)

def check_access(ID):
	try:
		input_file = open("user_list.csv", "rt") 	
		reader = csv.reader(input_file)
		for row in reader:
			if (row[0] == ID and (row[1] == "admin" or row[1] == "student")):
				print("Normally we would disengage the lock here.")
				print("Access granted.")
				break
	except Exception as e:
		print(e.args)
		print(e)

def main(argv):
	while(1):		
		card_input = input("Reading card now..\n")
		print("Passing in input.. " + card_input)
		w_number = extract_wnumber(card_input)
		if (check_admin(w_number)):
			new_user = input("Please enter new user info\n")
			new_w_number = extract_wnumber(new_user)
			add_access(new_w_number)
			check_access(new_w_number)
		else:
			check_access(w_number)

if __name__ == "__main__":
	main(sys.argv)