# coding: utf-8

# #Question:
# The recent Citi Bike data has garnered a lot of attention. Attached you will find a data set of Citibike riders. The challenge is threefold:
# 1. Calculate and print the average trip duration
# 2. Visualize the usage by gender (male, female, unknown) and by user type (subscriber vs customer) over the period of a month.
# 3. Visualize total monthly usage by gender on a hourly basis (24 hrs over x-axis)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
from datetime import datetime

print "Loading data......"
data = pd.read_csv("2014-07-Citi_Bike_trip_data.csv")
print "Calculating the average trip duration......"
print np.average(data["tripduration"])

print "Visualizing......"
male = data["gender"]==1
female = data["gender"]==2
unknown = data["gender"]==0
customer = data["usertype"]=="Customer"
subscriber = data["usertype"]=="Subscriber"

def _calculate_time(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")    
v_calculate_time = np.vectorize(_calculate_time)
start = v_calculate_time(data["starttime"])

m = np.zeros(24)
f = np.zeros(24)
u = np.zeros(24)
def _check(start,cond,sex):
    if sex and start.hour==cond:
        return 1
    else:
        return 0
v_check = np.vectorize(_check)
for i in xrange(24):
    m[i] = np.sum(v_check(start,i,male))
    f[i] = np.sum(v_check(start,i,female))
    u[i] = np.sum(v_check(start,i,unknown))

pk = m+f+u

fig = plt.figure()
fig.canvas.set_window_title("Python Core Challenge")
gs = gridspec.GridSpec(2, 2)
ax = fig.add_subplot(gs[0,:])
x_g = 0.22
y_g = 0.5
x_t = 0.22
y_t = 0.5
ap_width = 1
ap_const = 1
ap_ind = np.arange(24)

# For Hourly Usage
rect1 = ax.bar(np.arange(24), pk, color='#3F5D7D',edgecolor=None, alpha=0.3)

rect2 = ax.bar(np.arange(24), f, color='#3F5D7D',edgecolor=None, alpha=0.7, bottom=m)

rect3 = ax.bar(np.arange(24), u, color='#3F5D7D',edgecolor=None, alpha=1, bottom=m+f)
ax.plot(np.arange(24)+0.4, pk, color='#ff0000')

ax.legend( (rect1, rect2, rect3), ('Men', 'Women', 'Unknown') )

ax.set_xlabel('Hour of the Day')
ax.set_xticks(np.arange(pk.shape[0]))
ax.set_xlim(right = pk.shape[0])
ax.grid(color='grey', linestyle='--', linewidth=1, alpha=0.2)
ax.set_ylabel('Number of People')
ax.set_title('Peak Hour for July 2014')

# For Gender
bx = fig.add_subplot(gs[1,0])                                                       
rect2 = bx.bar(np.arange(2)+0.3, (sum(m),sum(f)), 0.3, color='#3F5D7D', edgecolor=None, alpha=0.7)                                       
bx.set_xlabel('Gender')                                                         
bx.set_ylabel('Number of people')                                               
bx.set_title('Rides by Men vs Women')                                           
bx.grid(color='grey', linestyle='--', linewidth=1, alpha=0.2)                   
bx.set_xlim([0, 2])                                                             
bx.set_ylim(top = 1.02 * data.shape[0])                                            
bx.axes.get_xaxis().set_visible(False)                                          
bx.tick_params(labelsize=8)                                                     
bx.text(x_g, y_g, 'Male', horizontalalignment='center', verticalalignment='center', color='#303030', weight='ultralight', rotation='horizontal', transform=bx.transAxes)     
bx.text(x_g, y_g-0.2, np.sum(m), horizontalalignment='center', verticalalignment='center', color='#303030', weight='ultralight', rotation='horizontal', transform=bx.transAxes)
bx.text(x_g+0.5, y_g, 'Female', horizontalalignment='center', verticalalignment='center', color='#303030', weight='ultralight', rotation='horizontal', transform=bx.transAxes)
bx.text(x_g+0.5, y_g-0.2, np.sum(f), horizontalalignment='center', verticalalignment='center', color='#303030',        weight='ultralight', rotation='horizontal', transform=bx.transAxes) 

cx = fig.add_subplot(gs[1,1])               
utype = (np.sum(customer),np.sum(subscriber))
rect3 = cx.bar(np.arange(2)+0.3, utype, 0.3, color='#3F5D7D', edgecolor=None, alpha=0.7)
cx.set_xlabel('Types of Customers')
cx.set_ylabel('Number of Customers')
cx.set_title('Customers vs Subscribers')
cx.grid(color='grey', linestyle='--', linewidth=1, alpha=0.2)
cx.set_xlim([0, 2])
cx.set_ylim(top = 1.02 * data.shape[0])
cx.axes.get_xaxis().set_visible(False)
cx.tick_params(labelsize=8)
cx.text(x_t, y_t, 'Customers', horizontalalignment='center',
        verticalalignment='center', color='#303030',
        weight='ultralight', rotation='horizontal', transform=cx.transAxes)
cx.text(x_t, y_t-0.2, utype[0], horizontalalignment='center',
        verticalalignment='center', color='#303030',
        weight='ultralight', rotation='horizontal', transform=cx.transAxes)
cx.text(x_t+0.5, y_t, 'Subscribers', horizontalalignment='center',
        verticalalignment='center', color='#303030',
        weight='ultralight', rotation='horizontal', transform=cx.transAxes)
cx.text(x_t+0.5, y_t-0.2, utype[1], horizontalalignment='center',
        verticalalignment='center', color='#303030',
        weight='ultralight', rotation='horizontal', transform=cx.transAxes)

plt.show()
