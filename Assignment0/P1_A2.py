count=1
while (count==1):


	x=int(input("enter first number"))

	y=int(input("enter the seconnd number"))

	N=int(input(''' for additon press-0
		for substraction press-1
		for multiplication press-2
		for  division press-3
		for modulo press-4
		'''
		))

	if N==0:
	    print("ans is =",x+y)
	elif N==1 :
	    print("ans is =",x-y)
	elif N==2 :
	    print("ans is =",x*y)
	elif N==3 :
	    print("ans  is =",x/y)
	elif N==4:
	    print("ans is =",x%y)
	else :
	    print("Error: you have enter a wrong  number")

    count=input(print("Do you want to continue? (yes-1/no-0)"))