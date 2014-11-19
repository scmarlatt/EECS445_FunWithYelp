import re, sys, operator, json, io, math
from mrjob.protocol import JSONValueProtocol

STOP_WORD = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also','although','always','am','among', 'amongst', 'amoungst', 'amount',  'an', 'and', 'another', 'any','anyhow','anyone','anything','anyway', 'anywhere', 'are', 'around', 'as',  'at', 'back','be','became', 'because','become','becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom','but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven','else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own','part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'the']

def classifier(words):
	funny = float(1)/3
	cool = float(1)/3
	useful = float(1)/3 
	total_all = 0
	total_votes = 0
	tfunny = 0
	tcool = 0
	tuseful = 0
	for word in words.split():
		#print word
		if word in database:
			votes = database[word]
			funny_p = float(votes[1])
			funny_np = float(votes[2])
			cool_p = float(votes[3])
			cool_np = float(votes[4])
			useful_p = float(votes[5])
			useful_np = float(votes[6])
			t_votes = (funny_p+funny_np+cool_p+cool_np+useful_p+useful_np)
			#print useful_p, useful_np
			#print t_votes
			likelihood_funny = funny_p/(funny_p+cool_p+useful_p)
			predictor_funny = 0.253590446793
			#print likelihood_funny, predictor_funny
			likelihood_cool = cool_p/(funny_p+cool_p+useful_p)
			predictor_cool = 0.303213323986
			#print likelihood_cool, predictor_cool
			likelihood_useful = useful_p/(funny_p+cool_p+useful_p)
			predictor_useful = 0.443196229221
			#print likelihood_useful, predictor_useful
			total_votes += (funny_p+cool_p+useful_p)
			total_all += (funny_p+funny_np+cool_p+cool_np+useful_p+useful_np)
			funny = funny*float(likelihood_funny)/predictor_funny
			cool = cool*float(likelihood_cool)/predictor_cool
			useful = useful*float(likelihood_useful)/predictor_useful
			tcool += cool_p
			tuseful += useful_p
			tfunny += funny_p
			#print useful
	prior = float(total_votes)/(total_all+1)
	funny = funny*prior
	cool = cool*prior
	useful = useful*prior	
	return [funny, cool, useful, tfunny, tcool, tuseful]


f = io.open('review_votes.txt', 'r',encoding='utf-16')
database = {}
for line in f:
	data = str(line)
	data = data.replace("[","")
	data = data.replace("]","")
	data = data.replace('"',"")
	data = data.replace(",","")
	data_clean = data.split()
	database[data_clean[0]] = data_clean[1:]
# a = sorted(database.iteritems(), key=operator.itemgetter(1), reverse=True)
# print a[:50]
f.close()

f2 = open('reviews_sample.json','r')
total_f = 0
total_c = 0
total_u = 0
for line in f2:
	review = json.loads(line)
	text = json.dumps(review['text']).replace('"',"")
	text.replace("'","")
	text = text.lower()
	output = classifier(text)
	total_f += output[3]
	total_c += output[4]
	total_u += output[5]
	votes = json.dumps(review['votes'])
	print votes, output
print float(total_f)/(total_f+total_u+total_c)
print float(total_c)/(total_f+total_u+total_c)
print float(total_u)/(total_f+total_u+total_c)
f2.close()




