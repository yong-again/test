# 29.4
def mul(**args):
	m = 1
	for i in args:
		m *= i
	return m


# FLATTEN
def flatten(ls):
    result = []
    for item in ls:
        if type(item) == list:
            result += flatten(item)
        else:
            result += [item]
    return result