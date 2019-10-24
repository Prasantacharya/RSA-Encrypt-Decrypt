n = 4

def proc(n):
	if n == 0:
		return 2
	var = proc(n-1)
	return var * var


print(proc(n))
