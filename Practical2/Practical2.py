from tools import*

#Open up the california text file by using open function.
#and read the file, then close
textfile = open("california.txt", "r")
new_1 = textfile.readlines()
textfile.close()

# set up the new empty dictionaries
california = {}
percent = {}
texas = {}

# To count the total number of villains, we have set each variables to 0
Godzilla = 0
The_Joker = 0
Voldemort = 0
Cthulu = 0
Dr_Doom = 0

# count and add the total of each villians
for i in new_1:
    name, value = i.strip().split("\t")
    california[name] = value
    if name == "Godzilla":
        Godzilla += int(value)
    elif name == "The Joker":
        The_Joker += int(value)
    elif name == "Voldemort":
        Voldemort += int(value)
    elif name == "Cthulu":
        Cthulu += int(value)
    elif name == "Dr. Doom":
        Dr_Doom += int(value)

california["Godzilla"] = Godzilla
california["The Joker"] = The_Joker
california["Voldemort"] = Voldemort
california["Cthulu"] = Cthulu
california["Dr. Doom"] = Dr_Doom

#Set up the total value to figure out the each villain's percentage by dividing into total.

total = Godzilla + The_Joker + Voldemort + Cthulu +  Dr_Doom

g_percent = (california.get("Godzilla")/total)*int(100)
j_percent = (california.get("Godzilla")/total)*int(100)
v_percent = (california.get("Godzilla")/total)*int(100)
c_percent = (california.get("Godzilla")/total)*int(100)
d_percent = (california.get("Godzilla")/total)*int(100)

percentage["Godzilla"] = GP
percentage["The Joker"] = JP
percentage["Voldemort"] = VP
percentage["Cthulu"] = CP
percentage["Dr. Doom"] = DP

cali = list(california.items())

sorted_cali = [cali.pop()]

#sort
while cali:
    present = cali.pop()
    for elem in range(len(sorted_cali)):
        if int(present[1]) > int(sorted_cali[elem][1]):
            sorted_cali.insert(elem, present)
            present = ""
            break
    if present:
        sorted_cali.append(present)
for entry in sorted_cali:
    print(entry)


#Open up the california text file by using open function.
#and read the file, then close
#same step as california. txt

textfile = open("texas.txt", "r")
new_2 = textfile.readlines()
textfile.close()


for i in new_2:
    name, value = i.strip().split("\t")
    texas[name] = value
    if name == "Godzilla":
        Godzilla += int(value)
    elif name == "The Joker":
        The_Joker += int(value)
    elif name == "Voldemort":
        Voldemort += int(value)
    elif name == "Cthulu":
        Cthulu += int(value)
    elif name == "Dr. Doom":
        Dr_Doom += int(value)

texas["Godzilla"] = Godzilla
texas["The Joker"] = The_Joker
texas["Voldemort"] = Voldemort
texas["Cthulu"] = Cthulu
texas["Dr. Doom"] = Dr_Doom

total = Godzilla + The_Joker + Voldemort + Cthulu +  Dr_Doom

g_percent = (texas.get("Godzilla")/total)*int(100)
j_percent = (texas.get("Godzilla")/total)*int(100)
v_percent = (texas.get("Godzilla")/total)*int(100)
c_percent = (texas.get("Godzilla")/total)*int(100)
d_percent = (texas.get("Godzilla")/total)*int(100)


#sort texas.txt file
texas = list(texas.items())

sorted_texas = [texas.pop()]

while texas:
    current = texas.pop()
    for value in range(len(sorted_texas)):
        if int(current[1]) > int(sorted_texas[value][1]):
            sorted_texas.insert(value, current)
            current = ""
            break
    if current:
        sorted_texas.append(current)
for entrance in sorted_texas:
    print(entrance)

#using while function to loop every inputs by if/elif statement.
while True:
    state = input("Which state's totals would you like to compute? (or STOP) ")
    if state.lower() == "california":
        print("The candidates earned this many votes: ")
        table_print(("Name", "Votes"), sorted_cali, 15)
##        print("The break down by percent: ")
##        table-print(("Name", "Percentage"), percent, 15)
    elif state.lower() == "texas":
        print("The candidates earned this many votes: ")
        table_print(("Name", "Votes"), sorted_texas, 15)
    elif state.upper() == "STOP":
        break





