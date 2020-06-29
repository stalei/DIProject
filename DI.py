#!/usr/bin/env python
# coding: utf-8

# # Surge vs infection rate at the openning time
# ## Shahram Talei- University of Alabama

# This is a simple toy model to study ....


#  © Shahram Talei @ 2020 The University of Alabama
#you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.

import csv
import urllib.request
from datetime import timedelta, date
import matplotlib.pyplot as plt
import numpy as np
import io
import datetime
from scipy.optimize import minimize
from scipy.optimize import curve_fit
import pandas as pd

def fit(variables,d,m):
	g=variables
	return d+m*np.asarray(g)

USdailyTestURL='http://covidtracking.com/api/us/daily.csv' #ref: https://covidtracking.com/
csvURL='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/'
StatesList=["New York","Alabama","Florida"]
#ReopeningDate=[date(2020, 5, 28),date(2020, 4, 26),date(2020, 4, 30),date(2020, 5, 4)] # 3 days before reopening
ReopeningDate=[46,18,22]
f_date = date(2020, 4, 12) # earliest date date(2020, 4, 12).before this date, US data was mixed with other countries in one file.
l_date = date(2020, 6, 25) #date.today() # or enter manually: date(2020, 3, 23)#
delta = l_date - f_date
daycount=delta.days +1
totEachDay=[0]*daycount
# Reopening dates https://www.nytimes.com/interactive/2020/us/states-reopen-map-coronavirus.html
# New York Stay-at-home order expired on May 28
# Alabama Stay-at-home order expired on April 30
# Arizona Stay-at-home order expired on May 15
# Colorado Stay-at-home order expired on April 26
# Florida Stay-at-home order expired on May 4
# Louisiana Stay-at-home order expired on May 15
# New Hampshire Stay-at-home order expired on June 15
OpeningGrowth=[0,0,0]
Week2Growth=[0,0,0]
week2Increase=[0,0,0]

#
plt.rcParams["font.size"] =13

# Preparing plots so we can add elements in each step.

fig1 = plt.figure(figsize=plt.figaspect(1./3.))
fig1.suptitle('COVID-19 - ' + ' ( date (0): '+str(l_date)+')')
ax1 = fig1.add_subplot(221)
#ax1.set_xlabel('days ago')
ax1.set_ylabel('Log(N)')
ax1.set_xlim(daycount-1, -3)
ax1.title.set_text('Confirmed')
ax1.grid(True)

ax3 = fig1.add_subplot(222)
#ax3.set_xlabel('days ago')
ax3.set_ylabel('Log(N)')
ax3.set_xlim(daycount-1, -3)
ax3.title.set_text('Deaths')
ax3.grid(True)
ax4 = fig1.add_subplot(223)
ax4.title.set_text('State-Last growth- 7 day corrolation')
ax4.set_xlabel('days ago')
ax4.set_ylabel('Growth factor')
ax4.set_xlim(daycount-2, -3)
ax4.set_ylim(-2, 10)
ax4.axhspan(1, 10, alpha=0.15, color='red')
ax4.axhspan(-2, 1, alpha=0.15, color='green')

ax4.grid(True)

ax6 = fig1.add_subplot(224)
ax6.set_xlabel('days ago')
ax6.set_ylabel('Death ratio')
ax6.set_xlim(daycount-1, -3)
ax6.grid(True)
#inverse axis for days ago on x
daysaxis=range(daycount-1,-1,-1)
daysaxis_1=range(daycount-2,-1,-1)
g1=[1]*daycount
#ax4.plot(daysaxis,g1,'b',linestyle=':',label="Inflection Point")
ax4.hlines(y=1,xmin=daycount, xmax=-3,color='k',linestyle='-.',label="Inflection Point")

fig2 = plt.figure(figsize=plt.figaspect(1))
fig2.suptitle('COVID-19 - Increase in two weeks after reopening ')
ax21 = fig2.add_subplot(111)
ax21.set_ylabel('Increase two weeks after reopening')
ax21.set_xlabel('Reopening growth factor')
ax21.title.set_text('GrowthFactor')
ax21.grid(True)

j=0
for state in StatesList:
    i=0
    w2=0
    ####### These are lists of the values for all days
    totConfirmed=[0]*daycount
    totDeath=[0]*daycount
    totRecovered=[0]*daycount
    GrowthFactorAll=[0]*daycount
    ## temporary variables to keep the values for each days
    totConfPrePreviousDay=0
    totConfPreviousDay=0
    GrowthFactor=0
    totConf=0
    print(state)
    print("Please wait...")
    # the main loop on all files
    for n in range(0,daycount):
        day=(f_date + timedelta(n)).strftime("%m-%d-%Y")
        dayRev=(f_date + timedelta(n)).strftime("%Y-%m-%d")
        #print(day)
        csvfile=csvURL+str(day)+'.csv'
        #print(csvfile)
        response = urllib.request.urlopen(csvfile)
        data = response.read()
        csvdata = csv.reader(io.StringIO(data.decode('utf-8')), delimiter=',')
        next(csvdata)
        totConfPrePreviousDay=totConfPreviousDay
        totConfPreviousDay=totConf
        totConf=0;
        totRec=0;
        totD=0;
        for row in csvdata:
            if row[0]==state: #because the data for US is also displayed for each states separately
                totConf+=int(row[5])
                totD+=int(row[6])
                #print(row[7])
                #totRec+=int(row[7])
        #print(totConf,totRec,totD)
        totConfirmed[n]=totConf
        #totRecovered[n]=totRec
        totDeath[n]=totD
        if totConfPreviousDay - totConfPrePreviousDay !=0:
            GrowthFactor=(totConf-totConfPreviousDay)/(totConfPreviousDay-totConfPrePreviousDay)
        #print(GrowthFactor)
        GrowthFactorAll[n]=GrowthFactor
        ##
        #print(ReopeningDate[j])
        w2=ReopeningDate[j]+15
        if ReopeningDate[j]==n:
            print("got the day")
            #print(n)
            print(GrowthFactor)
            print("Please wait...")
            #print(GrowthFactorAll[n])
            OpeningGrowth[j]=GrowthFactor
            t1=totConf
        elif w2==n:# n>w2 and n<w2+7: #w2==n:
            print("got the w2 day")
            #print(w2)
            print(GrowthFactor)
            print("Please wait...")
            Week2Growth[j]+=GrowthFactor
            t2=totConf
            week2Increase[j]=t2-t1
        i+=1
    #week2Increase[j]/=totConf
    Week2Growth[j]/7
    j+=1
    #print(GrowthFactor)
    GrowthFactorAll2=GrowthFactorAll[1:daycount+2]
    ser = pd.Series(GrowthFactorAll2)
    corr=ser.autocorr(lag=7)
    ax1.plot(daysaxis,np.log10(totConfirmed),'+',label=str(state))
    ax3.plot(daysaxis,np.log10(totDeath),'x',label=str(state))
    ax4.plot(daysaxis_1,GrowthFactorAll2,linestyle='-',label=str(state)+'='+str(round(GrowthFactor,2))+','+str(round(corr,2)))
    ax6.plot(daysaxis,np.divide(totDeath,totConfirmed),linestyle='-',label=str(state))

##let's fit a function:
initial_guess = [2000.0, 1.0]
parameters,param_covariance=curve_fit(fit,OpeningGrowth,week2Increase,initial_guess)
print("fit parameters:")
print(parameters)
d,m = parameters

ax21.plot(OpeningGrowth,week2Increase,'o',label='Data')
ax21.plot(OpeningGrowth,fit(OpeningGrowth,d,m),'r',label='Fit')
ax1.legend(loc=4)
#ax2.legend(loc=4)
ax3.legend(loc=4)
ax4.legend(loc=1)
#ax5.legend(loc=1)
ax6.legend(loc=1)
ax21.legend(loc=2)
plt.show()

g_in =float(input("Enter an opening growth rate to see the prediction: "))
prediction=int(fit(g_in,d,m))
print("Increase prediction is:%d"%prediction)
