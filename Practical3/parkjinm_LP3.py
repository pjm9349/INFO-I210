#Justin Park

#Section 1

#Created Place class
class Place(object):
    name = []

    
# A Place has a name and a location
# a Place has either been visited(True) or not(False)
    def __str__(self):
        reply = self.__name
        if self.__location:
            reply += ", located in " + self.__location.get_name() + " "

        if self.__visited == True:
            reply += "(visited)."
        else:
            reply += "(not visited)."
        return reply

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

# SECTION 2

#Using static method, and locations()
    @staticmethod
    def locations():
        if Place.name:
            print("The following locations exist:")
            for locations in Place.name:
                print(locations)
        else:
            print("No locations exist at this time.")
            print("")

    def __init__(self, name, location = None):
        self.__name = name
        self.__location = location
        self.__visited = False
        Place.name.append(self)
        print(self.__name, "created")

    def visit(self):
        if self.__visited:
            print(self.__name + " has already been visited")
        else:
            print("You visit " + self.__name + ".")
            self.__visited = True
            if self.__location:
                print("That means...", end = "")
                self.__location.visit()
        

# SECTION 3

#Add two child classes which are "Home" and "City"
class Home(Place):
    def __init__(self, name, location = None, bedrooms = 0, occupancy = 0):
        super().__init__(name, location)
        self.__bedrooms = bedrooms
        self.__occupancy = occupancy

    def __str__(self):
        reply = super().__str__() + "\n"
        reply += "        This house has" + " " + str(self.__bedrooms) + " " + "bedrooms"
        reply += ", of which" + " " + str(self.__occupancy) + " " + "are occupied."
        return reply

class City(Place):
    def __init__(self, name, location = None, populations = 0, mayor = ""):
        super().__init__(name, location)
        self.__populations = populations
        self.__mayor = mayor

    def __str__(self):
        reply = super().__str__() + "\n"
        reply += "        This city has" + " " + str(self.__populations) + " " + "residents"
        reply += " and the mayor is " + self.__mayor
        return reply



# Main for SECTION 2 & 3
##Place.locations()
##indiana = Place("Indiana")
##indy = City("Indianapolis", indiana, 853173, "Joeseph Hogsett")
##btown = City("Bloomington", indiana, 80405, "John Hamilton")
##iu = Place("IU Campus", btown)
##library = Place("Wells Library", iu)
##rental = Home("Rental House", btown, 5, 4)
##historic = Home("Elias Abel House", btown, 4, 0)
##
##Place.locations()
##
##print()
##print(iu)
##print(library)


# Main for SECTION 4 - Visitation

##indiana = Place("Indiana")
##indy = City("Indianapolis", indiana, 853173, "Joeseph Hogsett")
##btown = City("Bloomington", indiana, 80405, "John Hamilton")
##iu = Place("IU Campus", btown)
##library = Place("Wells Library", iu)
##rental = Home("Rental House", btown, 5, 4)
##historic = Home("Elias Abel House", btown, 4, 0)
##
##print()
##library.visit()
##indiana.visit()


# Main
Place.locations()
indiana = Place("Indiana")
indy = City("Indianapolis", indiana, 853173, "Joeseph Hogsett")
btown = City("Bloomington", indiana, 80405, "John Hamilton")
iu = Place("IU Campus", btown)
library = Place("Wells Library", iu)
rental = Home("Rental House", btown, 5, 4)
historic = Home("Elias Abel House", btown, 4, 0)

Place.locations()

print()
library.visit()
indiana.visit()


# BONUS
##print("\nTrue or False, Rental House is located in Indiana:", end = ' ')
##print(rental.is_located_in(indiana), "\n")
##
##print("True or False, Elias Abel House is located in Indianapolis:", end = ' ')
##print(historic.is_located_in(indy), "\n")
    
            
    
