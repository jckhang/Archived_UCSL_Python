#!/usr/bin/env python
# coding=utf-8

import urllib
import os
import csv

def citi_bike():
    path = os.getcwd()
    os.chdir(path)
    if not(os.path.exists('dec-2week-2014.csv')):
        url = 'http://52.25.91.45/misc_files/dec-2week-2014.csv'    
        dest_dir = os.path.join('dec-2week-2014.csv')
        urllib.urlretrieve(url, dest_dir)
    
    with open('dec-2week-2014.csv', 'rb') as csvfile:
        citibike=csv.reader(csvfile, delimiter=',')
        male = 0
        female = 0
        for line in citibike:
            if line[14]=='1':
                male += 1
            else:
                female += 1
        print ("The Number of Male Riders is %d."%male)
        print ("The Number of Female Riders is %d."%female)
        p1 = float(male)/(male+female)
        p2 = float(female)/(male+female)
        print ("The Percentage of Male Riders is %f."%p1)
        print ("The Percentage of Female Riders is %f."%p2)
if __name__ == '__main__':
    citi_bike()
