import pandas as pd
import json

def load_restaurant_data(restaurant_data_filepath: str) -> dict:
    with open(restaurant_data_filepath, 'r') as file:
        restaurant_data = json.load(file)
    return restaurant_data

def load_country_code_data(country_code_filepath: str) -> pd.DataFrame:
    country_code_df = pd.read_excel(country_code_filepath)
    return country_code_df

def extract_restaurants(restaurant_data: dict, country_code_df: pd.DataFrame) -> pd.DataFrame:
    restaurants_list = []

    for result in restaurant_data:
        for restaurant in result['restaurants']:
            restaurant_info = restaurant['restaurant']
            country_id = restaurant_info['location']['country_id']
            try:
                country_name = country_code_df.loc[country_code_df['Country Code'] == country_id, 'Country'].values[0]
                restaurant_data = {
                    "Restaurant Id": restaurant_info['id'],
                    "Restaurant Name": restaurant_info['name'],
                    "Country": country_name,
                    "City": restaurant_info['location']['city'],
                    "User Rating Votes": restaurant_info['user_rating']['votes'],
                    "User Aggregate Rating": float(restaurant_info['user_rating']['aggregate_rating']),
                    "Cuisines": restaurant_info['cuisines']
                }
                restaurants_list.append(restaurant_data)
            except:
                pass


    restaurants_df = pd.DataFrame(restaurants_list)
    
    return restaurants_df

def extract_restaurant_events(restaurant_data: dict) -> pd.DataFrame:
    events_list = []
    
    for result in restaurant_data:
        for restaurant in result['restaurants']:
            restaurant_info = restaurant['restaurant']
            restaurant_id = restaurant_info['id']
            restaurant_name = restaurant_info['name']
            
            if restaurant_info.get('zomato_events'):
                for event in restaurant_info['zomato_events']:
                    event_info = event['event']
                    start_date = event_info['start_date']
                    end_date = event_info['end_date']
                    
                    if "2019-04" in start_date or "2019-04" in end_date:
                        event_data = {
                            "Event Id": event_info['event_id'],
                            "Restaurant Id": restaurant_id,
                            "Restaurant Name": restaurant_name,
                            "Photo URL": event_info['photos'][0]['photo']['url'] if event_info['photos'] else "NA",
                            "Event Title": event_info['title'],
                            "Event Start Date": start_date,
                            "Event End Date": end_date
                        }
                        events_list.append(event_data)
    
    events_df = pd.DataFrame(events_list)
    
    return events_df

def determine_rating_thresholds(restaurant_data: dict) -> pd.DataFrame:
    rating_data = {"Rating Text": [], "Aggregate Rating": []}
    
    for result in restaurant_data:
        for restaurant in result['restaurants']:
            restaurant_info = restaurant['restaurant']
            rating_text = restaurant_info['user_rating']['rating_text']
            aggregate_rating = float(restaurant_info['user_rating']['aggregate_rating'])
            
            if rating_text in ["Excellent", "Very Good", "Good", "Average", "Poor"]:
                rating_data["Rating Text"].append(rating_text)
                rating_data["Aggregate Rating"].append(aggregate_rating)

    rating_df = pd.DataFrame(rating_data)
    
    rating_thresholds = rating_df.groupby("Rating Text")["Aggregate Rating"].agg(["min", "max", "mean"]).reset_index()
    rating_thresholds = rating_thresholds.sort_values(by='mean', ascending=True)
    rating_thresholds.columns = ['Rating Text', 'Min. Rating', 'Max Rating', 'Mean Rating']
    
    return rating_thresholds
