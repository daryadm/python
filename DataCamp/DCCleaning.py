# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())
####################################

# Print the info of df
print(df.info()) #The .info() method provides important information about a DataFrame,
# such as the number of rows, number of columns, number of non-missing values in each column,
# and the data type stored in each column

# .describe() method to calculate summary statistics of your data.

#############Frequency counts for categorical data
#You want to set the dropna column to False
# so if there are missing values in a column, it will give you the frequency counts.

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False)) #if column name is no-space lower case, I could use .borough

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

##############################
######Visualizing single variables with histograms
#The .plot() method allows you to create a plot of each column of a DataFrame.
# The kind parameter allows you to specify the type of plot to use - kind='hist',
# for example, plots a histogram.
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()
#####Visualizing multiple variables with boxplots
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df.boxplot(column="initial_cost", by="Borough", rot=90)

# Display the plot
plt.show()

#############################Visualizing multiple variables with scatter plots
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
df.plot(kind="scatter", x="initial_cost", y="total_est_fee", rot=70)
plt.show()

###########Tidy Data
#describe
#head
#value_counts
#viz
############Reshaping your data using melt
#Melting data is the process of turning columns of your data into rows of data.

#pd.melt(). There are two parameters you should be aware of: id_vars and value_vars.
# The id_vars represent the columns of the data you do not want to melt
# (i.e., keep it in its current shape), while
# the value_vars represent the columns you do wish to melt into rows.
# By default, if no value_vars are provided, all columns not set in the id_vars will be melted.
# This could save a bit of typing, depending on the number of columns that need to be melted.
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=["Month", "Day"])

# Print the head of airquality_melt
print(airquality_melt.head())
##############
#You can rename the variable column by specifying an argument to the var_name parameter,
# and the value column by specifying an argument to the value_name parameter.

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt

airquality_melt = pd.melt(airquality, id_vars=["Month", "Day"], var_name="measurement", value_name="reading")

# Print the head of airquality_melt
print(airquality_melt.head())

################Pivot: un-melting data
#While melting takes a set of columns and turns it into a single column,
# pivoting will create a new column for each unique value in a specified column.
#.pivot_table() has an index parameter which you can use to specify the columns that
# you don't want pivoted: It is similar to the id_vars parameter of pd.melt().
# Two other parameters that you have to specify are columns (the name of the column
# you want to pivot), and values (the values to be used when the column is pivoted).

# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=["Month", "Day"], columns="measurement", values="reading")

# Print the head of airquality_pivot
print(airquality_pivot.head())

#########################

#########################
##Resetting the index of a DataFrame
#What you got back instead was a pandas DataFrame with a hierarchical index
# (also known as a MultiIndex). There's a very simple method
# you can use to get back the original DataFrame from the pivoted DataFrame: .reset_index().
## Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the new index of airquality_pivot
print(airquality_pivot.index)

# Print the head of airquality_pivot
print(airquality_pivot.head())
################
# Pivot airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=["Month", "Day"],
                                              columns="measurement",
                                              values="reading",
                                              aggfunc=np.mean) #The default aggregation function
# used by .pivot_table() is np.mean(). So you could have pivoted the duplicate values
#  in this DataFrame even without explicitly specifying the aggfunc parameter.

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())

####################Splitting a column with .str
# Melt tb: tb_melt
tb_melt = pd.melt(tb, id_vars=["country", "year"])

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
print(tb_melt.head())

######################
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=["Date", "Day"], var_name="type_country", value_name="counts")

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split("_")

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)