population = {
	"Shanghai":	17.8,
	"Istanbul":	13.3,
	"Karachi":	13.0,
	"Mumbai":	12.5
}

print(population["Shanghai"])
# print(population["Sydney"]) # KeyError
print(population.get("Emerald City", "There's no such city!"))

a = [1,2,3]
b = a
c = [1,2,3]

print(a == b)	# True
print(a is b)	# True
print(a == c)	# True
print(a is c)	# False