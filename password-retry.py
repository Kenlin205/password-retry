times = 3
password = "333"
while times > 0 :
	password = input("Please enter a password ")
	if password == "333":
		#print("You got the answer")
		break
	elif password != "333":
		print("The opportiany have",times )
		times = times - 1
	print("You have no opportiany")



