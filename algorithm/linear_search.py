def linear_search(_list,target):
	for i in range(len(_list)):
		if _list[i] == target:
			return i

	return None