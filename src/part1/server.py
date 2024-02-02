currentlyUsedIp = []
retiredIp = []

nextIp = [0, 0, 0, 0]

# generates new ip
def generatesNewIP() -> str:
    ipToReturn = f"{nextIp[3]}.{nextIp[2]}.{nextIp[1]}.{nextIp[0]}"
<<<<<<< HEAD
<<<<<<< HEAD
    nextIp[0]+= 1
=======

>>>>>>> main
=======
    nextIp[0]+= 1
>>>>>>> a9d3afcee907c556ccdf2207c69e2327f977ab17
    i = 0
    while i < 4:
        if nextIp[i] == 255:
            nextIp[i] = 0
            nextIp[i+1] += 1
        i += 1
    
    return ipToReturn


# removes given ip from active list
<<<<<<< HEAD
<<<<<<< HEAD
def retireIp(ip: str):
    try:
        currentlyUsedIp.remove(ip)
        retiredIp.append(ip)
        return 1
    except(ValueError): 
        return None

# checks recently used list when we need a new ip # will return "-1" if list is empty
def reuseIp() -> str:
    if len(retiredIp) > 0:
        return retiredIp.pop(0)
    else:
        return None
=======
def retireIp(ip: str, activeList: List[str], retiredList: List[str]) -> int:
=======
def retireIp(ip: str):
>>>>>>> a9d3afcee907c556ccdf2207c69e2327f977ab17
    try:
        currentlyUsedIp.remove(ip)
        retiredIp.append(ip)
        return 1
    except(ValueError): 
        return None

# checks recently used list when we need a new ip # will return "-1" if list is empty
def reuseIp() -> str:
    if len(retiredIp) > 0:
        return retiredIp.pop(0)
    else:
<<<<<<< HEAD
        return "-1"
>>>>>>> main
=======
        return None
>>>>>>> a9d3afcee907c556ccdf2207c69e2327f977ab17



# figures out if a new ip needs to be generated or if one can be reused
def getNewIp():
<<<<<<< HEAD
<<<<<<< HEAD
    tempIp = reuseIp()
    if(tempIp != None):
=======
    tempIp = reuseIp(retiredIp)
    if(tempIp != "-1"):
>>>>>>> main
=======
    tempIp = reuseIp()
    if(tempIp != None):
>>>>>>> a9d3afcee907c556ccdf2207c69e2327f977ab17
        return tempIp
    else:
        return generatesNewIP()

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a9d3afcee907c556ccdf2207c69e2327f977ab17

def getIpStatus(ipAddr):
    pass

if __name__ == '__main__':
    # Command : requiresIp, callout
    commandOpts = {
            "ASK" : (False, getNewIp),
            "RENEW" : (True, reuseIp),
            "RELEASE" : (True, retireIp),
            "STATUS" : (True, getIpStatus)
            }
    while True:
        commandIn = input("Please input a command:").strip().split()

        if len(commandIn) < 1:
            print("No command entered.")
            continue

        commandName = commandIn[0].upper()

        if not commandName in commandOpts:
            print("Illegal command entered.")
            continue

        commandOpt = commandOpts[commandIn[0].upper()]

        requiresIp, callout = commandOpt
        if (requiresIp and (len(commandIn) != 2)) \
                or (not requiresIp and (len(commandIn) != 1)):
            print("Illegal command arguments.")
            continue

        if requiresIp:
            # Check that Ip is valid
            if len([x for x in commandIn[1].split('.') if (len(x) <= 3) \
                    and x.isnumeric() and (0 <= int(x) <= 255)]) != 4:
                print("Invalid Ip address, should be from 0.0.0.0 to 255.255.255.255")
                continue

            # Error checking lets leading/trailing '.' through.
            ret = callout(commandIn[1].strip('.'))
            if ret == None:
                print("Command failed.")
                continue
            print(ret)
        else:
            ret = callout()
            if ret == None:
                print("Command failed.")
                continue
            print(ret)
<<<<<<< HEAD
=======
#test code
>>>>>>> main
=======
>>>>>>> a9d3afcee907c556ccdf2207c69e2327f977ab17
