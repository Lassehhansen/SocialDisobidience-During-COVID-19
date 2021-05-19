## How Distrust in Government Affects Social Disobedience During A Pandemic: Evidence from Google Mobility Reports and Twitter Mining

#### Parameterizing Social Disobidience in Denmark with the use of Google Mobility Reports. Further a Robust Bayesian Hierarchical Regression model is implemented to understand the effect of feeling towards government measured on twitter on this parameter.

### Twitter Scrape, Preprocessing & Sentiment Analysis 

Firstly, this repositorry contains a python script, where tweets from 1st of march until 1st of April were scraped. In this python script, a Bert model trained to classify Danish text was implemented to get the sentiment of the tweets.

### DMI API, Google Mobility Reports & Bayesian Analysis 

Secondly, this repository contains an r markdown where, weather variables and google mobility reports are scraped and preprocessed. Afterwards, a Robust Bayesian Hierarchical Regression model is implemented to understand the relationship between Social Disobidience and feeling towards government on twitter. 

In the folder 'Analysis' a r function is also uploaded, this is the function i have written to be able to load the DMI data, the data can be found here if replication wants to be done: https://dmigw.govcloud.dk/metObs/v1/bulk/?api-key=e32551a3-e242-45ae-8480-6129201f9a4c.
