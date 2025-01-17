import pandas as pd
from serpapi import GoogleSearch
from fuzzywuzzy import process
import os

def clean_data(file_path):
    """Cleans and standardizes the input CSV file."""
    try:
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
        return data
    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return None

def fetch_external_data(product_name):
    """Fetch competitor pricing data from Google Shopping using SerpAPI."""
    try:
        # Retrieve SerpAPI key from environment variables
        api_key = os.getenv("SERPAPI_KEY")
        if not api_key:
            print("Error: SERPAPI_KEY not found in .env file.")
            return None

        # Define search parameters
        params = {
            "engine": "google_shopping",  # Use Google Shopping engine
            "q": product_name,           # Query string (product name)
            "hl": "en",                  # Language
            "gl": "us",                  # Country
            "api_key": api_key           # SerpAPI key
        }

        # Perform search
        search = GoogleSearch(params)
        results = search.get_dict()
        shopping_results = results.get("shopping_results", [])

        # Check if any shopping results were found
        if not shopping_results:
            print(f"No shopping results found for {product_name}.")
            return None

        # Extract the first relevant result
        first_result = shopping_results[0]
        extracted_price = first_result.get("extracted_price")  # Direct float price
        if extracted_price is not None:
            return {
                "name": first_result["title"],
                "price": extracted_price
            }
        else:
            print(f"No extracted price found for {product_name}.")
            return None

    except Exception as e:
        print(f"Error during SerpAPI fetch: {e}")
        return None

def compare_prices(internal_data):
    """Compare internal product prices with external market prices."""
    results = []
    for _, row in internal_data.iterrows():
        product_name = row["product_name"]
        our_price = row["our_price"]

        # Fetch external price
        external_data = fetch_external_data(product_name)
        if external_data:
            competitor_price = external_data["price"]
            price_difference = our_price - competitor_price
            results.append({
                "product_name": product_name,
                "our_price": our_price,
                "competitor_price": competitor_price,
                "price_difference": price_difference,
                "recommendation": "Reduce" if price_difference > 0 else "Increase"
            })
        else:
            results.append({
                "product_name": product_name,
                "our_price": our_price,
                "competitor_price": None,
                "price_difference": None,
                "recommendation": "No data available"
            })

    return pd.DataFrame(results)
