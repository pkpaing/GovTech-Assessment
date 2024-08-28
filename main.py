import argparse
import data_processing
import config

def create_arg_parser():
    parser = argparse.ArgumentParser(description="Process restaurant data.")
    
    # Adding flags for each function
    parser.add_argument(
        '--extract_restaurants', 
        action='store_true', 
        help="Flag to extract restaurants data and save it to a CSV file."
    )
    
    parser.add_argument(
        '--extract_restaurant_events', 
        action='store_true', 
        help="Flag to extract restaurant events and save them to a CSV file."
    )
    
    parser.add_argument(
        '--determine_rating_thresholds', 
        action='store_true', 
        help="Flag to determine rating thresholds based on the aggregate rating."
    )
    
    return parser

if __name__ == "__main__":
    parser = create_arg_parser()
    args = parser.parse_args()

    restaurant_data = data_processing.load_restaurant_data(config.configs.restaurant_filepath)
    country_code_data = data_processing.load_country_code_data(config.configs.country_code_filepath)
    
    if args.extract_restaurants:
        restaurants_df = data_processing.extract_restaurants(restaurant_data, country_code_data)
        print("Restaurants data extracted and saved to restaurants.csv")
    
    if args.extract_restaurant_events:
        restaurant_events = data_processing.extract_restaurant_events(restaurant_data)
        print("Restaurant events extracted and saved to restaurant_events.csv")
    
    if args.determine_rating_thresholds:
        rating_threshold = data_processing.determine_rating_thresholds(restaurant_data)
        print("Rating thresholds determined:")
        print(rating_threshold)
