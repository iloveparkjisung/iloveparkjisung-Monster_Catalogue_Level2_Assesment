#this is our dictionary where the information the user wants to know, remove, add, find are in.
catalogue = {
    "Stoneling" : { #dictionary inside a dictionary to store more values so we could put in different keys.
        "Strength" : 7,
        "Speed" : 1,
        "Stealth" : 25,
        "Cunning" : 15
    } , 
    "Vexcream" : {
        "Strength" : 1,
        "Speed" : 6,
        "Stealth" : 21,
        "Cunning" : 19
    } , 
    "Dawnmirage" : {
        "Strength" : 5,
        "Speed" : 15,
        "Stealth" : 18,
        "Cunning" : 22
    } ,
    "Blazegolem" : {
        "Strength" : 15,
        "Speed" : 20,
        "Stealth" : 23,
        "Cunning" : 6
    } ,
    "Websnake" : {
        "Strength" : 7,
        "Speed" : 15,
        "Stealth" : 10,
        "Cunning" : 5
    } , 
    "Moldvine" : {
        "Strength" : 21,
        "Speed" : 18,
        "Stealth" : 14,
        "Cunning" : 5
    } , 
    "Vortexwing" : {
        "Strength" : 19,
        "Speed" : 13,
        "Stealth" : 19,
        "Cunning" : 2
    } , 
    "Rotthing" : {
        "Strength" : 16,
        "Speed" : 7,
        "Stealth" : 4,
        "Cunning" : 12
    } , 
    "Froststep" : {
        "Strength" : 14,
        "Speed" : 14,
        "Stealth" : 17,
        "Cunning" : 4
    } , 
    "Wispghoul" : {
        "Strength" : 17,
        "Speed" : 19,
        "Stealth" : 3,
        "Cunning" : 2
    } 
}


def main_catalogue(): #this will be our main interface where we can navigate and locate what we want to see
    print ("=== NEOZONE: THE Monster Game Catalogue ===") #the welcoming message the user is receiving
    while True:
        print("\nWelcome to NEOZONE: THE Monster Game Catalogue\n What would you like to do today?\n\n== Input the number to navigate ==") #this is the user's instruction
        print("1 : View available NEOZONE monsters and stats!!\n2 : Look up a specific NEOZONE monsters\n3 : Make your own monster and stats\n4 : Delete a NEOZONE monster\n5 : QUIT ") #the options the user can input
        choice = input("Enter your choice: ")
        if choice == '1': #if the user chooses 1 - 4 it will do the fuctions which has specific tasks assigned using the def function.
            view_monsters()
        elif choice == '2':
            search_catalogue()
        elif choice == '3':
            make_monster()
        elif choice == '4':
            delete_monster()
        elif choice == '5':
            print("Thank you for using NEOZONE: THE Monster Game Catalogue") 
            break #using break quits the code
        else:
            print("That's not right. Please input the right numbers, Try Again.") #this makes sure that the user does not input an invalid option
        

def view_monsters(): #this shows us what is currently inside the dictionary
    print("Here are the existing NEOZONE monster's names with stats and are available to be viewed.")
    for monster_name, stats in catalogue.items(): #this would grab the information (name and stats)
        print(f"\n\n{monster_name}'s Stats:") #while this would print it
        for stats, stats_number in stats.items(): #this would print the stats
            print(f"{stats}: {stats_number}") 


def search_catalogue(): #in this def functions the user can search up certain monsters and see their stats
    print("Here are the existing NEOZONE monster's names with stats and are available to be viewed.\n Which NEOZONE monster would you like to look at?\n")
    for name in catalogue:
        print(name) #prints out the names of available monsters the user can search for
#this asks the user what type of NEOZONE minster they would like to see and capitalizes it so the program can figure out what to find
    ask =  input("\nWhich monster would you like to look at today? ").capitalize()  
    if ask in catalogue:
        print(f"\n{ask}'s Stats:") 
        for stats, stats_number in catalogue[ask].items():#this prints the stats of th emonster the monster the user asked for
            print(f"{stats} : {stats_number}")
    else:
        print("Combo not found") #value error

def make_monster():#this function helps the user search up their desired monster
    print("\nCreate new NEOZONE monsters and customize their stats!")
    name = input("Enter the name of the NEOZONE monster: ").capitalize()
    if not name:
        print("Monster name cannot be blank!!")
        return
    if name in catalogue: #we use these two so that the suer cannot enter an invalid monster!
        print(f"A NEOZONE monster named '{name}' already exists in the catalogue!")
        return
    items = {} # we use an empty dictionary so we can put new things into it
    for stat_name in ["Strength", "Speed", "Stealth", "Cunning"]:
            try: 
                stat_num = input(f"Choose a value for {stat_name}! (Please enter a number between 1 - 25) : ")
                if stat_num is None:
                    print("User entered a blank space. Monster creation canceled.\nReturning to the menu", "ERROR")
                    return
                try:
                    stat_num = float(stat_num)
                    items[stat_name] = stat_num
                finally:
                    if stat_num > 25:
                        print("Please enter a number between 1 - 25!\nCanceling monster creation, returning to Main Menu.")
                        return
                items[stat_name] = stat_num
                break
            except ValueError:
                print("Invalid stat number. Please enter a numeric value")
            catalogue [name] = items
            print(f"New NEOZONE monster '{name} added.")

    


def delete_monster():
    print("Delete a NEOZONE m")
    name = input("Enter the name of the NEOZONE monster you would want to delete: ").capitalize()
    if name in catalogue:
        del catalogue[name]
        print(f"NEOZONE monster '{name}' was deleted.")
    else:
        print("NEOZONE monster not found.")


main_catalogue()