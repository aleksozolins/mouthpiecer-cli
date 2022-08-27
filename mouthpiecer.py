# Import needed modules
import os                         # for clearing the screen and other OS level commands
import requests                   # for communicating via API
import json                       # for handling JSON
import getpass                    # provides a password input without revealing text
import pandas as pd               # for tabulating JSON
from termcolor import colored     # colored output in the terminal

# declare some vars
token = ""
bannerfile = open('banner.txt', 'r')
banner = bannerfile.read()
mpcselect = 0


# Uesful code
# selection = int(input("Select a mouthpiece by number: "))
# dfs = df.iloc[selection]['id']
# print(dfs)
# input("Press Enter to continue...")


# Login process
def login():
    global token
    global logemail
    if token != "":
        input("Please log out first. Press Enter...")
    else:
        print("Please log in...")
        print()
        logemail = input("Email: ")
        passwd = getpass.getpass("Password: ")
        api_url = "https://api.knack.com/v1/applications/60241522a16be4001b611249/session"
        creds = {"email": logemail, "password": passwd}
        headers = {"content-type":"application/json", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
        response = requests.post(api_url, data=json.dumps(creds), headers=headers)
        jresponse = response.json()
        token = jresponse['session']['user']['token']
        print()
        input("You have been logged in. Press Enter...")


# Logout process
def logout():
    global token
    if token == "":
        input("You aren't currently logged in. Press Enter...")
    else:
        input("You will be logged out. Press Enter...")
        token = ""


# Our Main Menu
def mainmenu():
    os.system('clear')
    if token == "":
        print()
        print("You are not currently logged in...")
        print(colored(banner, 'yellow'))
        print("[1] My Mouthpieces")
        print("-----------------------")
        print(colored("[6] ", 'green') + ("Log in"))
        print("[7] Log out")
        print(colored("[8] ", 'green') + ("Add a user"))
        print("-----------------------")
        print(colored("[0] ", 'green') + ("Exit to shell"))
        print()
    else:
        print()
        print("You are logged in as " + logemail)
        print(colored(banner, 'yellow'))
        print(colored("[1] ", 'green') + ("My Mouthpieces"))
        print("-----------------------")
        print("[6] Log in")
        print(colored("[7] ", 'green') + ("Log out"))
        print(colored("[8] ", 'green') + ("Add a user"))
        print("-----------------------")
        print(colored("[0] ", 'green') + ("Exit to shell"))
        print()


# My Mouthpieces Menu
def mympcsmenu():
    global mpcselect
    os.system('clear')
    print()
    print(colored(banner, 'yellow'))
    print("--- Mouthpieces for " + logemail + " ---")
    print()
    if mpcselect == 0:
        print(colored("[1] ", 'green') + ("Add mouthpiece               ") + (colored("[3] ", 'green') + ("Edit mouthpiece")))
        print(colored("[2] ", 'green') + ("Delete mouthpiece            ") + (colored("[0] ", 'green') + ("Back to main menu")))
        print("------------------------------------------------------")
        print()
    if mpcselect == 1:
        print("[1] Add mouthpiece               [3] Edit mouthpiece")
        print("[2] Delete mouthpiece            [0] Back to main menu")
        print("------------------------------------------------------")
        print()


# Menu for selecting a mouthpiece type
def mpctypemenu():
    print()
    print("one-piece")
    print("two-piece")
    print("cup")
    print("rim")
    print()


# Menu for selecting a mouthpiece finish
def mpcfinishmenu():
    print()
    print("silver plated")
    print("gold plated")
    print("brass")
    print("nickel")
    print("stainless")
    print("bronze")
    print("plastic")
    print()


# Add mouthpiece process
def addmpc():
    newmfr = str(input("Manufacturer: "))
    print()
    newmodel = str(input("Model: "))
    mpctypemenu()
    newtype = str(input("Mouthpiece type: "))
    mpcfinishmenu()
    newfinish = str(input("Finish: "))
    print()
    input("Press Enter to send to Knack...")
    api_url = "https://api.knack.com/v1/pages/scene_18/views/view_18/records"
    mouthpiece = {"field_17": newmfr, "field_24": newtype, "field_16": newmodel, "field_26": newfinish}
    headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"knack", "Authorization":token}
    response = requests.post(api_url, data=json.dumps(mouthpiece), headers=headers)
    mympcs()
    # print(response.json())
    # print(response.status_code)


# My mouthpieces process
def mympcs():
    global df
    if token == "":
        input("Please log in first. Press Enter...")
    else:
        mympcsmenu()
        listmpcs()
        selection = int(input("Make a menu selection: "))
        if selection == 1:
            addmpc()
        elif selection == 2:
            delmpc()
        elif selection == 3:
            editmpc()
        elif selection == 0:
            mainmenu()
        else:
            print()
            input("Invalid option selected. Press Enter to continue...")
            mympcs()


# List mouthpieces process
def listmpcs():
    global mpcselect
    api_url = "https://api.knack.com/v1/pages/scene_18/views/view_18/records"
    headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"knack", "Authorization":token}
    response = requests.get(api_url, headers=headers)
    jresponse = response.json()
    pd.set_option('display.max_rows', None)
    df = pd.json_normalize(jresponse['records'])
    df['index1'] = df.index
    df.drop(df.columns[[2, 4, 6, 8]], axis=1, inplace=True)
    df.columns = ['id', 'Make', 'Model', 'Type', 'Finish', 'Index']
    df = df.reindex(columns=['Index', 'Make', 'Model', 'Type', 'Finish', 'id'])
    if mpcselect == 0:
        df2 = df.to_string(index=False)
        print(df2)
        print()
    elif mpcselect -- 1:
        df2 = colored(df.to_string(index=False), 'green')
        print(df2)
        print()


# Delete mouthpiece process
def delmpc():
    global mpcselect
    mpcselect = 1
    mympcsmenu()
    listmpcs()
    print("Make a menu selection: 2")
    print()
    selection = int(input("Select a mouthpiece by Index to delete: "))
    delid = df.iloc[selection]['id']
    api_url = "https://api.knack.com/v1/pages/scene_18/views/view_18/records/" + delid
    headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"knack", "Authorization":token}
    response = requests.delete(api_url, headers=headers)
    print()
    input("Mouthpiece deleted...")
    mympcs()


# Add user process
# NOTE: Adding the connected Mouthpiecer in field_40 does not yet work. We may need to retrieve the ID of the new account and then add that value with an additional call.
def addusr():
    if token != "":
        input("Please log out before adding a user. Press Enter...")
    else:
        newusrfname = str(input("First name: "))
        print()
        newusrlname = str(input("Last name: "))
        newusrfullname = newusrfname + "" + newusrlname
        print()
        newusremail = str(input("Email: "))
        print()
        newusrpasswd1 = getpass.getpass("Password: ")
        newusrpasswd2 = getpass.getpass("Confirm: ")
        if newusrpasswd1 != newusrpasswd2:
            print("Passwords do not match -- Process aborted...")
        else:
            input("Press Enter to send to Knack...")
            api_url = "https://api.knack.com/v1/objects/object_1/records"
            newusr = {"field_1": {"first": newusrfname, "last": newusrlname}, "field_2": newusremail, "field_3": newusrpasswd1, "field_4": "active", "field_5": "Mouthpiecer"}
            headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
            response = requests.post(api_url, data=json.dumps(newusr), headers=headers)
            print(response.json())
            print(response.status_code)


# Retrieve user process
def rusr():
    usrid = (input("Enter user ID:"))
    input("Press Enter to send to Knack...")
    api_url = "https://api.knack.com/v1/objects/object_1/records/" + usrid
    headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
    response = requests.get(api_url, headers=headers)
    print(response.json())
    print(response.status_code)


# Here's where the program runs
mainmenu()
option = int(input("Enter your choice: "))

while option != 0:
    if option == 1:
        print()
        mympcs()
    elif option == 6:
        print()
        login()
    elif option == 7:
        print()
        logout()
    elif option == 8:
        print()
        addusr()
    else:
        print()
        input("Invalid option selected. Press Enter to continue...")

    print()
    mainmenu()
    option = int(input("Enter your choice: "))

bannerfile.close()
print()
print("You've exited to shell")
