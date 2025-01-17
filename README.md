# 10EQS Evaluation
This is a part of Technical evaluation assessment

## Setup Instructions

Follow these steps to set up the project on your local machine.

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- git
- SerpAPI key (stored in a `.env` file)

### Step 1: Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/KiranV-10/10EQS.git
```

### Step 2: Install the dependencies

in the root 

```bash
pip install -r requirements.txt
```

### Step 3: SerpAPI

Create a .env file in the root directory and copy the following into it. 

```bash
SERPAPI_KEY=Type_Your_Access_Token_Here
```
You will need to singup with SerpAPI and get an accesstoken (will be given on successful singup)


### Step 4: Run the program

Cd into the src folder and type the following command to run the program

```bash
python analysis.py ../data/products.csv
```

### Step 5: Results.md
You can find the results.md in the src folder.
- The results of this program are stored in a tabular format in results.md file after it successfully runs.
- This is a real-time comparision of the store price to the actual market price. If a product is not found an exact match or even a closer match then it is deemed as "No data available"

### Step 6: Report.md
You can find the report.md in the src folder.
- This is a brief report of our tool and how does this work and what the results suggest. It is a prototype model and not a full-fledged application since we need more market insights and robust webscrapers to find the exact match for the product in our store. This is also something I want to build on-top of this dedicatedly if I am given a chance.


## My Approach to the problem

The program automates price comparison between internal product prices and external market prices fetched from Google Shopping via SerpAPI. Key steps include:

- Data Cleaning: Standardizes input data for consistent processing.
- External Data Fetching: Retrieves competitor prices via SerpAPI. If categorized results are unavailable, fuzzy matching identifies the best match from shopping results.
- Price Analysis: Compares internal and competitor prices, calculates differences, and generates actionable recommendations.
- Reporting: Outputs insights in a markdown file for easy review.


## Issues and Limitations
- The program requires a valid SerpAPI key and a stable internet connection. API rate limits or connectivity issues can affect functionality.
- In cases where exact matches are unavailable, fuzzy matching may yield incorrect results, particularly for generic product names.
- Processing very large input files may result in slower execution times due to the sequential API calls and fuzzy matching operations.
- The program assumes all prices are in USD. Currency differences or conversions are not accounted for.
