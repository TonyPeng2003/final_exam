univerities_i_wish_to_attend = ['German', 'Japan', 'France']

# University I cannot attend
university_i_cannot_attend = "German"

# Remove university I cannot attend
univerities_i_wish_to_attend.remove(university_i_cannot_attend)

# Create new university
new_university = "US"

# Add new university to my list
univerities_i_wish_to_attend.append(new_university)


# Using insert to add Tsinghua University at beginning
univerities_i_wish_to_attend.insert(0, "Englang")






# Get number of univerities
total_universities = len(univerities_i_wish_to_attend)

# Use for loop to remove all but last two universities
for i in range(total_universities - 2):
	popped = univerities_i_wish_to_attend.pop()
	print(f"Sorry, I cannot visit {popped}.")
		


# Tell remaining schools I still wish to attend
for remaining_school in univerities_i_wish_to_attend:
	message = f"Dear {remaining_school}, I still wish to visit your country."
	print(message)

# Removing last two univerisities
del univerities_i_wish_to_attend[0]
del univerities_i_wish_to_attend[0]

# Printing my now empty list
print(univerities_i_wish_to_attend)
		