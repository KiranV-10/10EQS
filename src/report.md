
## Summary of Data Cleaning Steps
The data cleaning process ensures that the input CSV file is standardized and suitable for processing by the program. Below are the key steps:

- Read Input Data:
    The program reads the input CSV file using pandas.read_csv().

- Standardize Column Names:
    Column names are converted to lowercase.Spaces in column names are replaced with underscores (_). Any leading or trailing whitespace in column names is removed.
- Handle Missing or Invalid Data: Rows with critical missing data (e.g., product_name or our_price) are flagged or dropped based on the severity.
- Ensure Data Types: Ensures numerical columns (e.g., our_price) are correctly interpreted as numeric types. Converts text columns to consistent string format for uniform processing.

## Key Insights Discovered
Please take a look at [results.md](src/results.md) which is auto-generated once the program is run.
- Price Competitiveness: The program identifies products where the internal pricing is higher or lower than competitor prices, enabling data-driven decisions to adjust pricing strategies.

- Market Gaps:For some products, no competitor data was available, highlighting potential market niches or areas requiring further investigation.

- Recommendations for Pricing: 
    
        Each product is evaluated for pricing adjustments:

        "Reduce" is suggested for overpriced items to stay competitive.
        "Increase" is recommended for underpriced items to maximize profit margins.

- Data Availability Challenges: Certain product titles were not found in the external data, emphasizing the importance of clear and standardized product naming conventions.

- Fuzzy Matching Success: Leveraging fuzzy matching helped retrieve relevant competitor prices even when exact matches were unavailable, demonstrating adaptability to real-world inconsistencies in data.

## External Data Source Documentation
### External Data Source: 
SerpAPI Google Shopping. Our program integrates SerpAPI Google Shopping to fetch real-time product pricing and details for comparison. Below are the details of this external data source:

### API Overview
- Name: SerpAPI Google Shopping
- Description: A powerful API that allows querying Google Shopping results programmatically, providing detailed information about products such as price, title, and seller.

- Key Data Extracted
    
    Product Title: The name of the product retrieved from the shopping results.
    
    Extracted Price: The float value of the product's price, provided directly when available.
    
    Source: The vendor or platform selling the product (e.g., Walmart, Amazon).
    
    Product Link: Direct link to the product's page on the vendor's website.

### Data Handling:
The program processes the ```categorized_shopping_results``` or ```shopping_results``` sections to extract relevant product data.
Fuzzy matching (via fuzzywuzzy) is used to handle cases where the exact product is not listed.
Known Limitations

#### API Quota: The SerpAPI key has a request quota; exceeding it will result in errors.
Regional Restrictions: The shopping results may vary based on location (gl parameter) and might not reflect all global markets.

Incomplete Results: In cases where no categorized_shopping_results are available, fuzzy matching may return less accurate results.

Price Extraction: If extracted_price is missing in the API response, the program cannot retrieve the product price.


## Future Goals 

I want to Develop a robust Pricing Analysis Tool for Local Businesses.

### Integrating AI and ML:
  - Train ML models to predict optimal pricing strategies based on real-time competitor data, demand, and market trends.
  - Develop an AI-based recommendation engine to suggest product bundles or promotions.
  - Use collaborative filtering techniques for personalized recommendations based on customer purchasing behavior.
  - Analyze customer reviews and social media data to identify market sentiment and refine pricing strategies.
### Real-world APIs:
  - Integrate APIs such as the Amazon Product Advertising API, Walmart API, or eBay API to fetch real-time competitor pricing and inventory data.
  - Use API gateways like AWS API Gateway to manage multiple APIs and ensure scalability.
### Web Scraper Development:
  - Developing a robust and scalable Web scraper.
  - Use Scrapy for building robust scrapers or Selenium for websites with heavy JavaScript.
  - Integrate proxies and captcha solvers to handle website restrictions.
### Web and Mobile Application Development:
  - Make it to the production quality and readily available to the public.
### Business Model:
  - Offer tiered subscription models, e.g., Basic, Professional, and Enterprise, with varying feature sets.
  - Introduce a pay-per-use model for businesses that prefer flexibility in data usage.
  - Offer data analysis and pricing strategy consulting as an additional revenue stream.



