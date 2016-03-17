import nltk
import codecs
from collections import defaultdict

file_object = open('ebitda_tech_crunch_preprocessed.txt', 'r')
data = file_object.read()
file_object.close()

sentences = nltk.sent_tokenize(data.lower())


prob_eb_eb = defaultdict(int)
for sent in sentences:
	prob_eb_eb[sent.count('ebitda')] += 1
print prob_eb_eb


def probability_0(sentences, check, treshold=0):
	prob = 0
	for sent in sentences:
		if ('ebitda' in sent) and sum([sent.count(i) for i in check])>treshold:
			prob += 1
	prob = float(prob) / len(sentences)
	return prob

def probability_1(sentences, check, treshold=1):
	prob = 0
	for sent in sentences:
		if ('ebitda' in sent) and sum([sent.count(i) for i in check])==treshold:
			prob += 1
	prob = float(prob) / len(sentences)
	return prob

def probability_2(sentences, check1, check2, treshold1=0, treshold2=0):
	prob = 0
	for sent in sentences:
		if ('ebitda' in sent) and sum([1 for i in check1 if sent.find(i)!=-1])>treshold1 and sum([sent.find(i) for i in check2 if sent.find(i)!=-1])>treshold2:
			prob += 1
	prob = float(prob) / len(sentences)
	return prob

def probability_3(sentences, check1, check2, treshold1=1, treshold2=1):
	prob = 0
	for sent in sentences:
		if ('ebitda' in sent) and sum([sent.count(i) for i in check1])==treshold1 and sum([sent.count(i) for i in check2])==treshold2:
			prob += 1
	prob = float(prob) / len(sentences)
	return prob



money = ['dollar', 'euro', 'pound', 'rur', 'million', 'billion']
money_ = ['dollar', 'euro', 'pound', 'rur']
year = ['year'] + [str(i) for i in range(2000,2017)]
year_ = [str(i) for i in range(2000,2017)]
percent = ['percent']



p = probability_0(sentences, money)
print 'p(money >= 1|eb) = ', p

p = probability_0(sentences, year)
print 'p(year >= 1|eb) = ', p

p = probability_0(sentences, percent)
print 'p(percent >= 1|eb) = ', p



p = probability_1(sentences, money_)
print 'p(money = 1|eb) = ', p

p = probability_1(sentences, year_)
print 'p(year = 1|eb) = ', p

p = probability_1(sentences, percent)
print 'p(percent = 1|eb) = ', p



p = probability_2(sentences, money, year)
print 'p(money >= 1, year >= 1|eb) = ', p


p = probability_3(sentences, money_, year_)
print 'p(money = 1, year = 1|eb) = ', p
