# DIProject
Shahram Talei
DI.py
As a scientist I was thrilled by solving problems especially problems with a real life implication. The latest pandemic has had a devastating effects on societies and data analysis of the pandemic has been challenging and extremely important to stop the spread and recover our economy after we move out of the pandemic. We still don't have a complete picture of this phenomena so we can study the data and extract the correlations. I start this project with a code to scrape daily reports by John Hopkins university. Then add them together and plot the general trend for a given list of states. First I plot this data. Beside typical total confirmed cases and total death I plot the death ratio.
In the next step I extract the growth factor(GF). GF is defined as the change today divided by the change yesterday. In theory if this number is above one we will see increase and if this number is below one we are moving to contain the spread and stop it so 1 is inflection point. 
Using this number we can study the pattern and in a long time we can perform a time series analysis. For example we can study the surge based on the growth factor at the time of reopening. I extract the growth factor then following the data I look at the number of new cases after two weeks from reopening. 
But more important I plot growth factor change for all these states and we can compare it with the inflection point. I put the last growth factor in the legend. I was also interested to see if there is a weekly correlation in growth rate and I calculate autocorrelation of the growth factor. For these test states this correlation is very weak.
In the next step we can fit a function on this data and predict the surge rate as a function of the growth factor at the time of reopening. This function could help us predict the increase for a new state given their growth factor. And finally this code will ask for a growth factor and will provide the increase two weeks after reopening.
This would be more challenging and more accurate if I include more states and in a real analysis we have to include more parameters however given the short time of the challenge and starting from scratch the result is very exciting and being an open source tool will let other people to reproduce the results and study more data.
The code is written in a flexible way to include any list and fitting part is easy to change to any function. Basic python libraries + numpy + scipy + pandas + csv are required for the analysis.

Stay safe!






