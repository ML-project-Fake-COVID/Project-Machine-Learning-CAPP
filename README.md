# Project-Machine-Learning
Twitter Bot & COVID-19

* Macarena Guzman
* Rukhshan Arif Mian
* Yue Kuang

## Executive Summary

Given the current pandemic of COVID-19 affecting the world is crucial for the people, to get accurate and timely information. Twitter, one of the most important social media platforms, is working assiduous spreading reliable and trustworthy facts related to the pandemic. 

However, as the pandemic is spreading, the misinformation is spreading as fast as the disease itself. Bots accounts on twitter are responsible for more than half of misinformation spreading, this inaccurate information includes topics as “unproved cures”, “conspiracy theories” and “reopening America”.

As bots are an important part combating misinformation, our project aim to identifies bots accounts tweeting about COVID-19. This project relies on machine learning approaches, training Naives Bayes, Decision Tree and Random Forest models in order to label accounts as bot giving some common features.

## Distribution of files
data_consolidation: This folder contains the original consolidated labeled and unlabeled datasets.
- consolidated_version2.csv --> this csv is used to train the machine learning models.
- covid_user_info.csv --> this csv is used to predict labels under the best-trained model.

Data_Cleaning: This folder contains a Jupyter Notebook which unifies and cleans the datasets.
- data_cleaning.ipynb --> this Jupyter notebook cleans the 'consolidated_version2.csv' and 'covid_user_info.csv' transforming all the columns into features to train our models. After run this notebook will be created two new csv files:
1. verified.csv: Clean version of consolidated_version2.csv ready to train the models.
2. COVID_tweet.csv: Clean version of covid_user_info.csv ready to test the models.

Exploring-Features: this folder explores the features and models run to find the ultimate best model.
- naive_bayes_predict.ipynb --> This Jupyter Notebook contains the information related to the naive_bayes Model. Returns nb_predicted.csv --> Predicted labels under the COVID_tweet dataset under the best Naive Bayes model.
- decision_tree.ipynb --> This Jupyter Notebook contains the information related to the decision tree model.
- random_forest.ipynb --> This Jupyter Notebook contains the information related to the random forest models. Returns COVID_prediction --> Predicted labels under the COVID_tweet dataset under the best random forest model.

- created_time_accounts_test.csv --> test labeled dataset under the 7 features best model of random forest, this dataset is used by the validate_results.ipynb which compares true positive and true negatives values.



