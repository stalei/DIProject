# First plot- Extract data from raw csv files
![alt text](https://github.com/stalei/DIProject/blob/master/DataExtract2.png?raw=true)
(Total Confirmed- Total Death- Growth Factor and Correlation - Death Ratio)

John Hopkins university collects daily cases state by state.
[https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)

Using the first part of the code I collect all the information between two given dates. I ran this from the first day they created US specific files up to the run time. Before this date they have different file format. I add all data for each state and plot the number of cases in log scale with respect to days from now.
Growth factor is important parameter for policy makers and I extract growth factor for each state and print the last (today's) growth factor at the end.
I also look ag the auto-corrolation with lag of 7 (weekly) but apparantly there is no strong correlation for given states. Last panel is the death ratio.
