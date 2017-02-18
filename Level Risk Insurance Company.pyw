#RISK VALUE FOR POTENTIAL CUSTOMERS

#Type Of Business
Combustible = "Yes"
NotCombustible = "No"

#QUERY
TypeOfBus = raw_input("Type Yes for Combustible and No for Non-combustible:")
PropertyValue = input("What's your property value: ")

#LEVEL OF RISK

if TypeOfBus == Combustible and PropertyValue <500:
    print "risklevelis 3"
elif TypeOfBus == Combustible and PropertyValue > 500:
    print "risklevelis 4"
elif TypeOfBus == NotCombustible and PropertyValue <750:
    print "risklevelis 1"
elif TypeOfBus == NotCombustible and PropertyValue >750:
    print "risklevelis 2 "