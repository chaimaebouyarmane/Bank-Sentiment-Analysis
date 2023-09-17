# Bank Branch Sentiment Analysis Project 📊

This project aims to develop an automated sentiment analysis system for bank branches using data mining techniques. Our goal is to collect customer feedback to gain insights into their sentiments regarding banking services. The results of this sentiment analysis will provide valuable information to bank branches, allowing them to identify potential issues, enhance their customer service, and strengthen their competitive advantage. To achieve this, we rely on tools and technologies such as Apify, Airflow, BERT, PostgreSQL, and Power BI to collect, transform, store, and visualize data.


## Project Objectives 🎯

The main objectives of this project are as follows:
- Collect data from various sources.
- Apply advanced sentiment analysis using BERT.
- Store the results in a PostgreSQL database.
- Visualize the data using Power BI.

## Project Architecture 🏛️

The project's architecture includes the following components:
- **Apify**: Used for data extraction from online sources.
- **Airflow**: Manages the scheduling and execution of data processing tasks.
- **BERT**: A natural language processing (NLP) model for sentiment analysis.
- **PostgreSQL**: The relational database where data is stored.
- **Power BI**: Used for data visualization.

## Project Structure 📂

The project structure is as follows:
- `extraction.py`: Script to extract data from online sources.
- `transformation.py`: Script to clean and transform data.
- `loading.py`: Script to load data into PostgreSQL.
- `airflow_dag.py`: The Python file defining the Airflow DAG (Directed Acyclic Graph) for task scheduling.

## How to Run the Project ⚙️

1. Ensure you have the required Python dependencies installed (see `requirements.txt`).
2. Configure the PostgreSQL connection parameters in `loading.py`.
3. Execute the Airflow DAG using `airflow_dag.py` to automate the process.

## Results and Visualization 📈

The results of the sentiment analysis are stored in PostgreSQL. You can visualize this data using Power BI to gain valuable insights into customer sentiments towards bank branches.

## Author and Contact 📧

Author: [Your Name]
Contact: [Your Email Address]

Feel free to contribute, report issues, or ask questions.

---

✨ Leverage sentiment analysis to enhance customer experience, address issues, and stand out from the competition! ✨
