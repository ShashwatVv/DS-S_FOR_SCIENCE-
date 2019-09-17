


get_ipython().run_line_magic('autosave', '5')



import pandas as pd
import numpy as np

##Read csv file as DataFrame
data = pd.read_csv("HR-Employee-Attrition.csv", index_col='EmployeeNumber')




# Access index of DataFrame
data.index


# Access columns of DataFrame
data.columns



data.values


# # Operations and manipulations
# ## Inspection of data



data['Age'].head()

data[['Age', 'Gender', 'YearsAtCompany']].head()



# Add column to DataFrame
data['AgeInMonths'] = data['Age'] * 12
data['AgeInMonths'].head()





data.drop('AgeInMonths', axis=1, inplace=True)

data.drop("EmployeeCount",axis=1, inplace=True)


data[['Department', 'EducationField']][4:8]




# Total employees by department
data['Department'].value_counts()


# Overall attrition rate
normalized_count = data['Attrition'].value_counts(normalize=True)
normalized_count


normalized_count['Yes']



# Average hourly rate
data['HourlyRate'].mean()


# Average number of years
data['YearsAtCompany'].describe()


# Employees with the most number of years
data['YearsAtCompany'].sort_values(ascending=False)[:5]




# Overall employee satisfaction
job_satisfaction_dict = {
    1: 'Low',
    2: 'Medium',
    3: 'High',
    4: 'Very High'
}




data['JobSatisfaction'] = data['JobSatisfaction'].map(job_satisfaction_dict)
data['JobSatisfaction'].head()

data['JobSatisfaction'].value_counts(normalize=True)


# In[ ]:




# Employees with Low Job Satisfaction
data['JobSatisfaction'] == 'Low'




data.loc[data['JobSatisfaction'] == 'Low'].index





# Employees with both Low Job Satisfaction and Job Involvement
job_involvement_dict = {
    1: 'Low',
    2: 'Medium',
    3: 'High',
    4: 'Very High'
}

data['JobInvolvement'] = data['JobInvolvement'].map(job_involvement_dict)



data.loc[(data['JobSatisfaction'] == 'Low') & (data['JobInvolvement'] == 'Low')].index


 


# Employee comparison
## Create new DataFrame with observations of interest
subset = data.loc[(data['JobSatisfaction'] == 'Low') | (data['JobSatisfaction'] == 'Very High')]
print('Shape: ', subset.shape)
print('\nJob Satisfaction Count')
print(subset['JobSatisfaction'].value_counts())





## Split DataFrame by 'JobSatisfaction'
grouped = subset.groupby('JobSatisfaction')

## View groups in GroupBy object
grouped.groups





## View details of Low group
grouped.get_group('Low').head()




## Get summary statistics for age for each group
grouped['Age'].describe()




## Get employee count per department for each group
grouped['Department'].value_counts(normalize=True) * 100





grouped['Department'].value_counts(normalize=True).unstack() * 100



