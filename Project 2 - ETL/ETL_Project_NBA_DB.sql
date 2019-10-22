DROP TABLE Player_Info;

--Create tables for raw data to be loaded into
CREATE TABLE Player_Info (

Rk INT PRIMARY KEY, 
Player TEXT, 
Tm TEXT, 
Salary_2019To2020 TEXT, 
Salary_2020To2021 TEXT,
Salary_2021To2022 TEXT, 
Salary_2022To2023 TEXT, 
Salary_2023To2024 TEXT,
Salary_2024To2025 TEXT, 
Signed_Using TEXT, 
Guaranteed TEXT, 
year_start INT,
position TEXT, 
height TEXT, 
weight FLOAT, 
birth_date TEXT, 
college TEXT, 
AGE INT, 
GP INT,
W INT, 
L INT, 
MIN FLOAT, 
PTS FLOAT, 
FGM FLOAT, 
FGA FLOAT, 
FG_prc FLOAT, 
Three_pnt_m FLOAT, 
Three_pnt_a FLOAT, 
Three_pnt_prc FLOAT, 
FTM FLOAT,
FTA FLOAT, 
FT_prc FLOAT, 
OREB FLOAT, 
DREB FLOAT, 
REB FLOAT, 
AST FLOAT, 
TOV FLOAT, 
STL FLOAT, 
BLK FLOAT,
Plusminus FLOAT
);

SELECT * FROM Player_Info;