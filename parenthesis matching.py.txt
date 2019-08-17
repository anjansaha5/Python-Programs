a = '[((a+b)c-d]'

def parenthesis_checking(a)
	l = []
	for i in a
		if i in '([{'
			l.append(i)
		elif i in ')}]'
			if l == []
				print('1')
				return False
			else
				x = l.pop()
				if (i == ')' and x != '(') or (i == ']' and x != '[') or (i == '}' and x != '{')
					print('2')
					return False
	if l == []
		return True
	else
		print('3')
		return False

print(parenthesis_checking(a))


