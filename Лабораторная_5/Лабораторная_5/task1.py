from pprint import pprint
a = 16
pprint([{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(a)])
