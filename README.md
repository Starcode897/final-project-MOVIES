# final-project-TELECOM

#Team Members:
* [Ben Kramskoi](https://github.com/kramskb1)
* [Rachel Chan](https://github.com/chanrce)
* [Ryan Gonzalez](https://github.com/RyanAdamGonzalez1996) 
* [Jordan Chatman](https://github.com/JordanChat)
* [Tyler Brown](https://github.com/Starcode897)

#### Procedure:
Dependencies were imported. Path to CSV was formed. The data with no internet service was dropped. A label encoder was used for the data. The dataframe was converted to a csv. A correlation matrix was run on the data.

The data with no internet was dropped, leaving only two internet options. Multiple lines data was dropped because of multicollinearity with the phone service data. Contracts or payment methods were not included because of multiple options. The first model was run, where there was an R squared of 0.98, and a mean squared error of 5.

For our second model, we dropped the internet service DSL variable due to multicollinearity. For our third model, we dropped the paperless billing variable to see how this would impact our model. For our fourth model, we started dropping random variables to see if the R squared would go down, and to see how the mean squared error would change. For our fifth model, we ended up dropping characteristics.

Our final model had fifteen variables. Monthly charges was on the y axis. 20 percent of the data was put in the test set. 80 percent of the data was put in the training set. A linear regression model was formed. The model was fit to the training data. The scores for the training data and the testing data were calculated.

The training score and testing score were both 0.99. The mean squared error was 5.59. The R squared was 0.98. The intercept and coefficient was printed. The coefficients made sense, which was checked by the coefficient for the phone service being 22, which means that for each “Yes”, the monthly price would increase by 22 dollars, which makes sense. 
A predictions model was formed. The residuals were plotted for the training data and the testing data. The VIF scores were looked at for multicollinearity. A standard scaler was used. The model was saved as a pickle file. 


### [Project Presentation!](https://docs.google.com/presentation/d/1aZsKhIUplQxirxhCHY3ZwdMNveFSOaMW4jF4jsQmDYk/edit?ts=603ed6cb#slide=id.p)

#Data Sources:
### [Kaggle Data Set](https://www.kaggle.com/radmirzosimov/telecom-users-dataset)


##### Question to answer:
What should user be paying for their telecom services?

## Residual

![residual_plot](https://github.com/Starcode897/final-project-TELECOM/blob/main/static/img/residuals.png)

## Telecom
![telecom_pic](https://github.com/Starcode897/final-project-TELECOM/blob/main/static/img/telecom.jpg)

##### Methods:
First, we got the values from the survey and inserted that data into an array.
Then, we input that array to the model using the predict method.
Next, we converted the resulting index into a float in USD Money Format.
Finally,  we returned this output to the ‘outcome.html’ to display the result on our website.

## Calculator
![calculator_pic](https://github.com/Starcode897/final-project-TELECOM/blob/main/static/img/calculatehtml.png)

## Index
![index_pic](https://github.com/Starcode897/final-project-TELECOM/blob/main/static/img/indexhtml.png)

## Machine Learning
![machine_learning_pic](https://github.com/Starcode897/final-project-TELECOM/blob/main/static/img/machinelearninghtml.png)

## Outcome
![outcome_pic](https://github.com/Starcode897/final-project-TELECOM/blob/main/static/img/outcomehtml.png)


Heroku APP:
https://calm-headland-26707.herokuapp.com/
