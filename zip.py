Identity = ("Surname", "FirstName", "LastName")
Names = ("Koppula", "Hari", "Teja")

zipped = zip(Identity, Names)

for a,b in zipped:
    print(a,b)