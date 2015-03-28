x=True
y=False
count=1
while count==1:
	oprat=int(input(print(''' which operatin would you like to perform
		press-2 for x and y
		press-3 for x or y
		press-4 for x not
		press-5 for y not
		'''
		)))

	if oprat <2 and oprat >5:
		print("enter valid choice")
	elif oprat==2:
		print("x and y=",x and y)
	elif oprat==3:
		print("x or y=",x or y)
	elif oprat==4:
		print("x not= ",not x)
	else :
		print("y not=",not y)
	count=int(input("if you want to continoue press-1 else press-0"))