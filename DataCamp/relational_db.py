#install like psycopg2 for PostgreSQL, you have to install prior to use.
# Import create_engine
from sqlalchemy import create_engine, Table, MetaData
metadata = MetaData()

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect() #creating connection

# Print table names
print(engine.table_names())
#============================================
# Import Table
from sqlalchemy import Table

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

#============================================

# Reflect the census table from the engine: census
census = Table("census", metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())

# Print full table metadata
print(repr(metadata.tables["census"]))
#====================================================================
# Build select statement for census table: stmt
stmt = "SELECT * from census"

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print Results
print(results)
#=====================================================================

# Import select. It requires a list of tables or columns as the only required argument.
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement and print the results.
# Use the .execute() method on connection with stmt as the argument to retrieve the ResultProxy.
#ResultProxy: The object returned by the .execute() method.
# It can be used in a variety of ways to get the data returned by the query.
# Use .fetchall() on connection.execute(stmt) to retrieve the ResultSet.
#ResultSet: The actual data asked for in the query when using a fetch method
# such as .fetchall() on a ResultProxy.
#This separation between the ResultSet and ResultProxy
# allows us to fetch as much or as little data as we desire.
print(connection.execute(stmt).fetchall())

#===============================================================
# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by using an index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row["state"])

#==============================================================
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://'+'student:datacamp'+ '@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com'+ ':5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())

#===============================================================
#Filter data selected from a Table - Simple
# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York
stmt = stmt.where(census.columns.state == "New York")

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2008
for result in results:
    print(result.age, result.sex, result.pop2008)
#==================================================================
#Filter data selected from a Table - Expressions
# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)
#==================================================================
#Filter data selected from a Table - Advanced
# Import and_
from sqlalchemy import and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == "California",
         census.columns.sex != "M"
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)
#=====================================================================
#Ordering by a Single Column
# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])
#======================================================================
#Ordering in Descending Order by a Single Column
# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by state in descending order: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])
#=====================================================================
#Ordering by Multiple Columns
# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])
#=====================================================================
#Counting Distinct Data
from sqlalchemy import func

# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)

#===================================================================
#Count of Records by State
# Import func
from sqlalchemy import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())

#=============================================================
#Determining the Population Sum by State
# Import func
from sqlalchemy import func


# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label("population")

# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())
#==================================================================
# SQLAlchemy ResultsProxy and Pandas Dataframes

# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)

#================================================================
#From SQLAlchemy results to a Graph
# Import Pyplot as plt from matplotlib
from matplotlib import pyplot as plt


# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)


# Plot the DataFrame
df.plot.bar()
plt.show()

#=========================================================

