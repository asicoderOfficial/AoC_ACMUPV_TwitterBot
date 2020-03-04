#!/usr/bin/env python
# -*- coding: utf-8 -*-

beforemap = {"Víctor Dorado Javier": (3330, 47), "Mario Campos Mocholí": (3284, 48), "RodrigoLlanes": (2754, 39), "Pere Marco": (2541, 38)}
aftermap  = {"Víctor Dorado Javier": (3335, 47), "Mario Campos Mocholí": (3284, 48), "RodrigoLlanes": (2754, 39), "Asier": (1, 30)}

listbefore = ["Víctor Dorado Javier", "Mario Campos Mocholí", "RodrigoLlanes", "Pere Marco"]
listafter  = ["Víctor Dorado Javier", "Mario Campos Mocholí", "RodrigoLlanes", "Asier"]

inboth = list(set(listbefore) & set(listafter)) #still participating
inbeforenotinafter = list(set(listbefore) - set(listafter)) #contestants that left the contest
inafternotinbefore = list(set(listafter) - set(listbefore)) #new contestants

for i in inboth:
	if beforemap[i][0] == aftermap[i][0] and beforemap[i][1] == aftermap[i][1]:
		print(i + " equal")
	else:
		print(i + " different")

"""
listone = [[2, 3],[4, 3]]
listtwo = [[2, 4],[4, 3],[5, 100]]

listonetuple = [tuple(lst) for lst in listone]
listtwotuple = [tuple(lst) for lst in listtwo]
"""
#print(set(listonetuple).intersection(listtwotuple))