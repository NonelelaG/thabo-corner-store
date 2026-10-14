Thabo's Corner Store - Sales Insights System.

Computational Thinking Plan

Decomposition I will break down the project into smaller parts that are manageable so that it can be easy to build and test them independently. (1). First I will eximine and clean the raw data in product and sales CSV files. (2). Write down the data-cleaning decisions that were made. (3). I will build an SQL database to hold products and sales. (4). Load the the cleaned data and run SQL quiries to get useful business information. (5). Analyse the data using python programming concepts. (6). Make charts that shows revenue and sales trends (virsualization). (7). Make a password protection using SHA-256 hashing. (8). Document the results. (9). Test the full system and prepare the final submission.

Pattern recognition The raw data have several issues concerning data quality. The products data may have missing product names or prices, inconsistent category capitalisation and duplicate entries. The sales data have inconsistant date formats, missing dates and quantities, missing payments methods and duplicate records.

Abstraction I will focus on the information the sales insights system actually needs and split the project into modules: (1). data_cleaning.py - for data cleaning. (2). database.py - for making SQLite and running SQL queries. (3). analysis.py - applying programming logic. (4). visualize.py - for making charts for visualization. (5). security.py - password hashing and access control. main.py - for connecting the modules.

Algorithm

The planned sequence is: (1). Inspect the CSV files for raw data. (2). Create and save this plan. (3). Set up the repository on Git and make an initial project. (4). Load the raw data using python. (5). Clean and fix data. (6). Document the cleaning decisions in the README. (7). Create the SQLite database. (include primary and foreign keys). (8). Insert the cleaned product and sales data in SQLite. (9). Run SQL queries, including joins and aggregation. (10). Analyse the cleaned data using Python functions, loops and conditionals. (11). Make the visualizations. (12). Make a password hashing and access control. (13). Test the system from start to finish. Upload the completed work to github and prepare the final submission files. (14). Submit on Upskill.

Expected Outcome The finished system should turn the store's messy data into useful sales information. It should include cleaned data, a relational SQLite database, SQL query results, Python-based analysis, two visualisations and a basic password-protection mechanism. The final documentation should explain the decisions made and offer useful business insights for Thabo's Corner Store.