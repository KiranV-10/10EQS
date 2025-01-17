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

        # Try categorized_shopping_results first
        categorized_results = results.get("categorized_shopping_results", [])
        if categorized_results:
            first_result = categorized_results[0]["shopping_results"][0]
            extracted_price = first_result.get("extracted_price")
            if extracted_price is not None:
                return {"price": extracted_price}

        # Fallback to shopping_results if categorized results are not present
        shopping_results = results.get("shopping_results", [])
        if shopping_results:
            # Use fuzzy matching to find the best match
            product_titles = [item["title"] for item in shopping_results]
            best_match, score = process.extractOne(product_name, product_titles)
            if score >= 90:  # Match threshold
                for item in shopping_results:
                    if item["title"] == best_match:
                        extracted_price = item.get("extracted_price")
                        if extracted_price is not None:
                            return {"price": extracted_price}

        # Log when no match is found
        print(f"Exact match not found for {product_name}.")
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
