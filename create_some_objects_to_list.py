from create_one_attribute import Person

#Create an object named "p1" whose name is "Anvar"
#Create an object named "p2" whose name is "Shavkat"
#Create an object named "p3" whose name is "Jasur"

#Add these objects to the "persons" named list
p1=Person("Anvar")
p2=Person("Shavkat")
p3=Person("Jasur")
persons=[]
persons.append(p1.name)
persons.append(p2.name)
persons.append(p3.name)
print(persons)