

age = 29
name = "Kalu"
friends = ['Tony', 'Lisa', 'Hali', 'Sara']

# test with lower()
if "Tony".lower().title() in friends:
	print("Hi Tony!")
else:
	print("I don't know Tony.")

if name == "Kalu" or "Lisa":
	print("Hi Kalu brothers")

if "Hali" and "Sara" in friends:
	print("Hi Hali and Sara")

if "Agbai" not in friends:
	print("Sorry, I do not know Agbai.")
