#this is our dictionary where the information the user wants to know, remove, add, find are in.
catalogue = {
    "Stoneling" : {
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
    for monster_name, stats in catalogue.items():
        print(f"\n\n{monster_name}'s Stats:")
        for stats, stats_number in stats.items():
            print(f"{stats}: {stats_number}") 




def search_catalogue():
    print("Here are the existing NEOZONE monster's names with stats and are available to be viewed.\n Which NEOZONE monster would you like to look at?\n")
    for name in catalogue:
        print(name) #prints out the names of available monsters the user can search for

    ask =  input("\nWhich monster would you like to look at today? ").capitalize() 
    if ask in catalogue:
        print(f"\n{ask}'s Stats:")
        for stats, stats_number in catalogue[ask].items():
            print(f"{stats} : {stats_number}")
    else:
        print("Combo not found")


def make_monster():
    print("hi")
def delete_monster():
    print("hi")

main_catalogue()