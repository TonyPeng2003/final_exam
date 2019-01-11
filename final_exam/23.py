 


favorite_food = ['Harrry Potter', 'Year 93', 'Holes'

# Make copy of favorite food
friend_food = favorite_food[:]

# Add a new food item to the original list
favorite_food.append("Ways")



# Add a different food to the list friend_food.
friend_food.append("Get Jobs")


# Print the message, “My favorite types of food are:" 
# “ and use a for-loop to print the first list. 
print("My favorite books are:")
for food_item in favorite_food:
	print(f"\t{food_item}")


# Print the message, my friend’s favorite types of food are:
# and then use a for loop to print the second list.

print("My friend's favorite books are:")
for food_item in friend_food:
	print(f"\t{food_item}")

# Make Sure Vegetable Soup in favorite_food, but not in friend_food
print("Ways" in favorite_food)
print("Ways" not in friend_food)


# Make Sure Vegetable Soup in favorite_food, but not in friend_food
print("Get Jobs" in friend_food)
print("Get Jobs" not in favorite_food)