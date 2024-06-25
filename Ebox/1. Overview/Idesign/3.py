brandingEx = int(input("Enter branding expenses\n"))
travelEx = int(input("Enter travel  expenses\n"))
foodEx = int(input("Enter food expenses\n"))
logisticEx = int(input("Enter logistics expenses\n"))

totalexpenses = brandingEx + travelEx + foodEx + logisticEx
brandpercent = (brandingEx/totalexpenses)*100
travelpercent = (travelEx /totalexpenses)*100
foodpercent = (foodEx/totalexpenses)*100
logisticpercent = (logisticEx/totalexpenses)*100

print (f"Total expenses : Rs.{totalexpenses:.2f}")
print (f"Branding expenses percentage : {brandpercent:.2f}%")
print (f"Travel expenses percentage : {travelpercent:.2f}%")
print (f"Food expenses percentage : {foodpercent:.2f}%")
print (f"Logistics expenses percentage :  {logisticpercent:.2f}%")