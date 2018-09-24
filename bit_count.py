def bitcount(arr):
	pairs = []
	for num in arr:
		count = bin(num)[2:].count("1")
		pairs.append((num, count))
	pairs = sorted(pairs, key = lambda x: [x[1], x[0]])
	return [p[0] for p in pairs]
print bitcount([3,2,4,5,3])