from JsonParser import create_leaderboardtuple
from JsonParser import get_json
from JsonParser import get_members

#from Twitterer import leaderboard_tweet
import os
import time

def main():
    while(True):
	i = 0
	oldlist = []
	newlist = []
	oldmap  = {}
	newmap  = {}
	leaderboardtuple = get_json()
	if i == 0:
		oldlist = leaderboardtuple[1]
		oldmap  = leaderboardtuple[0]
	else:
		newlist = leaderboardtuple[1]
		newmap  = leaderboardtuple[0]

		inboth = list(set(oldlist) & set(newlist))
		inold_notinnew = list(set(oldlist) - list(newlist))
		innew_notinold = list(set(newlist) - list(oldlist))
		changes = []
		for i in inboth:
			if oldmap[i][0] != newmap[i][0] or oldmap[i][1] != newmap[i][1]:
				changes.append(i,newmap[i])
		oldlist = newlist
		oldmap  = newmap
	++i
	sleep(900)


if __name__ == "__main__":
    main()
