import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
import folium

# Phone number to track
phone_number = "9051648577"

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number, None)

# Get the country information
country_info = geocoder.description_for_number(parsed_number, "en")

# Get the country code
country_code = phonenumbers.region_code_for_number(parsed_number)

# Initialize OpenCage Geocoder
geocoder_key = "232a5a25138e42a1a1541c7ac70b9794"
geocoder = OpenCageGeocode(geocoder_key)

# Build the query using country code
query = f"{country_info}, {country_code}"

# Perform geocoding
results = geocoder.geocode(query)

# Extract latitude and longitude if results exist
if results:
    lat = results[0]['geometry']['lat']  # type: ignore
    lng = results[0]['geometry']['lng']  # type: ignore
    print(f"Location: {results[0]['formatted']}")  # type: ignore
    print(f"Coordinates: {lat}, {lng}")

    # Create map centered on the location
    myMap = folium.Map(location=[lat, lng], zoom_start=9)

    # Add marker for the location
    folium.Marker([lat, lng], popup=results[0]['formatted']
                  ).add_to(myMap)  # type: ignore

    # Save map to HTML file
    myMap.save("location_map.html")
    print("Map saved as 'location_map.html'")
else:
    print("Location information not found.")
