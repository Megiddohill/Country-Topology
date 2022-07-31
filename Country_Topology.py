# David Prato CIS 276 Country Dictionary
#Menu---------------------------------#

def display():
    print("Command Menu\n")
    print("1: View countries")
    print("2: Add a country")
    print("3: Delete a country")
    print("4: Exit")
    print()

# List Function -----------------------------------#

def display_keys(countries):
    keys = list(countries.keys()) #this lists all the keys in our dictionary to the variable "keys"
    keys.sort() #sorts them in aslphabetical order
    keys_input = "Country Code: " 
    for key in keys:
        keys_input += key + " " #So here, it will make an iteration check and add keys to the end of the string
    print(keys_input) #ie "Country Code: MT NZ UK US"

# View Function ------------------------------------#
def view(countries):
    display_keys(countries) #Calls the previous function to ask the user what key they are looking for
    key = input("Enter Country Code: ")
    key = key.upper()
    if key in countries: #checking to see if the key is in our dictionary
        cName = countries[key] #displays the name if it does
        print(f'Country name: {cName}.\n')
    else:
        print("There is no country correlating with that key.\n")#if it doesn't


# Add Function -------------------------------------#

def add(countries):
    key = input("Enter country key: ")
    key = key.upper()
    if key in countries: #Here we are checking to see if the key in question is already in our dictionary
        cName = countries[key]
        print(f"{cName} is already using this key.\n")
    else:
        cName = input("Enter country name: ")
        cName = cName.title() #nifty little function that makes the first letter of a word capitalized in a string (after each white space)
        countries[key] = cName
        print(f"{cName} was added.\n")


# Delete Function ----------------------------------#

def delete(countries):
    key = input("Enter country code: ")
    key = key.upper() # obviously this is to make all charcters upper case for simplicity and readbalitly
    if key in countries: #Again checking if its there
        cName = countries.pop(key) #this will delete the country associated with that key
        print(f'{cName} is now deleted.\n')
    else:
        print("There is no country asscoiated with that key")


# Main Program ----------------------------------------#





def main():
    countries = {"UK": "United Kingdom",
                 "US": "United States",
                 "NZ": "New Zealand",
                 "MT": "Malta"} #This is how you create an intitial dictionary
    command = None
 
    
    display()

    while True: #"While True" is used to make a while loop operate until the given boolean condition becomes false
        try:
            command = int(input("Enter your choice number: \n"))
        except ValueError:
            print("Invalid input. Try again") #Making sure the user inputs numbers
            continue
        
        if command == 1: 
            view(countries)
        elif command == 2:
            add(countries)
        elif command == 3:
            delete(countries)
        elif command == 4:
            print("Farewell, Thank you for using our service!")
            break
        else:
            print("Invalid input, try again: \n")

   

if __name__ == "__main__": #This is used to call a "main()" function
    main()
