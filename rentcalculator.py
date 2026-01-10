rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
elcctricity_spend = int(input("Enter the total of electricitu spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the number of person living in room/flat = "))


total_bill = elcctricity_spend * charge_per_unit

output = (food + rent + total_bill)//person

print(output)