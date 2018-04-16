import math

def mean(numbers):
	return sum(numbers)/len(numbers)

def tiles_needed(area_l_w_tuples):
	return sum(tup[0] * tup[1] for tup in area_l_w_tuples)

def packs_needed(tiles_needed):
	return math.ceil(tiles_needed/6)

def tiles_remaining(packs, tiles):
	return packs*6 - tiles

# print(mean([23, 32, 64]))
print(tiles_needed([(9,7),(5,7)]))
tiles_needed = tiles_needed([(9,7),(5,7)])
packs_needed = packs_needed(tiles_needed)
tiles_remaining = tiles_remaining(packs_needed, tiles_needed)
print(tiles_remaining)