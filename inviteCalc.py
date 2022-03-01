def inviteCalc(filename):
    Catan_Notes = open(filename, "r") 
    inviteSet = set()
    for line in Catan_Notes:
        line = line.split(" ")
        inviteSet.add(line[1].strip())
    toRemove = "Samira, Ephrem, Jackson, JBCapone, Josiah, Liz, Tamasha, Bonnie, Karen, Nick, Reid"
    toRemove = toRemove.split(",")
    for item in toRemove: 
        inviteSet.remove(item.strip())
    for i in range(len(inviteSet)):
        print(str(1) +  ". " + sorted(inviteSet)[i])
if __name__ == "__main__":
    inviteCalc("Winners_Log.md")

