import datetime as dt
import os
import csv
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
from datetime import timedelta, date
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import chisquare

def FilterDate(Data, DStart, DEnd):
    Data['StartDate']=pd.to_datetime(Data['StartDate'], format="%m/%d/%Y")
    Data = Data[(Data['StartDate'] >= DStart) & (Data['StartDate'] <= DEnd)]
    return Data
def FilterConractAmount(Data,LowerLimit):
    Data = Data[(Data['ContractAmount'] > LowerLimit)]
    return Data
def FilterAgency(Data,Agency):
    Data = Data[(Data['AgencyName'] == Agency)]
    return Data
def FilterCategories(Data,Cat1,Cat2):
    Data = Data[(Data['CategoryDescription'] == Cat1) | (Data['CategoryDescription'] == Cat2)]
    return Data
def FilterShortTitle(Data,title):
    #t="+."+title
    #Data = Data[(Data['ShortTitle'] == t)]
    Data = Data[(Data['ShortTitle'].str.contains(title))]
    return Data
def FilterCategory(Data,Cat):
    Data = Data[(Data['CategoryDescription'] == Cat1)]
    return Data
def FilterZipcode(Data,zip):
    #t="+."+title
    #Data = Data[(Data['ShortTitle'] == t)]
    Data = Data[(Data['VendorAddress'].str.endswith(zip))]
    return Data

DataRaw = pd.read_csv('Recent_Contract_Awards.csv',low_memory=False)

Data = DataRaw#[DataRaw['BOROUGH'] == 'MANHATTAN'].copy()
del DataRaw
print(Data.head(1))
#print(Data['StartDate'].year)
DStart=date(2010,1,1)
DEnd=date(2019,12,31)
Data2 = FilterDate(Data, DStart,DEnd)
#print(Data2)
Data2.dropna(subset=['ContractAmount'])
Data3=FilterConractAmount(Data2,0) ### Use this for the rest
print(np.sum(Data3['ContractAmount']))
#Data2[['HOUR']].plot.hist()
#Data['StartDate']=pd.to_datetime(Data['StartDate'], format="%m/%d/%Y")
#print(Data['StartDate'])

#2
Agency="Citywide Administrative Services"
DataFor2=FilterAgency(Data3,Agency)
AgencyTotalAmount=np.sum(DataFor2['ContractAmount'])
#print(len(set(DataFor2['VendorName'])))
UniqueVendors=set(DataFor2['VendorName'])
size =len(UniqueVendors)
print("size:%d"%size)
VendorName=[]*size
VendorAmount=[0]*size
i=0
for v in UniqueVendors:
    dtemp=DataFor2[(DataFor2['VendorName']==v)]
    amount=dtemp['ContractAmount']
    #VendorName[i]=v
    VendorAmount[i]=np.sum(amount)
    #print(i)
    i+=1
i=0
for v in UniqueVendors:
    print(v,VendorAmount[i])
    i+=1
Top50Amount = sorted(VendorAmount, reverse = True)[:50]
#print(Top50Amount)
#print(Top50Amount[49])
Top50AmountSum=np.sum(Top50Amount)
FracTop50=Top50AmountSum/AgencyTotalAmount
print("Top 50 frac:%g"%FracTop50)

#3
Cat1="Construction Related Services"
Cat2="Construction/Construction Services"
DataFor3=FilterCategories(Data3,Cat1,Cat2)
TotFor3=np.sum(DataFor3['ContractAmount'])
#print(DataFor3['ContractAmount'],DataFor3['ShortTitle'],DataFor3['CategoryDescription'])
DataCentralPark=FilterShortTitle(DataFor3,"CENTRAL PARK")
DataWSP=FilterShortTitle(DataFor3,"WASHINGTON SQUARE PARK")
pd.set_option('display.max_colwidth', -1)
print(DataCentralPark['ShortTitle'])
print(DataWSP['ShortTitle'])
TotForCentralPark=np.sum(DataCentralPark['ContractAmount'])
TotForWSP=np.sum(DataWSP['ContractAmount'])
FracCentralPark=TotForCentralPark/TotFor3
FracWSP=TotForWSP/TotFor3
ANS3=TotForCentralPark/TotForWSP
print("Answer 3:%g"%ANS3)
#4
DataFor4=FilterCategory(Data3,"Goods")
totYear=[]
y=np.array(range(2010,2019)).reshape((-1, 1))
#years=range(2010,2019)
for yr in range(2010,2019):
    Di=date(yr,1,1)
    Df=date(yr+1,12,31)
    D4= FilterDate(DataFor4, Di,Df)#  DataFor4[date(DataFor4['StartDate']).year==yr]
    totYear.append(np.sum(D4['ContractAmount']))
print(totYear)
model = LinearRegression().fit(y, totYear)
r_sq = model.score(y, totYear)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
fig2 = plt.figure(figsize=plt.figaspect(1))
fig2.suptitle('Yearly expenditure')
ax21 = fig2.add_subplot(111)
ax21.set_ylabel('Amount')
ax21.set_xlabel('Year')
ax21.title.set_text('Contract amount-year')
ax21.grid(True)
ax21.plot(y,totYear,'o',label='Data')
ax21.legend(loc=2)


#5

UniqueAgencies=set(Data3['AgencyName'])
ContractCount=[]
for Agency in UniqueAgencies:
    D5=Data3[Data3['AgencyName']==Agency]
    ContractCount.append(len(D5['ContractAmount']))
Top5Contract = sorted(ContractCount, reverse = True)[:5]
ContractLimit=Top5Contract[4]
meanAmount=[]
for Agency in UniqueAgencies:
    D5=Data3[Data3['AgencyName']==Agency]
    cont=len(D5['ContractAmount'])
    if cont>=ContractLimit:
        meanAmount.append(np.mean(D5['ContractAmount']))
print(meanAmount)
meanAmountSorted= sorted(meanAmount, reverse = True)[:5]
print(meanAmountSorted)
print("Answer5:%g"%(meanAmountSorted[0]/meanAmountSorted[1]))
######
##6
Agency6="Parks and Recreation"
DataFor6=FilterAgency(Data3,Agency6)
DataNoticeFor6=FilterShortTitle(DataFor6,"NOTICE OF AWARD")
DataNoticeFor6['StartDate']=pd.to_datetime(DataFor6['StartDate'], format="%Y/%m/%d")
print(DataNoticeFor6['StartDate'].dt.dayofweek)
dofweek=DataNoticeFor6['StartDate'].dt.dayofweek
chi2=chisquare(dofweek)
print("chi square:")
print(chi2)
fig3 = plt.figure(2,figsize=plt.figaspect(1./2.))
ax3 = fig3.add_subplot(121)
ax3.hist(dofweek)

######
#7
Agency7="Environmental Protection"
DataFor7=FilterAgency(Data3,Agency7)
DataFor7['StartDate']=pd.to_datetime(DataFor7['StartDate'], format="%Y/%m/%d")
#print(DataFor7['StartDate'].dt.month)
monthlyExp=[]
m0=range(1,12)
for y in range(2010,2019):
    D=DataFor7[DataFor7['StartDate'].dt.year==y]
    for m in range(1,12):
        D2=D[D['StartDate'].dt.month==m]
        monthlyExp.append(np.sum(D2['ContractAmount']))
ax4 = fig3.add_subplot(122)
ax4.plot(monthlyExp)
s = pd.Series(monthlyExp)

print("Autocorrolation:%g"%s.autocorr(lag=12))

##########################
##8
DStart=date(2018,1,1)
DEnd=date(2018,12,31)
DataFor8 = FilterDate(Data3, DStart,DEnd)
NYCTot=0
Tot=np.sum(DataFor8['ContractAmount'])
with open('Zip2.csv') as csvfile: #Scraped all zipcodes to this csv file
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row[1])
        #print(len(row))
        for i in range(0,len(row)):
            D=FilterZipcode(DataFor8,row[i])
            #print(D['VendorAddress'])
            NYCTot+=np.sum(D['ContractAmount'])
TotOthers=Tot-NYCTot
print("NYC/Tot:%g"%(NYCTot/Tot))
print("NYC/TotOthers:%g"%(NYCTot/TotOthers))
plt.show()
