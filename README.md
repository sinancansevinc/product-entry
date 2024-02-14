# ProductEntry

## Project Description

ProductEntry is a scraping project that extracts product information from an XML file and stores it in a MongoDB database.

## Getting Started

This project is designed for Python developers. Follow the steps below to get started.

1. **Download and Install MongoDB:**
   - Download Python from the [official website](https://www.python.org/downloads/) and install it.
   - Download MongoDB from the [official website](https://www.mongodb.com/try/download/community) and install it.

3. **Create Python Virtual Environment (venv):**
   - **For Mac:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **For Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

4. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt

5. **Configure MongoDb Connection in DatabaseManager:**
    - Open the DatabaseManager.py file in your project.
    - Find the section where the MongoClient, db, and collection are configured.
    - Adjust the connection parameters, database name, and collection name according to your MongoDB setup.

## Usage

When the project is run, by your decision, you can scrape products from the XML file and save them on database or you can get products or you can delete them.


   
