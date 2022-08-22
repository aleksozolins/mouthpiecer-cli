def mainmenu():
    print("[1] Add a mouthpiece")
    print("[2] Delete a mouthpiece")
    print("[0] Exit to shell")


def mpctypemenu():
    print()
    print("One Piece")
    print("Underpart")
    print("Two Piece")
    print("Rim")
    print("Cup (No Shank)")
    print("Shank Only")


def mpcfinishmenu():
    print()
    print("Silver Plated")
    print("Gold Plated")
    print("Brass (Bare)")
    print("Nickel (Bare)")
    print("Stainless Steel")


def addmpc():
    newmfr = str(input("Manufacturer: "))
    mpctypemenu()
    newtype = str(input("Mouthpiece type: "))
    print()
    newmodel = str(input("Model: "))
    print()
    mpcfinishmenu()
    newfinish = str(input("Finish: "))
    print()
    input("Press Enter to send to Knack...")
    import requests
    import json
    api_url = "https://api.knack.com/v1/objects/object_4/records"
    mouthpiece = {"field_17": newmfr, "field_24": newtype, "field_16": newmodel, "field_26": newfinish}
    headers =  {"content-type":"application/json", "X-Knack-Application-Id":"60241522a16be4001b611249", "X-Knack-REST-API-KEY":"82d8170b-0661-4462-8dbb-3a589abdfc39"}
    response = requests.post(api_url, data=json.dumps(mouthpiece), headers=headers)
    print(response.json())
    print(response.status_code)


mainmenu()
option = int(input("Enter your choice: "))

while option != 0:
    if option == 1:
        print()
        addmpc()
    elif option == 2:
        print()
        print("Delete a mouthpiece selected")
    else:
        print()
        print("Invalid option selected")

    print()
    mainmenu()
    option = int(input("Enter your choice: "))

print()
print("You've exited to shell")
