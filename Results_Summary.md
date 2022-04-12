## High Level Results 
* **Key Stats - Original Loan Portfolio:** 
    * Default Rate: 19.2% 
    * Annualized return 1.94% 
    * Total portfolio size 5.9B
    * Earnings: 553M 
* Despite good loans outnumbering bad loans by roughly 4:1, the losses from the bad loans wiped out 61.3% of the gains from the good loans
* The typical bad loan wipes out the gains from 2.6 good loans 
* The performance of the machine learning model(s) were compared to the following two interventions identified during EDA:
    * Only originating loans to customers falling into Grades A, B, C & D per Lending Club's internal grading system. Doing so would only reduce earnings by ~1M, but would reduce capital outlay by nearly 900M. Annualized returns would grow by 15%, default rates would fall to around 16.2% 
    * Setting an interest rate cap of 13.5%, i.e. only originating loans to customers when the current models set interest rates of 13.5% or lower. This approach would reduce default rates to 12.3%, increase annualized return by 25%, but reduce total returns by 87M, while also requiring about 2.4B less in capital. 
* Both the machine learning model and the interventions identified during EDA attempt to identify inflection points, where yield is so low it's not worth lending to customers in higher risk categories and/or customers not identified by the model. 
* **Machine Learning Results:**
    * If Lending Club had restricted its lending to the loans identified by the model, earnings would've been 274M vs. 3.4B in capital. I.e. 80M less in earnings, but requiring 2.5B less in capital. The annualized return would've been 2.66%.
    * The results of the machine learning model exceed the performance of the suggested intervention of setting an interest cap, but fall short of the suggestion of only issuing loans in the higher grades in terms of gross returns, but exceed the performance of approach in terms of capital efficiency and annualized returns. 
    * How valuable this model would be to a lender would largely be a function of how they're looking to optimize thier portfolio. Namely, if an outlay of an additional 2.5B for an annualized gain is worth it to earn an extra 79 million, than neither the models or the suggested interventions are valuable. However, if capital efficiency is a goal, then using this model to identify loans and redirecting the excess capital to higher yield activities would undoubtedly give the company better overall results than it would receive by maintaining the status quo or simply raising lending standards. 
    * Of the loans identified by the model roughly 88.8% were good, thus reducing the default rate to around 11.2%. 
    * Recall scores were "okay" at around 68%, meaning the number of loans classified as good equated to about 2/3rds of the total number of good loans in the model 
