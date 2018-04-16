def example1():
	name = 'Jim'
	student = name
	name = 'Tim'

	print(name)
	print(student)

def example2():
	scores = ["B", "C", "A", "D", "B", "A"]
	grades = scores
	print("scores: " + str(scores))
	print("grades: " + str(grades))
	scores[3] = "B"
	print("scores: " + str(scores))
	print("grades: " + str(grades))

def example3():
	example3_number_list = [3,1,4,1,5,9,2,6,5,3]
	example3_string_list = ["the","big","red","dog","was","the","sad","dad"]
	print("len(number_list):", len(example3_number_list))
	print("min(number_list):", min(example3_number_list))
	print("max(number_list):", max(example3_number_list))
	print("sorted(number_list):", sorted(example3_number_list))
	print("sorted(number_list, reverse=True):", sorted(example3_number_list, reverse=True))

	print("len(number_list):", len(example3_string_list))
	print("min(number_list):", min(example3_string_list))
	print("max(number_list):", max(example3_string_list))
	print("sorted(number_list):", sorted(example3_string_list))
	print("sorted(number_list, reverse=True):", sorted(example3_string_list, reverse=True))

def example4():
	nautical_directions = "\n".join(["fore","aft","starboard","port"])
	print(nautical_directions)

	names = ["García","O'Kelly","Davis"]
	print("-".join(names))

	# stuff = ["thing", 42, "nope"]
	# print(" and ".join(stuff))

	python_varieties = [
		'Burmese Python',
		'African Rock Python',
		'Ball Python',
		'Reticulated Python',
		'Angolan Python'
	]
	python_varieties.append('Blood Python')
	print(python_varieties)

example1()
example2()
example3()
example4()