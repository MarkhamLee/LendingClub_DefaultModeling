## About This Project 
Lending Club is (well, was, they exited this business in '20) a peer-to-peer lender that gave investors the opportunity to invest in the personal loans they originated to their customers. To aid the decision-making process they would give each loan a letter grade, in addition making data on past loans available for download. Lending Club’s loans were often of the higher risk variety, with the default rate for the dataset used in this project being around 19.2% overall and 16.5% for the loans ranked as “D” class or higher. 

This project has the following goals:  

* Use machine learning to significantly reduce the default rate within the given group of loans.
* Build a machine learning model that would deliver higher returns than what one would receive by just investing in loans ranked C or higher  

The primary evaluation criteria will be default rate and annualized return, with the secondary criteria being capital efficiency. E.g., the models will be rated solely on their ability to make investors' money. 

I used XG Boost to generate the loan default predictions as it gave the best results, beating logistical regression via SK Learn, Decision Trees from same and PyTorch and Keras neural net classification models.  

### High Level Results

In terms of default rates, annualized returns and capital efficiency, the model outperformed alternative approaches of identifying the best loans by setting an interest rate cap or only investing in the highest ranked loans: 

* If Lending Club only funded the loans selected by the model their default rate would drop from **~19% to 11%** and their annualized return would increase from **1.92% to 2.65%.** 

* Net profits would be $275M vs $353M, but their net capital outlay would decline by $2.5B. Given that the annualized return on the extra $78M was only 1.1%, an argument could be made that the company would be better off redirecting those funds to higher yield activities.  

    * **Note:** [between 2011 and 2016 the range of the 10-yr T-bill rate was between 1.8 and 2.78%.](https://www.macrotrends.net/2016/10-year-treasury-bond-rate-yield-chart).  

## About Lending Club

Prior to 2020 Lending Club (LC) provided personal loans for debt consolidation and major purchases. The company worked on a "peer to peer" basis, where loans were often funded by individual investors who could look at a series of potential loan "investments" and then choose to fund all or just part of the loan. The company provided access to their data so that investors could perform their own research prior to funding loans, in addition to encouraging data science & financial analysis projects for educational purposes. 

### Note on the data
Lending Club shut down their peer-to-peer lending business after purchasing a bank in 2020, and no longer provides data on their personal loan portfolio to the public. As of April 2022, I am unsure of what their specific policy is around using this data, which is now several years old. Given the uncertainty around the data, I have not made the LC data available as part of this repo and am only sharing the code and the analysis as an example of my work. 

**Additionally: this code, analysis and files in this repository are strictly for educational purposes and are not meant to constitute investment advice.** 

### Replicating Results

Lending Club no longer offers individual investors the ability to invest in their loans and no longer provides this data via their web site, so you won't be able to use my code to attempt to replicate my results. I.e. this is just an example of my work, rather than a project someone can clone and work with. 

### Files contained within this repo

1) **LC_preprocessing_final.py:** this python script imports the downloaded CSV file from the Lending Club web site and does the initial high level data cleaning related to items where the cleaning tasks are more general and did not need significant study or a detailed analysis first. E.g., removing the '%' symbol from the values in the interest rate column. Cleaning tasks in this file included: taking log values of columns with large ranges (E.g. income ranged from several thousand to several million) calculating measures such as lost principle, the customer's monthly debt payments before and after the loan and expressing measures such as length of employment in months  instead of things along the lines of: "11 years, 2 months". 

2) **LC_Cleaning_LightEDA.ipynb:** this file is the second stage of cleaning the data, along with some high-level EDA. The cleaning tasks in this file were of the type that required significant analysis, e.g. filling in missing values or condensing the categories of loan purposes. This file also hot encodes certain fields and then generates a CSV file for the next stage of the analysis.

3) **LendingClubDefaultModeling_EDA.ipynb:** taking the csv from the above as an input, this is the notebook where the bulk of the EDA was performed, inclusive of things such as calculating default rates, analyzing loan default trends, and creating visualizations.  

4) **ml_data_prep.py:** this file prepares the data for machine learning by removing redundant columns, highly correlated features, adding dummy variables, etc.

5) **LendingClubDefaultModeling.ipynb:** this notebook contains the machine learning model (XG Boost) that was used for this project, plus analysis on the financial performance one would achieve by investing in the loans selected by the model. 

### Key References:
* [Machine Learning Mastery](https://machinelearningmastery.com/)
* [Sk Learn Logistic Regression Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)