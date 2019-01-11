# 31. Write a program that converts a list of gpas to the appropriate 
# percentage scale. Then convert the following list 
# [1.3, 3.4, 3.9, 3.3, 2.8, 2.2, 3.7] into the appropriate percentage grade. 
# You should output the gpas in the same order.

gpas = ["B+"]
new_list = []

for gpa in gpas:
	if gpa == "A+":
		grade = '4.O'
	elif gpa =="A" :
		grade = "4.0"
	elif gpa =="A-" :
		grade = "3.7"
	elif gpa =="B+":
		grade = "3.0"
	elif gpa =="B":
		grade = "2.7"
	elif gpa =="B-":
		grade = "2.3"
	elif gpa== "C+":
		grade = "2.0"
	elif gpa =="C":
		grade = "1.7"
	elif gpa =="C-":
		grade = "1.3"
	elif gpa =="D":
		grade = "1.0"
	elif gpa == "E" or "F":
		grade = "0.0"
	else:
		raise Exception(f"There was a problem with {gpa}")
	new_list.append(grade)


print(new_list)
