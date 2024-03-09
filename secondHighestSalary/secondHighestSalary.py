'''

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

'''

import pandas as pd

def second_highest_salary(employee):
    sorted_by_salary = employee["salary"].drop_duplicates().sort_values(ascending=False)
    return pd.DataFrame({"SecondHighestSalary": [None if sorted_by_salary.size < 2 else sorted_by_salary.iloc[1]]})


data = pd.read_csv("data.csv")
print(second_highest_salary(pd.DataFrame(data)))


'''
-- Write your PostgreSQL query statement below

SELECT (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1
    OFFSET 1
) AS SecondHighestSalary;
'''