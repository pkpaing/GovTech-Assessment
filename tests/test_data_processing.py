# tests/test_data_processing.py
import pytest
import pandas as pd
from data_processing import load_restaurant_data, load_country_code_data, extract_restaurants, extract_restaurant_events, determine_rating_thresholds

@pytest.fixture
def restaurant_data():
    return [
        {
            "restaurants": [
                {
                    "restaurant": {
                        "id": "1",
                        "name": "Restaurant A",
                        "location": {
                            "country_id": 1,
                            "city": "City A"
                        },
                        "user_rating": {
                            "votes": 100,
                            "aggregate_rating": "4.5",
                            "rating_text": "Excellent"
                        },
                        "cuisines": "Italian, Chinese",
                        "zomato_events": [
                            {
                                "event": {
                                    "event_id": "E1",
                                    "start_date": "2019-04-01",
                                    "end_date": "2019-04-02",
                                    "title": "Event A",
                                    "photos": [{"photo": {"url": "http://example.com/photo.jpg"}}]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    ]

@pytest.fixture
def country_code_data():
    return pd.DataFrame({
        "Country Code": [1],
        "Country": ["Country A"]
    })

def test_load_restaurant_data(tmp_path):
    file_path = tmp_path / "restaurant_data.json"
    data = '{"restaurants": []}'
    file_path.write_text(data)
    
    result = load_restaurant_data(str(file_path))
    assert result == {"restaurants": []}

def test_load_country_code_data(tmp_path):
    file_path = tmp_path / "country_codes.xlsx"
    data = pd.DataFrame({"Country Code": [1], "Country": ["Country A"]})
    data.to_excel(file_path, index=False)
    
    result = load_country_code_data(str(file_path))
    pd.testing.assert_frame_equal(result, data)

def test_extract_restaurants(restaurant_data, country_code_data):
    result = extract_restaurants(restaurant_data, country_code_data)
    
    expected = pd.DataFrame([{
        "Restaurant Id": "1",
        "Restaurant Name": "Restaurant A",
        "Country": "Country A",
        "City": "City A",
        "User Rating Votes": 100,
        "User Aggregate Rating": 4.5,
        "Cuisines": "Italian, Chinese"
    }])
    
    pd.testing.assert_frame_equal(result, expected)

def test_extract_restaurant_events(restaurant_data):
    result = extract_restaurant_events(restaurant_data)
    
    expected = pd.DataFrame([{
        "Event Id": "E1",
        "Restaurant Id": "1",
        "Restaurant Name": "Restaurant A",
        "Photo URL": "http://example.com/photo.jpg",
        "Event Title": "Event A",
        "Event Start Date": "2019-04-01",
        "Event End Date": "2019-04-02"
    }])
    
    pd.testing.assert_frame_equal(result, expected)

def test_determine_rating_thresholds(restaurant_data):
    result = determine_rating_thresholds(restaurant_data)
    
    expected = pd.DataFrame([{
        "Rating Text": "Excellent",
        "Min. Rating": 4.5,
        "Max Rating": 4.5,
        "Mean Rating": 4.5
    }])
    
    pd.testing.assert_frame_equal(result, expected)
