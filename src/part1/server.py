currentlyUsedIp = []
retiredIp = []

nextIp = [0, 0, 0, 0]

# generates new ip
def generatesNewIP() -> str:
    pass


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
