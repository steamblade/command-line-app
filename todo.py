import sys
import datetime

if len(sys.argv) == 1 :
	ab=str("Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics")
	print(ab)
elif len(sys.argv) == 2 :
	a=str(sys.argv[1])
	if a == "help":
		print("""Usage :-
$ ./todo add \"todo item\"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")
	elif a == "ls":
		l1=open("todo.txt",'a')		
		l=open("todo.txt",'r')
		r1=l.readlines()
		l1.close()		
		r2=len(r1)
		if r2>0:		
			for i in range(1,r2+1):
				r3=r1.index(r1[-i])			
				print("["+str(r3+1)+"]"+" ",end='')			
				for j in r1[-i]:
					if j=="\n":
						continue
					else:
						print(j,end='')
				print()
		else:
			print("There are no pending todos!")	
	elif a == "report":
		x1=open("todo.txt","r")
		x2=open("done.txt","r")
		x3=x1.readlines()
		x4=len(x3)
		x5=x2.readlines()
		x6=len(x5)
		x1.close()
		x2.close()		
		comp=x6
		pend=x4
		now=datetime.datetime.now()
		cy=now.year
		cm=now.month
		cd=now.day
		print(str(cy)+"-"+str(cm)+"-"+str(cd)+" Pending : "+str(pend)+" Completed : "+str(comp))
	elif a=="add":
		print("Error: Missing todo string. Nothing added!")	
	
	elif a=="del":
		print("Error: Missing NUMBER for deleting todo.")
	elif a=="done":
		print("Error: Missing NUMBER for marking todo as done.")	
	else:
		print("Error: Invalid input")


elif len(sys.argv) == 3 :
	a=str(sys.argv[1])
	if a == "add":	
		b=sys.argv[2]	
		t1=open("todo.txt","a")
		t1.write(b+"\n")		
		t1.close()
		print("Added todo: "+'"'+str(b)+'"')
	elif a=="del":
		b1=int(sys.argv[2])
		b6=open("todo.txt","r")		
		b2=b6.readlines()
		b3=len(b2)
		b4=int(b1-1)
		if 0<=b4<b3:
			b2.pop(b4)
			print("Deleted todo #"+str(b1))
			b6.close()
			b5=open("todo.txt","w")
			b5.writelines(b2)
			b5.close()
		else:
			print("Error: todo #"+str(b1)+" does not exist. Nothing deleted.")
			b6.close()
	elif a=="done":
		z1=int(sys.argv[2])
		z6=open("todo.txt","r")		
		z2=z6.readlines()
		z3=len(z2)
		z4=int(z1-1)
		if 0<=z4<z3:
			z7=z2.pop(z4)
			print("Marked todo #"+str(z1)+" as done.")
			z6.close()
			z5=open("todo.txt","w")
			z5.writelines(z2)
			z5.close()
			z8=open("done.txt","a")
			z8.write(z7)
			z8.close()
		else:
			print("Error: todo #"+str(z1)+" does not exist.")
			z6.close()
		
	else:
		print("Error: Invalid input")




