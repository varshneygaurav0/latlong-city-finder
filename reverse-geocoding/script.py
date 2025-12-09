import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from tqdm import tqdm

# --------------------------------------------------
# Load CSV
# --------------------------------------------------
df = pd.read_csv("coordinates.csv")  # columns: longitude, latitude

# Remove invalid rows
df = df[(df["latitude"] != 0) & (df["longitude"] != 0)].reset_index(drop=True)

# --------------------------------------------------
# Setup Geocoder
# --------------------------------------------------
geolocator = Nominatim(user_agent="reverse_geo_pro")
reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1, max_retries=3)

# --------------------------------------------------
# Cache results to avoid repeat lookups
# --------------------------------------------------
cache = {}

# --------------------------------------------------
# Reverse Geocoding Function
# --------------------------------------------------
def get_location(lat, lon):
    key = f"{lat},{lon}"

    if key in cache:
        return cache[key]

    try:
        location = reverse((lat, lon), language="en")
        if location is None:
            result = ["", "", "", ""]
        else:
            address = location.raw.get("address", {})

            city = (address.get("city") or address.get("town") or 
                    address.get("village") or address.get("hamlet") or "")

            district = (address.get("county") or address.get("district") or 
                        address.get("region") or "")

            state = address.get("state", "")
            country = address.get("country", "")

            result = [city, district, state, country]

        cache[key] = result
        return result

    except Exception as e:
        print(f"Error at {lat}, {lon}: {e}")
        return ["", "", "", ""]

# --------------------------------------------------
# Sequential Loop with Progress Bar
# --------------------------------------------------
results = []
print("\n🔄 Starting Reverse Geocoding...\n")

for idx, row in tqdm(df.iterrows(), total=len(df)):
    lat = row["latitude"]
    lon = row["longitude"]
    results.append(get_location(lat, lon))

    # Save progress every 50 rows
    if idx % 50 == 0 and idx > 0:
        temp_df = df.iloc[:len(results)].copy()
        temp_df[["city", "district", "state", "country"]] = results
        temp_df.to_csv("output_progress.csv", index=False)

# --------------------------------------------------
# Attach Results
# --------------------------------------------------
df[["city", "district", "state", "country"]] = results

# --------------------------------------------------
# Save Final
# --------------------------------------------------
df.to_csv("reverse_geocoded_output.csv", index=False)

print("\n✅ DONE! Saved as reverse_geocoded_output.csv")
