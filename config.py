from dataclasses import dataclass

@dataclass
class Config:
    """Configurations for data ingestion"""
    restaurant_filepath: str
    country_code_filepath: str
    restaurants_save_filepath: str
    restaurant_events_save_filepath: str
    


configs = Config(
    restaurant_filepath="source_data/restaurant_data.json",
    country_code_filepath="source_data/Country-Code.xlsx",
    restaurants_save_filepath="output_data/restaurants.csv",
    restaurant_events_save_filepath="output_data/restaurant_events.csv"
)