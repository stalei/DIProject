# DIProject
Shahram Talei
(DI.py)

![alt text](https://github.com/stalei/DIProject/blob/master/scince-mag.png?raw=true)

As a scientist I was thrilled by solving problems especially problems with a real life implication. The latest pandemic has had a devastating effects on societies and data analysis of the pandemic has been challenging and extremely important to stop the spread and recover our economy after we move out of the pandemic. We still don't have a complete picture of this phenomena so we can study the data and extract the correlations. I start this project with a code to scrape daily reports by John Hopkins university. 

[https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)

Then add them together and plot the general trend for a given list of states. First I plot this data. Beside typical total confirmed cases and total death I plot the death ratio.

![alt text](https://github.com/stalei/DIProject/blob/master/DataExtract2.png?raw=true)
(Total Confirmed- Total Death- Growth Factor and Correlation - Death Ratio)

In the next step I extract the growth factor(GF). GF is defined as the change today divided by the change yesterday.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;GF=\frac{\Delta%20N_{today}}{\Delta%20N_{yesterday}}" title="\Large GF=\frac{N_{Today}}{N{Yesterday}}" />

In theory if this number is above one we will see increase and if this number is below one we are moving to contain the spread and stop it so 1 is inflection point. 
Using this number we can study the pattern and in a long time we can perform a time series analysis. For example we can study the surge based on the growth factor at the time of reopening. I extract the growth factor then following the data I look at the number of new cases after two weeks from reopening. 


We can also plot positivity rate:
![alt text](https://github.com/stalei/DIProject/blob/master/positivity.png?raw=true)




But more important I plot growth factor change for all these states and we can compare it with the inflection point. I put the last growth factor in the legend. I was also interested to see if there is a weekly correlation in growth rate and I calculate autocorrelation of the growth factor. For these test states this correlation is very weak. Reopening time are taken from NYTimes reoprt:
[https://www.nytimes.com/interactive/2020/us/states-reopen-map-coronavirus.html](https://www.nytimes.com/interactive/2020/us/states-reopen-map-coronavirus.html)

In the next step we can fit a function on this data and predict the surge rate as a function of the growth factor at the time of reopening. This function could help us predict the increase for a new state given their growth factor. And finally this code will ask for a growth factor and will provide the increase two weeks after reopening.

![alt text](https://github.com/stalei/DIProject/blob/master/Fit.png?raw=true)

(Surge vs Reopening Growth Factor)
THIS PLOT IS FOR DEMONSTRATION PURPOSE ONLY. MORE DATA ANALYSIS IS REQUIRED ON MORE STATES AND THIS FUNCTION HAS A DIFFERENT FORM IN REALTY

Sample output:

    fit parameters:
    
    [-19861.12495688  22312.70488886]
    
    Enter an opening growth rate to see the prediction: 1.13
    
    Increase prediction is:5352


We can also try cross-corellation and lag between confirmed cases and death:

    New York
    Please wait...
    Cross-Corellation:1.02575-lag:14
    Alabama
    Please wait...
    Cross-Corellation:0.991008-lag:0
    Florida
    Please wait...
    Cross-Corellation:0.990245-lag:0

Cross-correlation is ~1. The lag for NY is 14 days but it gives 0 for AL and FL.

This would be more challenging and more accurate if I include more states and in a real analysis we have to include more parameters however given the short time of the challenge and starting from scratch the result is very exciting and being an open source tool will let other people to reproduce the results and study more data.

If I get a chance I would like to include model selection (minimum parameters using stepwise selection) and regularization and finally include unsupervised analysis (neural networks,...) for more accurate predictions.

The code is written in a flexible way to include any list and fitting part is easy to change to any function. Basic python libraries + numpy + scipy + pandas + csv are required for the analysis.

## Future works:
- Include more states
- Develop parallel version (MPI and/or CUDA), I have access to UAHPC and OZ-Star
- Include more predictors

Stay safe!






