def recursive_binary_search(_list, target):
	if len(_list) == 0:
		return False

	midpoint = (len(_list)) // 2
	value = _list[midpoint]

	if value == target:
		return True

	if value < target:
		return recursive_binary_search(_list[midpoint+1:], target)
	else:
		return recursive_binary_search(_list[:midpoint], target)