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
    print ("=== NEOZONE: THE Monster Game Catalogue ===\n") #the welcoming message the user is receiving
    while True:
        print("Welcome to NEOZONE: THE Monster Game Catalogue\n What would you like to do today?\n\n== Input the number to navigate ==") #this is the user's instruction
        print("1 : View available NEOZONE monsters and stats!!\n2 : Look up a specific NEOZONE monsters\n3 : Make your own monster and stats\n4 : Delete a NEOZONE monster\n5 : QUIT ") #the options the user can input
        choice = input("Enter your choice: ")
        if choice == '1':
            view_monsters()
        elif choice == '2':
            search_catalogue()
        elif choice == '3':
            make_monster()
        elif choice == '4':
            delete_monster()
        elif choice = '5':
            print("Thank you for using NEOZONE: THE Monster Game Catalogue")
            break
        else:
            print("That's not right. Please input the right numbers, Try Again.")
        

def view_monsters():

def search_catalogue():

def make_monster():

def delete_monster():
