print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip = int (input("What percentage tip would you like to give?\n"))
people = int (input("How many people are going to split the bill?\n"))
tips = bill*(tip/100)
bill_final = tips + bill
per_person = bill_final / people
print (f"Each person should pay: ${round(per_person,2)}")
