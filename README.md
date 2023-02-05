# SQL Challenge - Pewlett Hackard

## Introduction
You have been hired as a new data engineer at Pewlett Hackard, a fictional company. Your first major task is to do a research project about the employees who were employed by the company during the 1980s and 1990s. The only remaining information about the employees from that period are six CSV files.

## Objectives
The objective of this project is to design tables to hold the data from the CSV files, import the CSV files into a SQL database, and then answer questions about the data. This project involves performing data modelling, data engineering, and data analysis.

## Files
The .csv files are available in the resouces folder.

## The challenge is divided into three parts:
- Data Modelling
- Data Engineering
- Data Analysis

## Data Modelling
See ERD sketch of the tables creates using QuickDBD.

## Data Engineering
Created a table schema for each of the six CSV files.
Specified the data types, primary keys, foreign keys, and other constraints.
For the primary keys, verifies that the column is unique. If not, create a composite key.
Create the tables in the correct order to handle the foreign keys.
Import each CSV file into its corresponding SQL table.

## Data Analysis
List the employee number, last name, first name, sex, and salary of each employee.
List the first name, last name, and hire date for the employees who were hired in 1986.
List the manager of each department along with their department number, department name, employee number, last name, and first name.
List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
List the first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
List each employee in the Sales department, including their employee number, last name, and first name.
List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.
List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).
