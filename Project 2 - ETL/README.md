![NBA_Logo](NBA_Logo.jpg)

# NBA Player Query

Our group decided to extract data for NBA players salaries, stats and basic information for the 2018-2019 season.
In the `NBA_19` database, we wanted to provide users with the ability to compare **statistics, player dynamics and the salaries for the following season(s)**.

## Getting Started

### Gathering Data
During our search for information, we found two separate sources including *Kaggle* and *Basketball-Reference*.
1. NBA Players statistics since 1950  
https://www.kaggle.com/drgilermo/nba-players-stats
2. 2019-20 NBA Player Contracts and Salary information   
https://www.basketball-reference.com/contracts/players.html
3. 2018-2019 NBA Players Statistics   
https://www.kaggle.com/terrycheng/2018-nba-players-stats

### Putting the Data Together
After collecting the desired data from both sources, the next step was to use **Jupyter Notebook** to manipulate and *join* the data sets together into *one* database.
- steps within the Jupyter Notebook included importing files, reading files, merging tables, changing column names, removing some columns, and changing all column names to all lower case letters in order to smoothly connect with **PostgreSQL**.

### Importing to PostgreSQL (pgAdmin)
Once the tables were merged on Jupyter Notebook, we finally created a **Database** and **Table** within pgAdmin and inserted each **column name** and its **datatype**.

### Finally
To insert the data from *Jupyter* to *pgAdmin*, we created a connection to the local host server, created an engine, opened the table, and imported the data. 

### Authors
- Melissa Djohan
- Tyler Fasulo
- Luan Hajnaj
- Limei Hou
