num=float(input('1st number: '))
op=input('+,-,x,/: ')
num2=float(input('2nd number: '))
total=float(0)

if op == '+':
	total=num + num2
elif op == '-':
	total=num - num2
elif op == 'x':
	total=num * num2
elif op == '/': 
	total=num / num2

print (num,op,num2,"=",total)
