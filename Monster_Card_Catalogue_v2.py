import easygui as eg
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
    while True:
        choice = eg.buttonbox(
            "=== NEOZONE: THE Monster Game Catalogue ===\nWhat would you like to do today?\n\nChoose one of the options to navigate!",#the welcoming message the user is receiving
            title = "THE Burger Shop",
            choices = ["Look at all the monsters >-<!", "Search for a MONSTER?! rawr :3", "Create the Monster of your dreams :O", "Delete a Monster :<", "Exit"]
        )
        if choice == 'Look at all the monsters >-<!': #if the user chooses one of the options it will do the fuctions which has specific tasks assigned using the def function.
            view_monsters()
        elif choice == 'Search for a MONSTER?! rawr :3':
            search_catalogue()
        elif choice == 'Create the Monster of your dreams :O':
            make_monster()
        elif choice == 'Delete a Monster :<':
            delete_monster()
        elif choice == 'Exit':
            eg.msgbox("Thank you for using NEOZONE: THE Monster Game Catalogue") 
            break #using break quits the code
        


def view_monsters(): #this shows us what is currently inside the dictionary
    catalogue = "Existing NEOZONE monsters:"
    for monster_name, stats in catalogue.items(): #this would grab the information (name and stats)
        catalogue += f"\n\n{monster_name}'s Stats:" #while this would print it
        for stats, stats_number in stats.items(): #this would print the stats
            catalogue += f"{stats}: {stats_number}"
    eg.msgbox(catalogue, title="catalogue")




def search_catalogue(): #in this def functions the user can search up certain monsters and see their stats
    monster = eg.choicebox("View NEOZONE monster", "View monster", list(catalouge.keys())) 
#this asks the user what type of NEOZONE minster they would like to see and capitalizes it so the program can figure out what to find
    ask =  input("\nWhich monster would you like to look at today? ").capitalize()  
    if monster:
        monster_txt += f"\n{ask}'s Stats:"
        for stats, stats_number in catalogue[ask].items():#thsi prints the stats of th emonster the monster the user asked for
            monster_txt += f"{stats} : {stats_number}"
        eg.msgbox(monster_txt, title="NEOZONE monster details :")



def make_monster():
    print("Create new NEOZONE monsters and customize their stats!")
    name = input("Enter the name of the NEOZONE monster: ")
    items = {} # we use an empty dictionary so we can put new things into it
    for i in range (1,4):
        while True:
            try:
                stat = float(input(f"Choose a {stat} for " , name ,":"))
                break
            except ValueError:
                print("Invalid stat number. Please enter a numeric value")
        items[name] = stat
    catalogue [name] = items
    print(f"New NEOZONE monster '{name} added.")



def delete_monster():
    name = eg.choicebox("Choose the NEOZONE monster you would want to delete: ", "Delete a NEOZONE monster" ,list(catalogue.keys()))
    if name in catalogue:
        del catalogue[name]
        eg.masbox(f"NEOZONE monster '{name}' was deleted.", "SUCCESS")

main_catalogue()