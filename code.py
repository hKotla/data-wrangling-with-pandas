# --------------
import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.

df = pd.read_csv(path, delimiter=';')

# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows
df.replace('unknown', np.nan, inplace = True)

# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 
df.rename({'loan':'previous_loan_status', 'y':'loan_status'}, axis=1, inplace=True)

# Find out the information of the `job` column.
df['job'].describe()

# Check the `loan_status`  approval rate by `job`
df.groupby('job').loan_status.value_counts(normalize=True).round(4)*100

# Check the percentage of loan approved by `education`
df[df.loan_status == 'yes'].education.value_counts(normalize = True).round(4)*100

# Check the percentage of loan approved by `previous loan status`
df.groupby('previous_loan_status').loan_status.value_counts(normalize = True).round(3)*100

# Create a pivot table between `loan_status` and `marital ` with values form `age`
df.pivot_table(index = 'loan_status', values = 'age', columns = 'marital').round(2)

# Loan status based on marital status whose status is married
df[df.marital == 'married'].loan_status.value_counts()

#Create a  Dataframes 

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 
df_branch_1 = pd.DataFrame({'customer_id': ['CID001', 'CID002'],
                           'first_name': ['Adam','Brain'],
                           'last_name': ['Scott','Lee']})

# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value
df_branch_2 = pd.DataFrame({'customer_id': ['CID003', 'CID004'],
                           'first_name': ['Krish','Anand'],
                           'last_name': ['Kumar','Rao']})

# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value
df_credit_score = pd.DataFrame({'customer_id': ['CID001', 'CID002', 'CID003', 'CID004'],
                               'score': [675,712,779,403]})

# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows
df_new = pd.concat([df_branch_1, df_branch_2], axis=0)

# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key
pd.merge(df_new, df_credit_score, on = 'customer_id')



