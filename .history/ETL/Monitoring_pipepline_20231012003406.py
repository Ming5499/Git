import logging

try:# Try to filter by price_change   
    clean_stock_data = transform(raw_stock_data)   
    logging.info("Successfully filtered DataFrame by 'price_change'")
except KeyError as ke:# Handle the error, create new column, transform   
    logging.warning(f"{ke}: Cannot filter DataFrame by 'price_change'")    
    raw_stock_data["price_change"] = raw_stock_data["close"] - raw_stock_data["open"]   
    clean_stock_data = transform(raw_stock_data)
