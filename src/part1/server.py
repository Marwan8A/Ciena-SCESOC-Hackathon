# generates new ip
def generatesNewIP() -> str:
    pass

# removes given ip from active list
def retireIp(ipAddr):
    pass
# checks recently used list when we need a new ip
def reuseIp(ipAddr):
    pass


# figures out if a new ip needs to be generated or if one can be reused
def getNewIp():
    pass

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
            if callout(commandIn[1].strip('.')) != -1:
                print("Command failed.")
        else:
            if callout() != -1:
                print("Command failed.")
