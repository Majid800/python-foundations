# Database

This folder contains the SQL scripts used to create and populate the PostgreSQL database for the Library Management project.

## Files

### schema.sql

Creates the database structure, including the `books` table, columns, data types, and constraints required by the application.

### sample_data.sql

Populates the `books` table with sample records for development, testing, and demonstration purposes.

## Setup

1. Create a PostgreSQL database named `library_management`.
2. Execute `schema.sql` to create the database schema.
3. Execute `sample_data.sql` to insert the sample book records.
4. Run the Python application.

## Purpose

These scripts allow the database to be recreated quickly on any machine, making the project easy to set up, test, and maintain.