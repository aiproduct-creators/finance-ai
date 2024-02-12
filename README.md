# Finance AI Bot

Finance AI Bot is an innovative web application crafted to assist individuals and professionals in the finance sector by providing precise answers to finance-related questions directly from financial documents. Utilizing advanced AI algorithms, this application supports a variety of formats including CSV, and MS Excel files, making it a versatile tool for financial analysis and decision-making.

## Features

- Automatically extract and interpret financial data from documents in CSV, PDF, Excel, and Word formats.
- Provide accurate answers to complex finance-related questions by analyzing the content of financial documents.
- Offer insights and analytics derived from financial data to aid in informed decision-making.
- Enable users to quickly understand financial trends, performance metrics, and key financial indicators from their documents.

## Installation

To run this application, you need to have Python 3.8 or higher installed on your system. Additionally, you'll need to obtain a OpenAI API key and store it securely. Follow these steps to set up and run the application:

### Setup Instructions

#### For Mac

- Open a terminal and navigate to the directory where you want to clone this repository.
- Run the following command to clone this repository:

    ```bash
    git clone git@github.com:aiproduct-creators/finance-ai.git
    ```
- Navigate to the cloned repository:

    ```
    cd finance-ai
    ```
- Create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install the required packages:
    ```
    pip install -r requirements.txt
    ```
- Copy the `.env.example` file to a new file named `.env` and set your Cohere API key:
    ```
    OPENAI_KEY=your_api_key_here
    ```
- Run the application:
    ```
    streamlit run app.py
    ```
    Open your browser and go to http://localhost:8501 to see the app.

#### For Windows

- Open a command prompt and navigate to the directory where you want to clone this repository.
- Run the following command to clone this repository:
    ```
    git clone git@github.com:aiproduct-creators/finance-ai.git
    ```
- Navigate to the cloned repository:

    ```
    cd finance-ai
    ```
- Create a virtual environment and activate it:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
- Install the required packages:
    ```
    pip install -r requirements.txt
    ```
- Copy the `.env.example` file to a new file named `.env` and set your Cohere API key:
    ```
    OPENAI_KEY=your_api_key_here
    ```
- Run the application:
    ```
    streamlit run app.py
    ```
Open your browser and go to http://localhost:8501 to see the app.

