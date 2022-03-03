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
    # for i in range(len(inviteSet)):
        # print(str(1) +  ". " + sorted(inviteSet)[i])
    return sorted(inviteSet)

def findAllPlayerStats(filename, winnerList):
    winner_map = {}
    for item in winnerList:
        winner_map[item] = []
    Catan_Notes = open(filename, "r") 
    for line in Catan_Notes:
        item = line.split("-")
        name = item[0].split(" ")[1].strip()
        if name in winner_map.keys():
            line = line.strip().split(".")
            line[0] = "("+ line[0] + ")"
            line = " ".join(line)
            winner_map[name].append(line.strip())
    return winner_map

def printPlayerStats (winner_map,name):
    return(winner_map[name])
    




if __name__ == "__main__":
    winnerListCalculated = inviteCalc("Winners_Log.md")
    allPlayerStats = findAllPlayerStats("Winners_Log.md", winnerListCalculated)
    for k in sorted(allPlayerStats.keys()):
        print("## " + k)
        print("Game notes are: (Game #, winner, date, notes) \n")
        playerstats = (printPlayerStats(allPlayerStats,k))
        for item in playerstats:
            print (item, "\n")
        print("\n")


