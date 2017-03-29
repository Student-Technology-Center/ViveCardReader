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
			if (row[1] == "admin"):
				print("Admin found.")
				return True
		return False
	except Exception as e:
		print(e.args)
		print(e)

def allow_access(ID):
	try:
		input_file = open("user_list.csv", "a") 	
		writer = csv.writer(input_file)
		writer.writerow( (ID, "student") )
	except Exception as e:
		print(e.args)
		print(e)

def main(argv):
	card_input = input("Reading card now..\n")
	print("Passing in input.. " + card_input)
	if (check_admin(extract_wnumber(card_input))):
		new_user = input("Please enter new user info\n")
		allow_access(extract_wnumber(new_user))

if __name__ == "__main__":
	main(sys.argv)