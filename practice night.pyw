#BANQUET FACILITY

NumPeople = input("How many people will attend the party")
PeopleTable = 10
NumFullTable = NumPeople/PeopleTable
ExtraPeople = NumPeople%PeopleTable
NumFullTable = (NumPeople/PeopleTable)

if NumPeople <= 10:
print "There is/are ", NumFullTable, "full tables"
print ExtraPeople, " people will need to be squeezed in" 
