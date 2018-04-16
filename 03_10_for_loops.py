cities = [
	"new york city",
	"mountain view",
	"chicago",
	"los angeles"
]

capitalised_cities = []

print(cities)

for city in cities:
	print(city.title())

for city in cities:
	capitalised_cities.append(city.title())

print(list(range(4)))
print(list(range(2,6)))
print(list(range(1,10,2)))

for index in range(len(cities)):
	cities[index] = cities[index].title()
	print(cities)

for i in range(3):
	print("Hello!")
# print(capitalised_cities)
"""
for x in xrange(1,10):
	pass

while :
	pass
"""