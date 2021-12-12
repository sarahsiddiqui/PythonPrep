
#asks the user to input the information for the first city
city1 = input ("Please enter the first city: ") 
population1 = int (input ("Please enter the population: ")) 
workforce1 =  float (input ("Please enter the workforce: ")) 

#asks the user to input the information for the second city
city2 = input ("Please enter the second city: ") 
population2 = int (input ("Please enter the population: ")) 
workforce2 =  float (input ("Please enter the workforce: ")) 

#asks the user to input the information for the third city
city3 = input ("Please enter the third city: ")
population3 = int (input ("Please enter the population: "))
workforce3 =  float (input ("Please enter the workforce: ")) 

#displays the information in a table format
print ("\n%-20s\t\t%10s\t\t%10s" % ("City", "Population", "Workforce"))
print ("%-20s\t\t%8i\t\t%10.1f" % (city1, population1, workforce1))
print ("%-20s\t\t%8i\t\t%10.1f" % (city2, population2, workforce2))
print ("%-20s\t\t%8i\t\t%10.1f" % (city3, population3, workforce3))