# Import needed modules
import os              # for clearing the screen and other OS level commands
import requests        # for communicating via API
import json            # for handling JSON
import getpass         # provides a password input without revealing text


# Login process
def login():
    print()
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
    print("Token: " + token)


# Our Main Menu
def mainmenu():
    print()
    print("[1] Add a mouthpiece")
    print("[2] List my mouthpieces")
    print("[3] Delete a mouthpiece")
    print("-----------------------")
    print("[7] Log in")
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
    newmfr = str(input("Manufacturer: "))
    print()
    newmodel = str(input("Model: "))
    mpctypemenu()
    newtype = str(input("Mouthpiece type: "))
    mpcfinishmenu()
    newfinish = str(input("Finish: "))
    print()
    input("Press Enter to send to Knack...")
    api_url = "https://api.knack.com/v1/objects/object_4/records"
    mouthpiece = {"field_17": newmfr, "field_24": newtype, "field_16": newmodel, "field_26": newfinish}
    headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
    response = requests.post(api_url, data=json.dumps(mouthpiece), headers=headers)
    print(response.json())
    print(response.status_code)


# List mouthpieces process
def listmpcs():
    api_url = "https://api.knack.com/v1/objects/object_4/records"
    headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
    response = requests.get(api_url, headers=headers)
    jresponse = response.json()
    print(json.dumps(jresponse, indent=4, sort_keys=True))


# Delete mouthpiece process
def delmpc():
    delid = input("Enter ID of mouthpiece to delete: ")
    api_url = "https://api.knack.com/v1/objects/object_4/records/" + delid
    headers = {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
    response = requests.delete(api_url, headers=headers)
    print(response.json())
    print(response.status_code)


# Add user process
# NOTE: Adding the connected Mouthpiecer in field_40 does not yet work. We may need to retrieve the ID of the new account and then add that value with an additional call.
def addusr():
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
os.system('clear')
bannerfile = open('banner.txt', 'r')
banner = bannerfile.read()
print(banner)
print("A Python-based command line interface to the Mouthpiecer Knack DB")
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
    elif option == 7:
        print()
        login()
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

print()
print("You've exited to shell")
