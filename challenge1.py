#!/usr/bin/env python
# coding=utf-8

def q1():
    print 'Question 1: Generate 2-dimension arrays'
    x,y=input('Please input 2 digits with comma: \n')
    print('>>> ')
    lists = [[] for i in range(x)]
    for i in range(x):
        for j in range(y):
          lists[i].append(i*j)
    print lists
    print

def q2():
    print 'Question 2: Removing duplicate words and alphaumatical sorting'
    words = raw_input('Enter sequence of words seperated by whitespace:\n').split(' ')
    print('>>> ')
    words_set = set(words)
    print ' '.join(sorted(words_set))
    print

def q3():
    print 'Question 3: Upper and lower letter counter'
    letters = raw_input('Enter a sentence of words with upper and lower case letters:\n')
    print('>>> ')
    import string
    upper=len(filter(lambda x: x in string.uppercase, letters))
    lower=len(filter(lambda x: x in string.lowercase, letters))
    print ("UPPER CASE %d"%upper)
    print ("LOWER CASE %d"%lower)

if __name__ == "__main__":
    q1()
    q2()
    q3()
    print 'Challenge 1 Finished!'
