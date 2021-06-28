def binary_search(_list,target):
	first = 0
	last = len(_list) - 1

	while first <= last:
		midpoint = (first + last) // 2
		value = _list[midpoint]

		if value == target:
			return midpoint

		if value < target:
			first = midpoint + 1
		else:
			last = midpoint - 1

	return None