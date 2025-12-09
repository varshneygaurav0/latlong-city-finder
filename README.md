# **LatLong City Finder**

Bulk Reverse Geocoding (Latitude/Longitude → City, District, State, Country) using Python + OpenStreetMap (Nominatim)

---

## 🚀 Overview

**LatLong City Finder** is a Python tool that converts raw **latitude & longitude coordinates** into:

* City / Town / Village
* District / County
* State
* Country

This script is optimized for **large datasets**, includes:

* Caching (avoids repeated lookups)
* Progress saving (`output_progress.csv`)
* Error handling & retries
* 1 request/second rate-limited Nominatim usage
* Clean final export: **reverse_geocoded_output.csv**

---

## 📁 Project Structure

reverse-geocoding/
│
├── script.py                      # Main Python script
├── coordinates.csv                # Input file
└── reverse_geocoded_output.csv    # Final output (auto-generated)

---

## 🗂️ Features

✔ Bulk reverse-geocoding
✔ Automatically detects city/town/village
✔ District, State & Country detection
✔ Caching system → speeds up repeated coordinates
✔ Saves progress every few batches
✔ Skips invalid coordinates (0,0)
✔ Fully open-source & OpenStreetMap-powered

---

## 📦 Requirements

Install dependencies:

```bash
pip install pandas geopy joblib tqdm
```

---

## 📁 Input Format (`coordinates.csv`)

Your CSV **must include** these two columns:

```csv
longitude,latitude
88.1234,22.9876
87.9876,22.4567
...
```

---

## 🧠 How It Works

* Reads coordinates from CSV
* Skips invalid or zero coordinates
* Sends reverse-geocode requests to Nominatim
* Extracts city, district, state, and country
* Writes results to output CSV

---

## ▶️ Usage

Run the script:

```bash
python script.py
```

You will see a progress bar:

```
🔄 Starting Reverse Geocoding...
███████████▒▒▒ 35% Completed...
```

---

## 📤 Output Files

### ✔ Final Output

```
reverse_geocoded_output.csv
```

### ✔ Auto-Saved Progress

```
output_progress.csv
```

---

## 📄 Example Output

```csv
longitude,latitude,city,district,state,country
87.9034,22.0420,Tamluk,Purba Medinipur,West Bengal,India
88.4145,22.6332,Barrackpore,North 24 Parganas,West Bengal,India
...
```

---

## ⚠️ Nominatim Usage Rules (Very Important!)

* Minimum **1 second delay** per request
* Do **NOT** hammer the server (your IP can get blocked)
* Use a unique `user_agent` (already done in script)

---

## 🤝 Contributing

PRs are welcome!
You can help improve:

* Speed optimization
* Multi-provider support (Google Maps API, Mapbox, etc.)
* GUI frontend
* API wrapper

---

## 🪪 License

This project is licensed under the MIT License.
Free for commercial & personal use.

---

## ⭐ Support the Project

If this tool helped you, give the repo a **star ⭐ on GitHub**!
