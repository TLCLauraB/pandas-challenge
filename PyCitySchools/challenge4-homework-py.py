#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
import os
from pathlib import Path


# In[2]:


# From Assignment:
# Hint: Check out the sample solution called PyCitySchools_starter.ipynb located in the .zip file to review the desired format for this assignment.
# https://courses.bootcampspot.com/courses/3876/assignments/58093?module_item_id=1017229

# Starter prompts from the provided PyCitySchools_starter.ipynb

# File to Load
school_data_to_load = Path("../Resources/schools_complete.csv")
student_data_to_load = Path("../Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[3]:


## District Summary


# In[4]:


# Test for Success (Info Gathering)

# Header names of the school_data (easeir for me to read this way)
for column in school_data.columns:
    print(column)


# In[5]:


# Test for Success (Info Gathering)

# Header names of the student_data (easeir for me to read this way)
for column in student_data.columns:
    print(column)


# In[6]:


# What the homework is asking for

# Calculate the total number of unique schools
school_count = school_data_complete['school_name'].nunique()

print(f"There are {school_count} schools.")


# In[7]:


# Calculate the total number of students
student_count = school_data_complete['student_name'].count()

print(f"There are {student_count} students total.")


# In[8]:


# Calculate the total budget
total_budget = school_data['budget'].sum()

print(f"Total budget: ${total_budget}")


# In[9]:


# Calculate the average (mean) math score
average_math_score = student_data['math_score'].mean()

print(f"The average math score across all schools is: {average_math_score}")
print(f"The (rounded) average math score across all schools is: {average_math_score:.2f}")


# In[10]:


# Calculate the average (mean) reading score
average_reading_score = student_data['reading_score'].mean()

print(f"The average math score across all schools is: {average_reading_score}")
print(f"The (rounded) average math score across all schools is: {average_reading_score:.2f}")


# In[11]:


# Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70)
passing_math_count = school_data_complete[(school_data_complete["math_score"] >= 70)].count()["student_name"]
passing_math_percentage = passing_math_count / float(student_count) * 100

print(f"Percentage of Students who passed Math Class: {passing_math_percentage}%")
print(f"Percentage of Students who passed Math Class, rounded: {passing_math_percentage:.2f}%")


# In[12]:


# Calculate the percentage of students who passed reading (hint: look at how the math percentage was calculated)  
passing_reading_count = school_data_complete[(school_data_complete["reading_score"] >= 70)].count()["student_name"]
passing_reading_percentage = passing_reading_count / float(student_count) * 100

print(f"Percentage of Students who passed Reading Class: {passing_reading_percentage}%")
print(f"Percentage of Students who passed Reading Class, rounded: {passing_reading_percentage:.2f}%")


# In[13]:


# Use the following to calculate the percentage of students that passed math and reading
passing_math_reading_count = school_data_complete[
    (school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70)
].count()["student_name"]

overall_passing_rate = passing_math_reading_count /  float(student_count) * 100

print(f"Percentage of students that passed both math and reading: {overall_passing_rate}%")
print(f"Percentage of students that passed both math and reading, rounded: {overall_passing_rate:.2f}%")


# In[14]:


# Create a dictionary of the listed metrics
district_summary_dict = {'Total Schools': school_count,
                         'Total Students': student_count,
                         'Total Budget': total_budget,
                         'Average Math Score': average_math_score,
                         'Average Reading Score': average_reading_score,
                         '% Passing Math': passing_math_percentage,
                         '% Passing Reading': passing_reading_percentage,
                         '% Overall Passing': overall_passing_rate
}


# Test for Success
district_summary_dict


# In[15]:


# Creating a DataFrame from the dictionary
district_summary = pd.DataFrame(district_summary_dict, index=[0])

# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format)

# Display the DataFrame
district_summary


# In[16]:


## School Summary


# In[17]:


# Use the code provided to select all of the school types
# DEBUGGING school_types = school_data_complete["type"].unique()
school_types = school_data_complete.groupby("school_name")["type"].first()

print(f"These are the Type of schools: {school_types}")


# In[18]:


# DEBUGGING - List the school name and type for each school

# school_name_and_type = school_data_complete.groupby("school_name")["type"].first()
# print(school_name_and_type)


# In[19]:


# List the school name and type for each school
school_name = school_data_complete["school_name"].unique()

print(school_name)


# In[20]:


# Calculate the total student count per school
per_school_counts = school_data_complete["school_name"].value_counts()

per_school_counts


# In[21]:


# Calculate the total school budget and per capita spending per school
# per_school_budget = school_data_complete.groupby(["school_name"]).mean()["budget"]

# per_school_capita = per_school_budget / per_school_counts

# Tried this version, got the following error message:
# C:\Users\TLCLa\AppData\Local\Temp\ipykernel_20968\526294201.py:2: FutureWarning: The default value of numeric_only in DataFrameGroupBy.mean is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.
# per_school_budget = school_data_complete.groupby(["school_name"]).mean()["budget"]


# In[22]:


# New Version: 

# Calculate the total school budget and per capita spending per school
per_school_budget = school_data_complete.groupby(["school_name"]).mean(numeric_only=True)["budget"]

per_school_capita = per_school_budget / per_school_counts


# In[23]:


# Test for success
per_school_budget


# In[24]:


# Test for success
per_school_counts


# In[25]:


# Test for success
per_school_capita


# In[26]:


# Calculate the average test scores per school
per_school_math = school_data_complete.groupby(["school_name"]).mean(numeric_only=True)["math_score"]

per_school_reading = school_data_complete.groupby(["school_name"]).mean(numeric_only=True)["reading_score"]


# In[27]:


# Test for success
per_school_math


# In[28]:


# Test for success
per_school_reading


# In[29]:


# Calculate the number of students per school with math scores of 70 or higher
students_passing_math = school_data_complete[school_data_complete["math_score"] >= 70]

school_students_passing_math = students_passing_math.groupby(["school_name"]).count()["student_name"]


# In[30]:


# Test for success
students_passing_math


# In[31]:


# Test for success
school_students_passing_math


# In[32]:


# Calculate the number of students per school with reading scores of 70 or higher
students_passing_reading = students_passing_reading = school_data_complete[school_data_complete["reading_score"] >= 70]

school_students_passing_reading = students_passing_reading.groupby(["school_name"]).count()["student_name"]


# In[33]:


# Test for success
students_passing_reading


# In[34]:


# Test for success
school_students_passing_reading


# In[35]:


# Use the provided code to calculate the number of students per school that passed both math and reading with scores of 70 or higher
students_passing_math_and_reading = school_data_complete[
    (school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)
]
school_students_passing_math_and_reading = students_passing_math_and_reading.groupby(["school_name"]).size()


# In[36]:


# Test for success
school_students_passing_math_and_reading


# In[37]:


# Use the provided code to calculate the passing rates
per_school_passing_math = school_students_passing_math / per_school_counts * 100
per_school_passing_reading = school_students_passing_reading / per_school_counts * 100
overall_passing_rate = school_students_passing_math_and_reading / per_school_counts * 100


# In[38]:


# Test for success
per_school_passing_math


# In[39]:


# Test for success
per_school_passing_reading


# In[40]:


# Test for success
overall_passing_rate


# In[41]:


# Create a DataFrame called `per_school_summary` with columns for the calculations above.

# Create a dictionary of the listed metrics
per_school_summary_dict = {'School Type': school_types,
                           'Total Students': per_school_counts,
                           'Total School Budget': per_school_budget,
                           'Per Student Budget': per_school_capita,
                           'Average Math Score': per_school_math,
                           'Average Reading Score': per_school_reading,
                           '% Passing Math': per_school_passing_math,
                           '% Passing Reading': per_school_passing_reading,
                           '% Overall Passing': overall_passing_rate
}

# Test for success
per_school_summary_dict


# In[42]:


# DEBUGGING - What is the length of each array

# for key, value in per_school_summary_dict.items():
#    print(f"{key}: {len(value)}")


# In[43]:


# Creating a DataFrame from the dictionary
per_school_summary = pd.DataFrame(per_school_summary_dict)


# In[44]:


# Formatting
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)


# In[45]:


# Display the DataFrame
per_school_summary


# In[46]:


## Highest-Performing Schools (by % Overall Passing)


# In[47]:


# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
top_schools = per_school_summary.sort_values(by='% Overall Passing', ascending=False)
top_schools = top_schools[['School Type', 'Total Students', 'Total School Budget', 'Per Student Budget', 'Average Math Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall Passing']]
top_schools.head(5)


# In[48]:


## Bottom Performing Schools (By % Overall Passing)


# In[49]:


# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
bottom_schools = per_school_summary.sort_values(by='% Overall Passing', ascending=True)
bottom_schools = bottom_schools[['School Type', 'Total Students', 'Total School Budget', 'Per Student Budget', 'Average Math Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall Passing']]
bottom_schools.head(5)


# In[50]:


## Math Scores by Grade


# In[51]:


# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]


# In[52]:


# Test for success
ninth_graders
tenth_graders
eleventh_graders
twelfth_graders


# In[53]:


# Group by `school_name` and take the mean of the `math_score` column for each.
# ninth_grade_math_scores = school_data_complete[school_data_complete["grade"] == "9th"].groupby("school_name").mean()["math_score"]
# tenth_grade_math_scores = school_data_complete[school_data_complete["grade"] == "10th"].groupby("school_name").mean()["math_score"]
# eleventh_grade_math_scores = school_data_complete[school_data_complete["grade"] == "11th"].groupby("school_name").mean()["math_score"]
# twelfth_grade_math_scores = school_data_complete[school_data_complete["grade"] == "12th"].groupby("school_name").mean()["math_score"]

# FutureWarning: The default value of numeric_only in DataFrameGroupBy.mean is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.


# In[54]:


# Second attempt

# Group by `school_name` and take the mean of the `math_score` column for each.
ninth_grade_math_scores = school_data_complete[school_data_complete["grade"] == "9th"].groupby("school_name").mean(numeric_only=True)["math_score"]
tenth_grade_math_scores = school_data_complete[school_data_complete["grade"] == "10th"].groupby("school_name").mean(numeric_only=True)["math_score"]
eleventh_grade_math_scores = school_data_complete[school_data_complete["grade"] == "11th"].groupby("school_name").mean(numeric_only=True)["math_score"]
twelfth_grade_math_scores = school_data_complete[school_data_complete["grade"] == "12th"].groupby("school_name").mean(numeric_only=True)["math_score"]


# In[55]:


# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
math_scores_by_grade = pd.DataFrame({"9th": ninth_grade_math_scores,
                                     "10th": tenth_grade_math_scores,
                                     "11th": eleventh_grade_math_scores,
                                     "12th": twelfth_grade_math_scores
})


# In[56]:


# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
math_scores_by_grade


# In[57]:


## Reading Score by Grade 


# In[58]:


# Do I need to do this again if it's already done and defined?

# Use the code provided to separate the data by grade
# ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
# tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
# eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
# twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]


# In[59]:


# Group by `school_name` and take the mean of the the `reading_score` column for each.

ninth_grade_reading_scores = school_data_complete[school_data_complete["grade"] == "9th"].groupby("school_name").mean(numeric_only=True)["reading_score"]

tenth_grade_reading_scores = school_data_complete[school_data_complete["grade"] == "10th"].groupby("school_name").mean(numeric_only=True)["reading_score"]

eleventh_grader_reading_scores = school_data_complete[school_data_complete["grade"] == "11th"].groupby("school_name").mean(numeric_only=True)["reading_score"]

twelfth_grade_reading_scores = school_data_complete[school_data_complete["grade"] == "12th"].groupby("school_name").mean(numeric_only=True)["reading_score"]


# In[60]:


# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = pd.DataFrame({"9th": ninth_grade_reading_scores,
                                        "10th": tenth_grade_reading_scores,
                                        "11th": eleventh_grader_reading_scores,
                                        "12th": twelfth_grade_reading_scores
})


# In[61]:


# Minor data wrangling
reading_scores_by_grade = reading_scores_by_grade[["9th", "10th", "11th", "12th"]]
reading_scores_by_grade.index.name = None

# Display the DataFrame
reading_scores_by_grade


# In[62]:


## Scores by School Spending


# In[63]:


# Establish the bins 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]


# In[64]:


# Create a copy of the school summary since it has the "Per Student Budget" 
school_spending_df = per_school_summary.copy()


# In[65]:


# Test for success
school_spending_df


# In[66]:


# DEBUGGING - I do not understand why it will not accept < or $ when that is what is provided

# Use `pd.cut` to categorize spending based on the bins.
# school_spending_df["Spending Ranges (Per Student)"] = pd.cut(school_spending_df["Per Student Budget"], bins=spending_bins, labels=labels)

# school_spending_df

# Cell In[88], line 2
#      1 # Use `pd.cut` to categorize spending based on the bins.
#----> 2 school_spending_df["Spending Ranges (Per Student)"] = pd.cut(school_spending_df["Per Student Budget"], bins=spending_bins, labels=labels)
#      4 school_spending_df

#File ~\anaconda3\envs\dev\lib\site-packages\pandas\core\reshape\tile.py:293, in cut(x, bins, right, labels, retbins, precision, include_lowest, duplicates, ordered)
#    290     if (np.diff(bins.astype("float64")) < 0).any():
#    291         raise ValueError("bins must increase monotonically.")
#--> 293 fac, bins = _bins_to_cuts(
#    294     x,
#    295     bins,
#    296     right=right,
#    297     labels=labels,
#    298     precision=precision,
#    299     include_lowest=include_lowest,
#    300     dtype=dtype,
#    301     duplicates=duplicates,
#    302     ordered=ordered,
#    303 )
#    305 return _postprocess_for_cut(fac, bins, retbins, dtype, original)
#
#File ~\anaconda3\envs\dev\lib\site-packages\pandas\core\reshape\tile.py:428, in _bins_to_cuts(x, bins, right, labels, precision, include_lowest, dtype, duplicates, ordered)
#   425         bins = unique_bins
#    427 side: Literal["left", "right"] = "left" if right else "right"
#--> 428 ids = ensure_platform_int(bins.searchsorted(x, side=side))
#    430 if include_lowest:
#    431     ids[np.asarray(x) == bins[0]] = 1
#
#TypeError: '<' not supported between instances of 'int' and 'str'


# In[67]:


# DEBUGGING

# This is the solution I created using .str.repace. It's working Harder, not Smarter (tm).

# Create a temporary column with numeric values for categorization - this is annoying
# school_spending_df["Per Student Budget Numeric"] = school_spending_df["Per Student Budget"].str.replace('[\$\,]', '', regex=True).astype(float)

# Use `pd.cut` to categorize spending based on the bins.
# school_spending_df["Spending Ranges (Per Student)"] = pd.cut(school_spending_df["Per Student Budget Numeric"], bins=spending_bins, labels=labels)

# Drop the temporary column
# school_spending_df = school_spending_df.drop("Per Student Budget Numeric", axis='columns')

# school_spending_df


# In[68]:


# This is Katy Yelle's solution, which is MUCH more efficent/ellegant than my own

# Use `pd.cut` to categorize spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels=labels)

school_spending_df


# In[69]:


#  Calculate averages for the desired columns. 
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Math Score"].mean()
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Math"].mean()
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Overall Passing"].mean()


# In[70]:


# Assemble into DataFrame
spending_summary = pd.DataFrame({"Average Math Score": spending_math_scores,
                                 "Average Reading Score": spending_reading_scores,
                                 "% Passing Math": spending_passing_math,
                                 "% Passing Reading": spending_passing_reading,
                                 "% Overall Passing": overall_passing_spending
})


spending_summary


# In[71]:


## Scores by School Size


# In[72]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels2 = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[73]:


# Categorize the spending based on the bins
# Use `pd.cut` on the "Total Students" column of the `per_school_summary` DataFrame.
per_school_summary["School Size"] = pd.cut(per_school_summary["Total Students"], size_bins, labels=labels2)

per_school_summary


# In[74]:


# Calculate averages for the desired columns. 
size_math_scores = per_school_summary.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = per_school_summary.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = per_school_summary.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = per_school_summary.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = per_school_summary.groupby(["School Size"])["% Overall Passing"].mean()


# In[75]:


# Test for success
size_math_scores
size_reading_scores
size_passing_math
size_passing_reading
size_overall_passing


# In[76]:


# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`

size_summary = pd.DataFrame({"Average Math Score": size_math_scores,
                             "Average Reading Score": size_reading_scores,
                             "% Passing Math": size_passing_math,
                             "% Passing Reading": size_passing_reading,
                             "% Overall Passing": size_overall_passing
})

# Display results
size_summary


# In[77]:


## Scores by School Type


# In[78]:


# Group the per_school_summary DataFrame by "School Type" and average the results.
average_math_score_by_type = per_school_summary.groupby(["School Type"])["Average Math Score"].mean()
average_reading_score_by_type = per_school_summary.groupby(["School Type"])["Average Reading Score"].mean()
average_percent_passing_math_by_type = per_school_summary.groupby(["School Type"])["% Passing Math"].mean()
average_percent_passing_reading_by_type = per_school_summary.groupby(["School Type"])["% Passing Reading"].mean()
average_percent_overall_passing_by_type = per_school_summary.groupby(["School Type"])["% Overall Passing"].mean()


# In[79]:


# Assemble the new data by type into a DataFrame called `type_summary`
type_summary = pd.DataFrame({"Average Math Score": average_math_score_by_type,
                             "Average Reading Score": average_reading_score_by_type,
                             "% Passing Math": average_percent_passing_math_by_type,
                             "% Passing Reading": average_percent_passing_reading_by_type,
                             "% Overall Passing": average_percent_overall_passing_by_type
})

# Display results
type_summary


# In[ ]:




