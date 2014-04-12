number1 = int(raw_input("First number "))
delimeter = raw_input("What delimeter? ")
number2 = int(raw_input("Second number "))

if delimeter == "+":
	number = number1 + number2
if delimeter == "-":
	number = number1 - number2
if delimeter == "*":
	number = number1 * number2	
if delimeter == "/"
	number = number1 / number2

print "Your answer is ", number