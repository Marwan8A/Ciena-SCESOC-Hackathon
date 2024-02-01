currentlyUsedIp = []
retiredIp = []

nextIp = [0, 0, 0, 0]

# generates new ip
def generatesNewIP() -> str:
    ipToReturn = f"{nextIp[3]}.{nextIp[2]}.{nextIp[1]}.{nextIp[0]}"

    i = 0
    while i < 4:
        if nextIp[i] == 255:
            nextIp[i] = 0
            nextIp[i+1] += 1
        i += 1
    
    return ipToReturn


# removes given ip from active list
def retireIp(ip: str, activeList: List[str], retiredList: List[str]) -> int:
    try:
        activeList.remove(ip)
        retiredList.append(ip)
        return 1
    except(ValueError): 
        return -1

# checks recently used list when we need a new ip # will return "-1" if list is empty
def reuseIp(unusedList) -> str:
    if len(unusedList) > 0:
        return unusedList.pop(0)
    else:
        return "-1"



# figures out if a new ip needs to be generated or if one can be reused
def getNewIp():
    tempIp = reuseIp(retiredIp)
    if(tempIp != "-1"):
        return tempIp
    else:
        return generatesNewIP()

#test code
