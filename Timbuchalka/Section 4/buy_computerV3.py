available_parts = ["computer",
				   "monitor",
				   "keyboard",
				   "mouse",
				   "mouse mat",
				   "hdmi cable",
				   "dvd drive"
				   ]
valid_choices = [str(i) for i in range(1 , len (available_parts)+1)]
print (valid_choices) 
current_choice = "-"
computer_parts = list()  # create an empty list

while current_choice != '0':
	if current_choice in "123456":
		print("Adding {}".format(current_choice))
		if current_choice == '1':
			computer_parts.append("computer")
		elif current_choice == '2':
			computer_parts.append("monitor")
		elif current_choice == '3':
			computer_parts.append("keyboard")
		elif current_choice == '4':
			computer_parts.append("mouse")
		elif current_choice == '5':
			computer_parts.append("mouse mat")
		elif current_choice == '6':
			computer_parts.append("hdmi cable")
	else:
		print("Please add options from the list below:")
		for part in available_parts:
			print(f"{available_parts.index(part)+1}: {part}")

	current_choice = input()

print(computer_parts)