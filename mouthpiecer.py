# Import needed modules
import os              # for clearing the screen and other OS level commands
import requests        # for communicating via API
import json            # for handling JSON
import getpass         # provides a password input without revealing text

# declare some vars
token = ""
bannerfile = open('banner.txt', 'r')
banner = bannerfile.read()


# Login process
def login():
    global token
    global logemail
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
    else:
        print()
        print("You are logged in as " + logemail)
    print(banner)
    print("[1] Add a mouthpiece")
    print("[2] List my mouthpieces")
    print("[3] Delete a mouthpiece")
    print("-----------------------")
    print("[6] Log in")
    print("[7] Log out")
    print("[8] Add a user")
    print("[9] Retrieve a user by ID")
    print("-----------------------")
    print("[0] Exit to shell")
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
    if token == "":
        input("Please log in first. Press Enter...")
    else:
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
        print(response.json())
        print(response.status_code)


# List mouthpieces process
def listmpcs():
    if token == "":
        input("Please log in first. Press Enter...")
    else:
        api_url = "https://api.knack.com/v1/pages/scene_18/views/view_18/records"
        headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"knack", "Authorization":token}
        response = requests.get(api_url, headers=headers)
        jresponse = response.json()
        print(json.dumps(jresponse, indent=4, sort_keys=True))
        input("Press Enter to continue...")


# Delete mouthpiece process
def delmpc():
    if token == "":
        input("Please log in first. Press Enter...")
    else:
        delid = input("Enter ID of mouthpiece to delete: ")
        api_url = "https://api.knack.com/v1/pages/scene_18/views/view_18/records/" + delid
        headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"knack", "Authorization":token}
        response = requests.delete(api_url, headers=headers)
        print(response.json())
        print(response.status_code)
        input("Press Enter to continue...")


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
        addmpc()
    elif option == 2:
        print()
        listmpcs()
    elif option == 3:
        print()
        delmpc()
    elif option == 6:
        print()
        login()
    elif option == 7:
        print()
        logout()
    elif option == 8:
        print()
        addusr()
    elif option == 9:
        print()
        rusr()
    else:
        print()
        print("Invalid option selected")

    print()
    mainmenu()
    option = int(input("Enter your choice: "))

bannerfile.close()
print()
print("You've exited to shell")
