#!/usr/bin/env python
# coding=utf-8
import urllib2
import random
import pickle

def pickle_file():
    file = urllib2.urlopen('http://52.25.91.45/misc_files/test.txt')
    html = file.read()
    sentences = html.split('\n\n')
    l = range(len(sentences))
    random.shuffle(l)
    pkl = {}
    for i in l:
        pkl[i] = sentences[l[i]]
    try:
        with open('test.pkl','wb') as f:
            pickle.dump(pkl, f)        
    except IOError, e:
            print "IOError: ",e
                    
    try:
        with open('test.pkl', 'rb') as f:
            s = pickle.load(f)
    except IOError, e:
            print 'IOError: ',e
    print s

if __name__ == "__main__":
    pickle_file()
