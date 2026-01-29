# Project Requirements

## Acquire Historic NBA Data from REST API
Historic data is required in order to build and train the predicitve model. 

There are a number of data providers that offer this. Typically, free offerings have some sort of limit
or cap to them. Fee based offerings typically have no limits.

The most basic model that could predict the score of an upcoming game would require the following:
1. Team / Player statistics and rankings by day
2. Daily game schedule 


## Convert Data to Desired Format
After the data is downloaded, it might need to be converted or cleaned to meet the requirements of 
predictive model. Any conversion errors would need to be reported and dealt with manually.


## Develop Predictive Model
Most data science projects follow these high-level steps:
1. Business project understanding - What are we trying to solve?
   1. NBA Game Scores?
   2. Team Rankings?
   3. Player Rankings?
2. Data collection
   1. Current team rankings
   2. Current player rankings?
   3. Daily schedule
3. Data cleaning and processing
   1. Convert data from provider
   2. Report conversion and parsing errors
4. Exploratory data analysis - What are the best predictive variables and factors?
   1. There are Python tools for this
5. Build model
   1. Predictive neural network
   2. There are Python tools for this
6. Communicate model results
   1. Basic web based UI, hosted by GitHub
7. Model deployment and maintenance
   1. The application could be deployed on a low level server that has access to the Internet
   2. Manual tuning of the model based on perceived results

## Automate Gathering of Latest NBA Data
The same data that was gathered to build the model will be requested everyday in order to make the
predictions for the day. 

API errors and data parsing errors will be need to be dealt with manually.

## Run New Against Predictive Model
New data will be used to make predictions for the current day's games.

## Develop Real-time UI for System Monitoring and Prediction Results
A basic UI could be developed to show the health of the system and the daily predictions

## BONUS: Automate Betting Via Online Gambling Venue
Once the daily prediction process is tuned and successfully making predictions, it could be taken
"live" by make actual bets using an gambling API. 
