

![alt text](https://github.com/stalei/DIProject/blob/master/Fit.png?raw=true)

(Surge vs Reopening Growth Factor)

I plot the number of new cases two weeks after reopening as a function the growth factor at reopening.
In the next step we can fit a function on this data and predict the surge rate as a function of the growth factor at the time of reopening. 
This function could help us predict the increase for a new state given their growth factor. And finally this code will ask for a growth factor 
and will provide the increase two weeks after reopening.
 Reopening time are taken from NYTimes reoprt:
[https://www.nytimes.com/interactive/2020/us/states-reopen-map-coronavirus.html](https://www.nytimes.com/interactive/2020/us/states-reopen-map-coronavirus.html)

THIS PLOT IS FOR DEMONSTRATION PURPOSE ONLY. MORE DATA ANALYSIS IS REQUIRED ON MORE STATES AND THIS FUNCTION HAS A DIFFERENT FORM IN REALTY

Using this fit we can start making predictions:
Sample output:

    fit parameters:
    
    [-19861.12495688  22312.70488886]
    
    Enter an opening growth rate to see the prediction: 1.13
    
    Increase prediction is:5352




Link to full project:
[https://github.com/stalei/DIProject](https://github.com/stalei/DIProject)
