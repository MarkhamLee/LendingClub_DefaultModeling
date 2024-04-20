## Results Summary

 ### Original Loan Portfolio 

 **Note:** despite good loans outnumbering bad loans by roughly 4:1, the losses from the bad loans wiped out 61.3% of the gains from the good loans

* Total portfolio size 5.9B
* Gains from good loans ~$912m
* Losses from bad loans: ~$560m
* Net Gains: ~$353M
* Default Rate: 19.2% 
* Annualized return 1.92% 

### High Level Results - Machine Learning Portfolio 

**Note:** the results are based on extrapolating the results of the test dataset to the entire loan portfolio. 
* Total portfolio size: $3.4M 
* Default rate drops to 11.2% 
* Annualized returns increase from 1.92% to 2.65%
* Net gains: $275M vs $3.4B in Capital, a reduction in capital outlay of $2.5B
* $78M fewer gains, but given the significant reduction in capital, capital efficiency improves substantially: the annualized return on the extra $2.5B investment was ~1.1%. 

#### On a capital efficiency basis and default rate basis, the model out performed both potential interventions identified during EDA

* Only originating loans to rated A, B, C & D per Lending Club's internal grading system. Doing so would only reduce earnings by ~1M, but would reduce capital outlay by ~900M. Annualized returns would grow by 15%, default rates would fall to around 16.2%. While one could make the argument that this approach is better than investing in the loans selected by the model, the higher default rate + reduced capital efficiency introduces a lot of risk for little benefit. 

* Setting an interest rate cap of 13.5%, i.e., only originating loans to customers when the current models set interest rates of 13.5% or lower. This approach would reduce default rates to 12.3%, increase annualized return by 25%, but reduce total returns by 87M, while also requiring about 2.4B less in capital.  

 The value of this model to a lender would be a function of how they are looking to optimize their portfolio. Namely: if an outlay of an additional 2.5B for annualized gains of less than 1% is worth it to gain an extra ~$80M, then neither the models nor the suggested interventions are valuable. However, if capital efficiency and/or maximizing returns is the lender's focus then this model could prove quite useful to them. 