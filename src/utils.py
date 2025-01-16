import pandas as pd
import requests
from fuzzywuzzy import process

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
    """Fetch pricing data for a given product from an external API."""
    try:
        # Query a mock public product API
        response = requests.get("https://fakestoreapi.com/products")
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            return None
        
        external_products = response.json()
        
        # Use fuzzy matching to find the best match
        best_match = process.extractOne(
            product_name, 
            [product["title"] for product in external_products]
        )
        if best_match and best_match[1] > 80:  # Confidence threshold
            matched_product = next(
                item for item in external_products if item["title"] == best_match[0]
            )
            return {"name": matched_product["title"], "price": matched_product["price"]}
        
        return None
    except Exception as e:
        print(f"Error during API fetch: {e}")
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
