Dataset:
The dataset is of insurance company, which shows the medical expenses of a person and the traits that defines his/her expenditure rate such as age, sex, bmi, smoking habit, and children. The more spending on the medical expense (>30,000) shows a good chance that the person will purchase a medical insurance.

Model:
The model used for the training of data is the Logistics Regression as the results are in either Yes / No or 0s / 1s.

Steps followed:
1.	Data Set with different domains
2.	Read the Data frame using pandas in python
3.	Split Data it in 80/20 using random (train train split function makes it random unless random_state parameter is used)
4.	Train the classifier on the 80 sliced data
5.	Evaluate the classifier on the 20 sliced data and share accuracy - max 3 domains are okay
6.	Using this .py of above in Eclipse IDE and then connecting the micro web framework of Flask to show results (accuracy) in a web app.
