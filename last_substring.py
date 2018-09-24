def lastsubstring(str):
	if len(str) == 0:	return str
	largest = max([c for c in str])
	ret = ""
	for ind, val in enumerate(str):
		if largest == val:
			ret = max(str[ind:], ret)
	return ret

print lastsubstring("ggaggggg")