import nltk
import nltk.classify
import sys
import operator

def write_verbs(reviews):
    f1 = open('POS/verb_list1.txt', 'w')
    f2 = open('POS/verb_list2.txt', 'w')
    f3 = open('POS/verb_list3.txt', 'w')
    f4 = open('POS/verb_list4.txt', 'w')
    f5 = open('POS/verb_list5.txt', 'w')

    for review in reviews[1]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='VBP' or assignment[1]=='VBD':
                f1.write(assignment[0] + ' ')

    for review in reviews[2]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='VBP' or assignment[1]=='VBD':
                f2.write(assignment[0] + ' ')

    for review in reviews[3]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='VBP' or assignment[1]=='VBD':
                f3.write(assignment[0] + ' ')

    for review in reviews[4]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='VBP' or assignment[1]=='VBD':
                f4.write(assignment[0] + ' ')

    for review in reviews[5]:
        try:
            pos_assign = nltk.pos_tag(review)
        except:
            continue
        for assignment in pos_assign:
            if assignment[1]=='VBP' or assignment[1]=='VBD':
                f5.write(assignment[0] + ' ')

def get_mc_vb(infile1, infile2, infile3, infile4, infile5, num_words):
    # reviews[1] is a list of 1 star reviews...
    # Number of reviews to process
    texts = {}
    with open (infile1) as myfile:
        texts[1] = myfile.read().replace('\n', ' ').split()
    with open (infile2) as myfile:
        texts[2] = myfile.read().replace('\n', ' ').split()
    with open (infile3) as myfile:
        texts[3] = myfile.read().replace('\n', ' ').split()
    with open (infile4) as myfile:
        texts[4] = myfile.read().replace('\n', ' ').split()
    with open (infile5) as myfile:
        texts[5] = myfile.read().replace('\n', ' ').split()
    fdists = {}
    for i in [1,2,3,4,5]:
        fdists[i] = nltk.FreqDist(texts[i])
    
    most_common_words_lists = {}
    for i in [1,2,3,4,5]:
        most_common_words_lists[i] = [word[0] for word in fdists[i].most_common(num_words)]

    return most_common_words_lists