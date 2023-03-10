def foo(string):
	l = 0
	r = len(string) - 1
	
	while r >= l:
		if not string[l] == string[r]:
			return False
		l += 1
		r -= 1
	return True
print(foo(input())) 
