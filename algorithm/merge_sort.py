def split(_list):
	midpoint = len(_list) // 2
	return [_list[:midpoint],_list[midpoint:]]

def merge(left, right):
	l = []
	i = 0
	k = 0

	while i < len(left) and k < len(right):
		if left[i] < right[k]:
			l.append(left[i])
			i += 1
		else:
			l.append(right[k])
			k += 1

	while i < len(left):
		l.append(left[i])
		i += 1

	while k < len(right):
		l.append(right[k])
		k += 1

	return l

def merge_sort(_list):
	if len(_list) <= 1:
		return _list

	left_half,right_half = split(_list)
	
	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left,right)