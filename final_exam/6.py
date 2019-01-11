

univerities_i_wish_to_attend = ['German', 'Japan', 'France']

# University I cannot attend
university_i_cannot_attend = "German"

# Remove university I cannot attend
univerities_i_wish_to_attend.remove(university_i_cannot_attend)

# Create new university
new_university = "US"

# Add new university to my list
univerities_i_wish_to_attend.append(new_university)
# For Loop
for country in univerities_i_wish_to_attend:

	# Create message
	message = f"I wish to go visiting {country} next semester."

	# Print message
	print(message)