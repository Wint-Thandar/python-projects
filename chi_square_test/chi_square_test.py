# install the required python libraries
import pandas as pd
from scipy.stats import chi2_contingency, chi2

# import campaign data
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name = "campaign_data")

# remove customers who were in the control group
campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]

# specify hypotheses & acceptance criteria for test
null_hypothesis = "No relationship between mailer type and signup rate. They are independent."
alternate_hypothesis = "Relationship exists between mailer type and signup rate. They are not independent." 
acceptance_criteria = 0.05

# aggregate data to get observed values
observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values

# run the chi-square test
chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction = False)

# print chi-square statistic
print(chi2_statistic)

# print p-value
print(p_value)

# find the critical value of the test
critical_value = chi2.ppf(1 - acceptance_criteria, dof)

# print critical value
print(critical_value)

# print the results (based on p-value)
if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else: 
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")

# print the results (based on chi-square statistic)
if chi2_statistic >= critical_value:
    print(f"As our chi-square statistic of {chi2_statistic} is higher than our critical value of {critical_value} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else: 
    print(f"As our chi-square statistic of {chi2_statistic} is lower than our critical value of {critical_value} - we retain the null hypothesis, and conclude that: {null_hypothesis}")
