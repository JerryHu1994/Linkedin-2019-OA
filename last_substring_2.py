import string
import random
import sys

def lastsubstring(string):
	"""compute the last substring"""
	if not string: return string
	max_char = max(char for char in string)
	d = {idx: idx for idx, char in enumerate(string) if char == max_char}
	starts = set(d.keys())
	res = ""
	n = len(string)
	while d:
		char = max(string[idx] for idx in d.values())
		res += char
		removes = set()
		for start, end in d.items():
			if string[end] != char or end == n - 1:
				removes.add(start)
			else:
				d[start] += 1
				if d[start] in starts:
					starts.remove(d[start])
					removes.add(d[start])
		for key in removes:
			if key in d:
				d.pop(key)
	return res


def naive_lastsubstring(string):
	if not string: return string
	return max(string[idx:] for idx in range(len(string)))


def generate_string(n):
	"""generate a random string with length n"""
	return ''.join(random.choices(string.ascii_lowercase, k = n))


def test(ntimes):
	string = generate_string(10)
	try:
		assert(lastsubstring(string) == naive_lastsubstring(string))
	except:
		print("Input {} failed".format(string))
		sys.exit(1)
	print("Passed {} tests".format(ntimes))


if __name__ == "__main__":
	test(10000)