#load libraries
library(tidyverse)

#set working directory (adjust this for your own computer)
setwd("C:/Users/Lucy Wu/Documents")

#read dataset into R
credit_df <- read.csv("Credit.csv")
View(credit_df)

#Convert categorical variables to factors with levels and labels
credit_df$Student<-factor(credit_df$Student,levels = c(0,1),labels = c("No","Yes"))
credit_df$Gender<-factor(credit_df$Gender,levels = c(0,1),labels = c("Male","Female"))
credit_df$Married<-factor(credit_df$Married,levels = c(0,1),labels = c("No","Yes"))

#check for missing data
sum(is.na(credit_df))

#generate summary statistics for all variables in dataframe
summary(credit_df)




#partition the data into a training set and a validation set
#set seed so the random sample is reproducible
set.seed(42)
sample <- sample(c(TRUE, FALSE), nrow(credit_df), replace=TRUE, prob=c(0.5,0.5))
train_credit  <- credit_df[sample, ]
validate_credit <- credit_df[!sample, ]


#Create a correlation matrix with the quantitative variables in the training dataframe.
cor(train_credit[c(1, 2, 3, 4, 5, 9)])
#turn off scientific notation for all variables
options(scipen=999) 

#Conduct a multiple regression analysis using the training dataframe 
#with Balance as the outcome variable and all the other variables in the dataset 
#as predictor variables. 

credit_mr <- lm(Balance ~ Income + Limit + Rating + Age + Education + Student + Gender + Married,
                    data = train_credit)
#View multiple regression output
summary(credit_mr)

library(car)

#Calculate the Variance Inflation Factor (VIF) for all predictor variables. 
vif(credit_mr)


#Conduct a new multiple regression analysis using the training dataframe 
#with Balance as the outcome variable and 
#Income, Rating, Age, Education, Student, Gender, and Married as predictor variables.
credit_mr_all<- lm(Balance ~ Income + Rating + Age + Education + Student + Gender + Married,
                    data = train_credit)
#View multiple regression output
summary(credit_mr_all)


#load libraries
library(car)


#Create a residual plot and a normal probability plot 
#using the results of the regression analysis in Step (6). 
credit_pred = predict(credit_mr_all)
credit_res = resid(credit_mr_all)
pred_res_df <- data.frame(credit_pred, credit_res)
ggplot(data = pred_res_df, mapping = aes(x = credit_pred, y = credit_res)) +
  geom_point() +
  labs(title = "Plot of residuals vs. predicted values", x = "Predicted values",
       y = "Residuals")


#Steps to create a Normal Probability Plot 

#create a vector of standardized residuals generated from the multiple
#regression above
credit_std.res = rstandard(credit_mr_all)

#produce normal scores for the standardized residuals and create
#normal probability plot
qqnorm(credit_std.res, ylab = "Standardized residuals", xlab = "Normal scores")



#Conduct a new multiple regression analysis using the training dataframe 
#with Balance  as the outcome variable and only the variables with 
#statistically significant relationships with Balance 

credit_mr_new <- lm(Balance ~ Income + Rating + Age + Student,
                      data = traincar)
#View multiple regression output
summary(credit_mr_new)



#What is the standardized slope coefficient for the Income variable 
#in the regression model from Step (9)

#load lm.beta
library(lm.beta)

#Extract standardized regression coefficients
lm.beta(credit_mr_new)



#Conduct a final multiple regression analysis using the validation dataframe 
#with Balance  as the outcome variable and 
#only the variables with statistically significant relationships with Balance 
#(the same variables as in Step (9) as predictors.


#run a final multiple regression model using the "validate" dataframe 
#and the following predictors: Age, KM, Horsepower, FuelType, and Automatic
credit_mr_Val <- lm(Balance ~ Income + Rating + Age + Student, 
                    data = validatecar)

summary(credit_mr_Val)

#Using the data contained in the csv file “credit_card_prediction.csv”, 
#predict the credit card balances for three new cardholders, 
#with 95% prediction intervals.

predictiondf <- read.csv("credit_card_prediction.csv")
View(predictiondf)

#Convert categorical variables to factors with levels and labels
predictiondf$Student<-factor(predictiondf$Student,levels = c(0,1),labels = c("No","Yes"))

predict(credit_mr_Val, predictiondf, interval = "prediction", level = 0.95)


