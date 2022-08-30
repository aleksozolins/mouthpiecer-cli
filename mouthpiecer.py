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
        if response.status_code == 200:
            token = jresponse['session']['user']['token']
            print()
            input("You have been logged in. Press Enter to continue...")
        else:
            print()
            input(colored("Invalid credentials. ", 'red') + "Press Enter to continue...")


# Login process for new users
def loginnewusr():
    global token
    api_url = "https://api.knack.com/v1/applications/60241522a16be4001b611249/session"
    creds = {"email": newusremail, "password": newusrpasswd1}
    headers = {"content-type":"application/json", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
    response = requests.post(api_url, data=json.dumps(creds), headers=headers)
    jresponse = response.json()
    token = jresponse['session']['user']['token']


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
        print("[1] My mouthpieces")
        print("-----------------------")
        print(colored("[6] ", 'green') + ("Log in"))
        print("[7] Log out")
        print(colored("[8] ", 'green') + ("Add a user"))
        print("-----------------------")
        print(colored("[0] ", 'green') + ("Exit to shell"))
        print()
    else:
        print()
        print("You are logged in as " + colored(logemail, 'blue'))
        print(colored(banner, 'yellow'))
        print(colored("[1] ", 'green') + ("My mouthpieces"))
        print("-----------------------")
        print("[6] Log in")
        print(colored("[7] ", 'green') + ("Log out"))
        print("[8] Add a user")
        print("-----------------------")
        print(colored("[0] ", 'green') + ("Exit to shell"))
        print()


# My Mouthpieces Menu
def mympcsmenu():
    global mpcselect
    os.system('clear')
    print()
    print("You are logged in as " + colored(logemail, 'blue'))
    print(colored(banner, 'yellow'))
    print("--- Mouthpieces for " + colored(logemail, 'blue') + " ---")
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
    print(colored("[1] ", 'green') + ("one-piece"))
    print(colored("[2] ", 'green') + ("two-piece"))
    print(colored("[3] ", 'green') + ("cup"))
    print(colored("[4] ", 'green') + ("rim"))
    print()


# Menu for selecting mouthpiece threads
def mpcthreadsmenu():
    print()
    print(colored("[1] ", 'green') + ("standard"))
    print(colored("[2] ", 'green') + ("metric"))
    print(colored("[3] ", 'green') + ("other"))
    print()


# Menu for selecting a mouthpiece finish
def mpcfinishmenu():
    print()
    print(colored("[1] ", 'green') + ("silver plated"))
    print(colored("[2] ", 'green') + ("gold plated"))
    print(colored("[3] ", 'green') + ("brass"))
    print(colored("[4] ", 'green') + ("nickel"))
    print(colored("[5] ", 'green') + ("stainless"))
    print(colored("[6] ", 'green') + ("bronze"))
    print(colored("[7] ", 'green') + ("plastic"))
    print()


# Add mouthpiece process
def addmpc():
    print()
    newmake = input("Make: ")
    print()
    newmodel = input("Model: ")
    mpctypemenu()
    while True:
        option = input("Mouthpiece type: ")
        try:
            option = (int(option))
            if option not in (1, 2, 3, 4):
                raise ValueError
        except:
            print(colored("Invalid Option", 'red'))
            print()
            continue
        break
    if option == 1:
        newtype = "one-piece"
    elif option == 2:
        newtype = "two-piece"
    elif option == 3:
        newtype = "cup"
    elif option == 4:
        newtype = "rim"
    newthreads = ""
    if newtype != "one-piece":
        mpcthreadsmenu()
        while True:
            option = input("Threads: ")
            try:
                if option not in ("1", "2", "3", ""):
                    raise ValueError
            except:
                print(colored("Invalid Option", 'red'))
                print()
                continue
            break
        if option == "1":
            newthreads = "standard"
        elif option == "2":
            newthreads = "metric"
        elif option == "3":
            newthreads = "other"
        elif option == "":
            newthreads = ""
    mpcfinishmenu()
    while True:
        option = input("Finish: ")
        try:
            option = (int(option))
            if option not in (1, 2, 3, 4, 5, 6, 7):
                raise ValueError
        except:
            print(colored("Invalid Option", 'red'))
            print()
            continue
        break
    if option == 1:
        newfinish = "silver plated"
    elif option == 2:
        newfinish = "gold plated"
    elif option == 3:
        newfinish = "brass"
    elif option == 4:
        newfinish = "nickel"
    elif option == 5:
        newfinish = "stainless"
    elif option == 6:
        newfinish = "bronze"
    elif option == 7:
        newfinish = "plastic"
    print()
    print("------------------------")
    print(("Make: ") + colored(newmake, 'green'))
    print(("Model: ") + colored(newmodel, 'green'))
    print(("Type: ") + colored(newtype, 'green'))
    print(("Threads: ") + colored(newthreads, 'green'))
    print(("Finish: ") + colored(newfinish, 'green'))
    print("------------------------")
    print()
    while True:
        conf = input("Send to Knack? " + colored("[y] [n]: ", 'green'))
        try:
            if conf not in ("y", "n"):
                raise ValueError
        except:
            print(colored("Invalid Option", 'red'))
            print()
            continue
        break
    if conf == "y":
        api_url = "https://api.knack.com/v1/pages/scene_18/views/view_18/records"
        mouthpiece = {"field_17": newmake, "field_24": newtype, "field_16": newmodel, "field_25": newthreads, "field_26": newfinish}
        headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"knack", "Authorization":token}
        response = requests.post(api_url, data=json.dumps(mouthpiece), headers=headers)
        print()
        if response.status_code == 200:
            input("Success! Press Enter to continue...")
            mympcs()
        else:
            input(colored("Error! There was a problem with your request. ", 'red') + ("Press Enter to continue..."))
            mympcs()
    else:
        mympcs()


# My mouthpieces process
def mympcs():
    global df
    if token == "":
        input("Please log in first. Press Enter...")
    else:
        mympcsmenu()
        listmpcs()
        while True:
            selection = input("Make a menu selection: ")
            try:
                selection = (int(selection))
                if selection not in (1, 2, 3, 0):
                    raise ValueError
            except:
                print(colored("Invalid Option", 'red'))
                print()
                continue
            break
        if selection == 1:
            addmpc()
        elif selection == 2:
            delmpc()
        elif selection == 3:
            editmpc()
        elif selection == 0:
            mainmenu()


# List mouthpieces process
def listmpcs():
    global df
    api_url = "https://api.knack.com/v1/pages/scene_18/views/view_18/records"
    headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"knack", "Authorization":token}
    response = requests.get(api_url, headers=headers)
    jresponse = response.json()
    pd.set_option('display.max_rows', None)
    df = pd.json_normalize(jresponse['records'])
    df['index1'] = df.index
    df.drop(df.columns[[2, 4, 6, 8, 10, 11, 12]], axis=1, inplace=True)
    df.columns = ['id', 'Make', 'Model', 'Type', 'Threads', 'Finish', 'Index']
    df = df.reindex(columns=['Index', 'Make', 'Model', 'Type', 'Threads', 'Finish', 'id'])
    if mpcselect == 0:
        df2 = df.to_string(index=False)
        print(df2)
        print()
    elif mpcselect == 1:
        df2 = colored(df.to_string(index=False), 'green')
        print(df2)
        print()


# Delete mouthpiece process
def delmpc():
    if len(df.index) == 1:
        print()
        input(colored("Add another mouthpiece to delete. ", 'red') + ("You need at least one in place. Press Enter to continue..."))
        mympcs()
    else:
        global mpcselect
        mpcselect = 1
        mympcsmenu()
        listmpcs()
        print("Make a menu selection: 2")
        print()
        while True:
            selection = input("Select a mouthpiece by Index to delete: ")
            try:
                selection = (int(selection))
                if selection not in (range(0, len(df.index))):
                    raise ValueError
            except:
                print(colored("Invalid Option", 'red'))
                print()
                continue
            break
        print()
        while True:
            conf = input(colored("Are you sure you want to delete this ", 'red') + (df.iloc[selection]['Make']) + (" ") + (df.iloc[selection]['Model']) + (" ") + colored("[y] [n]: ", 'green'))
            try:
                if conf not in ("y", "n"):
                    raise ValueError
            except:
                print(colored("Invalid Option", 'red'))
                print()
                continue
            break
        if conf == "y":
            delid = df.iloc[selection]['id']
            api_url = "https://api.knack.com/v1/pages/scene_18/views/view_18/records/" + delid
            headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"knack", "Authorization":token}
            response = requests.delete(api_url, headers=headers)
            print()
            if response.status_code == 200:
                input("Success! Press Enter to continue...")
                mpcselect = 0
                mympcs()
            else:
                input(colored("Error! There was a problem with your request. ", 'red') + ("Press Enter to continue..."))
                mpcselect = 0
                mympcs()
        else:
            mpcselect = 0
            mympcs()


# Edit mouthpiece process
def editmpc():
    print()
    input("Not yet! Press Enter to continue...")
    mympcs()


# Add user process
# NOTE: Adding the connected Mouthpiecer in field_40 does not yet work. We may need to retrieve the ID of the new account and then add that value with an additional call.
def addusr():
    global newusremail
    global newusrpasswd1
    global logemail
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
            print()
            input(colored("Passwords do not match. ", 'red') + ("Process aborted. Press Enter to continue..."))
        else:
            logemail = newusremail
            print()
            input("Press Enter to send to Knack...")
            api_url = "https://api.knack.com/v1/objects/object_1/records"
            newusr = {"field_1": {"first": newusrfname, "last": newusrlname}, "field_2": newusremail, "field_3": newusrpasswd1, "field_4": "active", "field_5": "Mouthpiecer"}
            headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
            response = requests.post(api_url, data=json.dumps(newusr), headers=headers)
            if response.status_code == 200:
                loginnewusr()
                print()
                input("Success! You have been added and logged in. Let's add your first mouthpiece. Press Enter to continue...")
                addmpc()
            else:
                print()
                input(colored("Error! There was a problem with your request. ", 'red') + ("Press Enter to continue..."))
                mainmenu()


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
option = input("Enter your choice: ")

while option != "0":
    if option == "1":
        print()
        mympcs()
    elif option == "6":
        print()
        login()
    elif option == "7":
        print()
        logout()
    elif option == "8":
        print()
        addusr()
    else:
        print()
        input(colored("Invalid option selected. ", 'red') + ("Press Enter to continue..."))

    print()
    mainmenu()
    option = input("Enter your choice: ")

bannerfile.close()
print()
print("You've exited to shell")
print()
