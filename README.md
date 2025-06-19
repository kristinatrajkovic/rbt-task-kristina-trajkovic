# rbt-task-kristina-trajkovic
# Real Estate API

This project is a REST API built with Flask for managing real estate listings.  
The API supports property search, viewing, creation, and updates, as well as automatic CSV data import.

## Features

- Retrieve a specific property by its ID
- Search properties using filters (type, square footage, parking, state, estate type)
- Add and update properties (protected with authentication)
- Pagination of search results
- Automated CSV file processing from a staging folder
- Basic Bearer token protection on restricted endpoints

## Technologies Used

- Python & Flask
- PostgreSQL with SQLAlchemy ORM

## Setup Instructions

1.Clone the repository:

```bash
git clone https://github.com/kristinatrajkovic/rbt-task-kristina-trajkovic.git
cd rbt-task-kristina-trajkovic
```
2.Create a .env file with your database credentials:

DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/real_estate

3.Install dependencies:
```bash
pip install -r requirements.txt
```
4.Run the application:
```bash
flask run
```

#### API Usage Examples

GET /properties/123 – Get property by ID

GET /properties/search?min_square_footage=60&parking=true – Filtered search

POST /properties – Add new property (requires Bearer token)

PUT /properties/<id> – Update property info (requires Bearer token)

#### Automated CSV Import
To process a CSV file:

Place your CSV file into the data_import/staging/ folder

Run the import script:
```bash
python import_csv.py
```
The script will:

Parse valid records and insert them into the database

Move processed files to processed/

Move problematic files to errored/

### Notes
The Kaggle dataset used for automated import is too large to be committed to GitHub


