drink = float(input("How much did your drink cost"))
appetizer = float(input("How much did your appetizer cost"))
entree = float(input("How much did your entree cost"))
dessert= float(input("How much does the dessert cost"))
tip= int(input("What percentage do you tip? (Dont type the %)"))
cost=drink+appetizer+entree+dessert
total=cost+tip*0.01
print(f"The total cost of your delicious good meal was {total}$")