from dataclasses import dataclass

@dataclass
class Config:
    """Configurations for data ingestion"""
    restaurant_filepath: str
    country_code_filepath: str


configs = Config(
    restaurant_filepath="data/restaurant_data.json",
    country_code_filepath="data/Country-Code.xlsx"
)