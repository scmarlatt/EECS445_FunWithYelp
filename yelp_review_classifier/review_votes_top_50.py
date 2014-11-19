import re, sys, operator, json, io, math
from mrjob.protocol import JSONValueProtocol
f = io.open('review_votes.txt', 'r',encoding='utf-16')
database = {}
for line in f:
	data = str(line)
	data = data.replace("[","")
	data = data.replace("]","")
	data = data.replace('"',"")
	data = data.replace(",","")
	data_clean = data.split()
	database[data_clean[0]] = int(data_clean[5])
count = 0
for w in sorted(database, key=database.get, reverse=True):
	if count > 50:
		break
	print w, database[w]
	count += 1
f.close()