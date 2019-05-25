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

#####Concantination
# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1, uber2, uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())

# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())

####find files
# Import necessary modules
import glob
import pandas as pd

# Write the pattern: pattern
pattern = '*.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Print the file names
print(csv_files)

# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])

# Print the head of csv2
print(csv2.head())
##################
# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:
    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)

    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())

#merging databases
# Merge the DataFrames: o2o from http://swcarpentry.github.io/sql-novice-survey/07-join/index.html
o2o = pd.merge(left=site, right=visited, left_on="name", right_on="site")

# Print o2o
print(o2o)

#In a many-to-one (or one-to-many) merge, one of the values will be duplicated
# and recycled in the output. That is, one of the keys in the merge is not unique.
# Merge the DataFrames: m2o
m2o = pd.merge(left=site, right=visited, left_on="name", right_on="site")

# Print m2o
print(m2o)

###########data types
#Numeric dtype loaded as object says that there is a problem with missing data
#use category dtype for categories: less memory and special methods
# Convert the sex column to type 'category'
tips.sex = tips.sex.astype("category")

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype("category")

# Print the info of tips
print(tips.info())

###You can use the pd.to_numeric() function to convert a column into a numeric data type.
# If the function raises an error, you can be sure that there is a bad value within the column.
# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips["total_bill"], errors="coerce")

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips["tip"], errors="coerce")

# Print the info of tips
print(tips.info())

###############When performing pattern matching on data,
# since the pattern will be used for a match across multiple rows,
# it's better to compile the pattern first using re.compile(),
# and then use the compiled pattern to match values.

# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result = prog.match('1123-456-7890')
print(bool(result))

# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)

# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Use \$ to match the dollar sign, \d* to match an arbitrary number of digits, \.
#  to match the decimal point, and \d{x} to match x number of digits.
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

#Use [A-Z] to match any capital letter followed by \w* to match an arbitrary
# number of alphanumeric characters.
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)


# Define recode_sex()
def recode_sex(sex_value):
    # Return 1 if sex_value is 'Male'
    if sex_value == "Male":
        return 1

    # Return 0 if sex_value is 'Female'
    elif sex_value == "Female":
        return 0

    # Return np.nan
    else:
        return np.nan


# Apply the function to the sex column
tips['sex_recode'] = tips.sex.apply(recode_sex)

# Print the first five rows of tips
print(tips.head())

# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())


##Dropping duplicate data

# Create the new DataFrame: tracks
tracks = billboard[["year", "artist", "track", "time"]]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())

###########Filling missing data
# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality.Ozone.fillna(oz_mean)

# Print the info of airquality
print(airquality.info())


############Testing your data with asserts
# The .all() method returns True if all values are True.
# When used on a DataFrame, it returns a Series of Booleans -
# one for each column in the DataFrame. So if you are using it on a DataFrame,
# like in this exercise, you need to chain another .all() method so
# that you return only one True or False value. When using these within an assert statement,
#  nothing will be returned if the assert statement is true: This is how you can confirm that
#  the data you are checking are valid.

# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()
######################################################Case study
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
g1800s.plot(kind="scatter", x="1800", y="1899")

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
assert g1800s.columns[0] == "Life expectancy"

# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
assert g1800s['Life expectancy'].value_counts()[0] == 1

# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s, g1900s, g2000s])

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())

# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(gapminder, id_vars = "Life expectancy")
gapminder_melt.columns = ["country", "year", "life_expectancy"]

# Print the head of gapminder_melt
print(gapminder_melt.head())


# Convert the year column to numeric
gapminder.year = pd.to_numeric(gapminder.year)

# Test if country is of type object
assert gapminder.country.dtypes == np.object

# Test if year is of type int64
assert gapminder.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64

#######################
# Create the series of countries: countries
countries = gapminder["country"]

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~countries.str.contains(pattern)

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)

# Assert that country does not contain any missing values
assert pd.notnull(gapminder.country).all()

# Assert that year does not contain any missing values
assert pd.notnull(gapminder.year).all()

# Drop the missing values
gapminder = gapminder.dropna()

# Print the shape of gapminder
print(gapminder.shape)

# Add first subplot
plt.subplot(2, 1, 1)

# Create a histogram of life_expectancy
gapminder.life_expectancy.plot(kind="hist")

# Group gapminder: gapminder_agg
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot()

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()

# Save both DataFrames to csv files
gapminder.to_csv("gapminder.csv")
gapminder_agg.to_csv("gapminder_agg.csv")
