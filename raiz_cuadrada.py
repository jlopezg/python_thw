import match

x = 81

print(match.sqrt(x))

def raiz_cuadrada(n):

    x = 0
	
	while x * x <= n:
	    x += 0.1
		
	return x
	
print(raiz_cuadrada(x))
