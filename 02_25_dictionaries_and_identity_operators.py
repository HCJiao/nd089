elements = {
	"hydrogen":	1,
	"helium":	2,
	"carbon":	6
}
print(elements["helium"])	# print the value mapped to "helium"
print(elements)	

elements['lithium'] = 3	# insert "lithium" with a value of 3 into the dictionary
print(elements)	

print("carbon" in elements)
print(elements.get("dilithium"))

n = elements.get("dilithium")
print(n is None)
print(n is not None)

print('mithril' in elements)