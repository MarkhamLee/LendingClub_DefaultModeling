## About This Project 
This goal of this project was to take data from Lending Club (a peer to peer lender) and see if I could use machine learning to reduce their default rate (originally 19.2%) on their personal loan portfolio. The goal of this analysis was to find out if machine learning and/or general EDA could be used to hypothetically improve one's returns beyond what one would get by just investing in the highest grade loans as defined by Lending Club's ranking system: grade A, B, C, et al. The metric to beat was the annualized return of the highest grade loans vs the loans selected by the model. The reason for doing this is that the primary concern(s) of Lending Club and their investors is going to be the performance of the lending portfolio, not machine learning accuracy metrics. ***I.e., "how much more money will this model make me"?*** I used XG Boost to generate the loan default predictions as it gave the best results, beating logistical regression via SK Learn, Decision Trees from same and a keras neural net classification model. 

### High Level Results

* If Lending Club only funded the loans slected by the model their default rate would drop from **~19% to 11%** and their annualized return would increase from **1.92% to 2.65%.**
* Net profits would be $275M vs $353M, but their net capital outlay would decline by $2.5B. Given that the annualized return on the extra $78M was only 1.1%, an argument could be be made that the company would be better off redirecting those funds to higher yield activities. 
    * **Note:** [between 2011 and 2016 the range of the 10-yr T-bill rate was between 1.8 and 2.78%.](https://www.macrotrends.net/2016/10-year-treasury-bond-rate-yield-chart). One can easily argue that Lending Club would've been better off investing that $2.5 billion in capital elsewhere. 
* In terms of default rates, annualized returns and capital efficiency, the model out performed alternative approaches of either setting an interest rate cap or only investing in higher quality loans.

## About Lending Club

Prior to 2020 Lending Club (LC) provided personal loans for debt consolidation and major purchases. The company worked on a "peer to peer" basis, where loans were often funded by individual investors who could look at a series of potential loan "investments" and then choose to fund all or just part of the loan. The company provided access to their data so that investors could perform their own research prior to funding loans, in addition to encouraging data science & financial analyses for educational purposes. 

### Note on the data
Lending Club shutdown their peer to peer lending business after purchasing a bank in 2020, and no longer provides data on their personal loan portfolio to the public. As of April 2022 I'm unsure of what their specific policy is around using this data which is now several years old, given this, I have not made the LC data available as part of this repo and am only sharing the code and the analysis as an example of the kind of work I'm capable of producing. Additionally, I will happily take this repo down immediately if so requested by Lending Club. 

Additionally: this code, analysis and files in this repository are strictly for educational purposes and are not meant to constitute investment advice.

### Replicating Results

Lending Club no longer offers individual investors the ability to invest in their loans and no longer provides this data via their web site, so you won't be able to use my code to attempt to replicate my results. I.e. this is just an example of my work, rather than a project someone can clone and work with. 

### Files contained within this repo

1) **LC_preprocessing_final.py:** this python script imports the downloaded CSV file from the Lending Club web site and does the initial high level data cleaning related to items where the cleaning tasks are more general and didn't need significant study or a detailed analysis first. E.g. removing the '%' symbol from the values in the interest rate column. Cleaning tasks in this file included: taking log values of columns with large ranges (E.g. income ranged from several thousand to several million) calculating measures such as lost principle, the customer's monthly debt payments before and after the loan and expressing measures such as length of employment in months  instead of things along the lines of: "11 years, 2 months". 

2) **LC_Cleaning_LightEDA.ipynb:** this file is the second stage of cleaning the data, along with some high level EDA. The cleaning tasks in this file were of the type that required significant analysis, E.g. filling in missing values or condensing the categories of loan purposes. This file also hot encodes certain fields and then generates a CSV file for the next stage of the analysis. 

3) **LendingClubDefaultModeling_EDA.ipynb:** this is the notebook where the bulk of the EDA was performed, inclusive of things such as calculating default rates, analyzing loan default trends and creating visualizations. This document takes as an input the CSV file generated by the notebook above. It also has a series of functions are used to generate most of the analysis simply for expediency sake, as it allows me or another user to quickly perform additional EDA or look at the data from another angle.

4) **ml_data_prep.py:** this file prepares the data for machine learning by removing redundant columns, highly correlated features, adding dummy variables, etc.

5) **LendingClubDefaultModeling.ipynb:** this notebook contains the machine learning model (XG Boost) that was used for this project, plus analysis on the financial performance one would achieve by investing in the loans selected by the model. 

### Key References:
* [Machine Learning Mastery](https://machinelearningmastery.com/)
* [Sk Learn Logistic Regression Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)