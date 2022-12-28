from requests import patch, get
import os, time

class Stats:
    faliures = 0
    sniped = False

def checkInvite(invite):
    r = get(f'https://discord.com/api/v9/invites/{invite}').text
    if '"message": "Unknown Invite"' in r:
        return True
    elif '"code": "' in r:
        return False
    else:
        return "Error"

def snipe(server,token,vanity):
    x = patch(f'https://discord.com/api/v9/guilds/{server}/vanity-url',json={"code":vanity},headers={'authorization':token})
    if 'Invite code is either invalid or taken.' in x.text:
        Stats.faliures+=1
        print("Sleeping for 15 seconds...")
        time.sleep(15)
        prg()
    else:
        print("[+] Vanity Sniped")
        Stats.sniped = True
        return True

def tokenCheck(token):
    r = get('https://discord.com/api/v9/users/@me',headers={'authorization':token}).text
    if 'Unauthorized' in r:
        return False
    elif '"id": "' in r:
        return True
    else:
        return "Error"

while True:
    token = input("> Discord Token (Must have perms in the server): ")
    if tokenCheck(token):
        serverid = str(input("> Server ID: "))
        vanity = input("> Vanity: ")
        break
    else:
        print("Invalid token..")
def prg():
    while True:
        if not checkInvite(vanity):
            Stats.faliures+=1
            os.system(f'title Failed to snipe - {Stats.faliures} / Vanity Sniped - {Stats.sniped}')
        elif checkInvite(vanity):
            if snipe(serverid,token,vanity):
                break
    input()
prg()
