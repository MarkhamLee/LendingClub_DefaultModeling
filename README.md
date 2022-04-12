## About This Project 
This is an update to a project I built about 18 months ago, where the changes were significant enough to justify just creating a new repo for it. The goal was to take data from Lending Club (a peer to peer lender) and see if I could use machine learning to reduce the default rate (originally 19.2%) on their personal loans. The major difference this time around (aside from a higher performing model) is that I used the EDA process to set goals for ML, in terms of reducing defaults and increasing earnings and instead of just focusing on accuracy goals like f1 or precision, I instead looked at the financial performance of the loan portfolio selected by the model to gauge the model's effectiveness. 

Unfortunately, Lending Club no longer offers individual investors the ability to invest in their loans and no longer provides this data via their web site, so you won't be able to use my code to attempt to replicate my results. I.e. this is just an example of my work, rather than a project someone can clone and work with. 

I used XG Boost to generate the loan default predictions as that gave the best results, beating logistical regression via SK Learn, Decision Trees from same and a keras neural net classification model. 


## Note on the data

Up until the last the year or so, Lending Club operated as a peer 
to peer lender and provided access to data on their loans for investors to analyze, as well as encouraging data science analysis for educational purposes. However, back in 2020 they purchased a bank, are now operating as a traditional lender and are no longer a peer to peer lender. As a result, they no longer provide this data to the public. Prior to this change they had issued some restrictions around usage of their data being restricted to investment analysis, only usable by customers or investors, etc., and as of April 2022 I'm unsure of what their specific policy is around using this data, which is now several years old. Given this, I have not made the LC data available as part of this repo and am only sharing the code and the analysis as an example of the kind of work I'm capable of producing. Additionally, I will happily take this repo down immediately if so requested by Lending Club. 

## General notes on Lending Club's Data Usage Rules 

Unless prior authorization is given Lending Club restricts the use of their data to investment evaluation purposes, so I've limited the scope of this project to looking at things from an investment perspective and have purposely avoided analyses that go beyond the scope of what's included in their public facing data for potential investors. Functionally this means that the EDA won't do things like profile ideal customers, and the predictive modeling will focus on minimizing losses.

If you want to replicate my results you will have to download the data for the 2015 calendar year directly from Lending Club, create a directory called 'data' and then update the file name where appropriate in the preprocessing file. Also, the LC files downloaded in an inconsistent matter whereas some opened up without issues and others didn't, in a few instances I had to open them up in Excel and then re-save them as a UTF-8 CSV.

Additionally: this code, analysis and files in this repository are strictly for educational purposes and are not meant to constitute investment advice.


## About Lending Club

Lending Club (LC) is a lender that provides personal loans for debt consolidation and major purchases. The company works on a "peer to peer" basis, in that loans are often funded by individual investors who can look at a series of potential loan "investments" and choose to fund all or part of the loan. The goal of this analysis will be find out if machine learning and/or general EDA could be used to hypothetically improve one's returns beyond what one would get by selecting loans by the grades LC assigns to them, or by investing in a broad basket of loans. Unlike most machine learning problems where the accuracy is the primary objective, I intend to show how a "good" or "okay" model can dramatically improve returns in a peer to peer lending scenario if it identifies a significant percentage of the bad loans. A loan default can cost significantly more than paid off loan generates in profit, so within certain parameters a model that causes you to "miss out" on a number of good investments is still valuable if it flags a significant number of bad ones. The general idea is that since an individual investor can only invest in a limited number of loans, the goal is to minimize the # of bad loans in basket of loans that are selected for investment.


### Replicating Results

NA - this repo is stricly for informational purposes, as the data is no longer publically available 

### Files contained within this repo

1) **LC_preprocessing_final.py:** this python script imports the downloaded CSV file from the Lending Club web site and does the initial high level data cleaning related to items where the cleaning tasks are more intuitive and don't need significant study an analysis first. E.g. removing the '%' symbol from the values in the interest rate column. Cleaning tasks in this file included: taking log values of columns with large ranges (E.g. income ranged from several thousand to several million) calculating measures such as lost principle, the customer's monthly debt payments before and after the loan and expressing measures such as length of employment in months. Another reason for doing this work in a single script vs. a notebook is that due to the size
of the file, it was significantly faster to subset the file, update fields and calculate measures in a script vs a notebook.

2) **LC_Cleaning_LightEDA.ipynb:** this file is the second stage of cleaning the data, along with some high level EDA. The cleaning tasks in this file were of the type that required significant analysis, E.g. filling in missing values or condensing the categories of loan purposes. This file also hot encodes certain fields and then generates a CSV file that can then be picked up/used by the machine learning notebook. This file will generate a CSV file for the next stage.

3) **LendingClubDefaultModeling_EDA.ipynb:** this notebook where the EDA was performed, inclusive of things such as calculating default rates, analyzing loan default trends and creating visualizations. This document takes as an input the CSV file generated by the notebook above. It also has a series of functions are used to generate most of the analysis simply for expediency sake, as it allows me or another user to quickly perform additional EDA or look at the data from another angle.

4) **ml_data_prep.py:** this file prepares the data for machine learning by removing certain columns and adding dummy variables. It also has helper functions for finding highly correlated features and deleting those columns from the dataset. The functions for finding feature correlations weren't used, as I did that work in the machine learning notebook as it was easier given the work I needed to do around analyzing investment returns prior to removing features and performing machine learning modeling. Since the purpose of this file is to be a general purpose machine learning preparing script, I left the correlated features functions in.

5) **LendingClubDefaultModeling.ipynb:** this notebook contains the machine learning models (XG Boost) that were used for this project, plus analysis on the financial performance of the loan identified by the model. 

### Key References:
* [Machine Learning Mastery](https://machinelearningmastery.com/)
* [Sk Learn Logistic Regression Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)