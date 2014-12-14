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
            if aassignment[1]=='VBP' or assignment[1]=='VBD':
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
       