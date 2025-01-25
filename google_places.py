import requests

GOOGLE_API_KEY = "your_google_api_key_here"

def get_top_attractions(destination, num_results=5):
    """
    Fetch top attractions for a destination using Google Places API.
    """
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"top attractions in {destination}",
        "key": GOOGLE_API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
    data = response.json()
    results = data.get("results", [])
    attractions = []

    for result in results[:num_results]:
        attractions.append({
            "name": result.get("name"),
            "address": result.get("formatted_address"),
            "rating": result.get("rating", "No rating available"),
        })

    return attractions
