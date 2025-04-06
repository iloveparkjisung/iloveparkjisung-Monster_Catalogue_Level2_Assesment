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
        eg.buttonbox(
            "=== NEOZONE: THE Monster Game Catalogue ===\nWhat would you like to do today?\n\nChoose one of the options to navigate!",#the welcoming message the user is receiving
            title = "THE Burger Shop",
            choices = ["Look at all the monsters >-<!", "Search for a MONSTER?! rawr :3", "Create the Monster of your dreams :O", "Delete a Monster :<", "Exit"]
        )
        if choices == 'Look at all the monsters >-<!': #if the user chooses one of the options it will do the fuctions which has specific tasks assigned using the def function.
            view_monsters()
        elif choices == 'Search for a MONSTER?! rawr :3':
            search_catalogue()
        elif choices == 'Create the Monster of your dreams :O':
            make_monster()
        elif choices == 'Delete a Monster :<':
            delete_monster()
        elif choices == 'Exit':
            eg.msgbox("Thank you for using NEOZONE: THE Monster Game Catalogue") 
            break #using break quits the code
        

def view_monsters(): #this shows us what is currently inside the dictionary
    catalouge_text = "Existing NEOZONE monsters:"
    for monster_name, stats in catalogue.items(): #this would grab the information (name and stats)
        catalouge_text += f"\n\n{monster_name}'s Stats:" #while this would print it
        for stats, stats_number in stats.items(): #this would print the stats
            catalouge_text += f"{stats}: {stats_number}"
    eg.msgbox(catalouge_text, title="Catalouge")





main_catalogue()