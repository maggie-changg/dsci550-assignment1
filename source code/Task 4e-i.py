import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "../dataset/haunted_places.tsv")

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found!")
else:
    df = pd.read_csv(file_path, sep="\t")
    print(df.head())

df = pd.read_csv(file_path, sep="\t")


df.columns = df.columns.str.strip()


def categorize_time_of_day(description):
    if pd.isna(description):
        return "Unknown"
    
    description = description.lower()
    if any(word in description for word in ["morning", "sunrise", "dawn"]):
        return "Morning"
    elif any(word in description for word in ["afternoon", "midday"]):
        return "Afternoon"
    elif any(word in description for word in ["evening", "sunset", "dusk"]):
        return "Evening"
    elif any(word in description for word in ["night", "midnight", "dark"]):
        return "Night"
    else:
        return "Unknown"

df["Time of Day"] = df["description"].apply(categorize_time_of_day)


def categorize_apparition_type(description):
    if pd.isna(description):
        return "Unknown"
    
    description = description.lower()
    if any(word in description for word in ["ghost", "spirit"]):
        return "Ghost"
    elif "orb" in description:
        return "Orb"
    elif any(word in description for word in ["ufo", "alien", "extraterrestrial"]):
        return "UFO"
    elif any(word in description for word in ["child", "boy", "girl"]):
        return "Child"
    elif "woman" in description:
        return "Female"
    elif "man" in description:
        return "Male"
    elif "several" in description:
        return "Several Ghosts"
    else:
        return "Unknown"

df["Apparition Type"] = df["description"].apply(categorize_apparition_type)


def categorize_event_type(description):
    if pd.isna(description):
        return "Unknown"
    
    description = description.lower()
    if any(word in description for word in ["murder", "killed", "death", "homicide"]):
        return "Murder"
    elif any(word in description for word in ["supernatural", "paranormal", "haunted"]):
        return "Supernatural Phenomenon"
    elif any(word in description for word in ["accident", "crash", "fire"]):
        return "Accident"
    else:
        return "Unknown"

df["Event Type"] = df["description"].apply(categorize_event_type)


df["state"] = df["state"].str.strip().str.title()


import pandas as pd
import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def fetch_timeanddate_daylight():
    url = "https://www.timeanddate.com/astronomy/usa"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(" Failed to fetch data from TimeAndDate website.")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "tb-sm"}) 
    if not table:
        print(" No valid table found on TimeAndDate website.")
        return None

    data = []
    for row in table.find_all("tr")[1:]: 
        cols = row.find_all("td")
        if len(cols) >= 3:
            state = cols[0].text.strip()
            daylight_hours = cols[2].text.strip().split(" ")[0]  
            data.append({"state": state, "daylight_hours": daylight_hours})

    return pd.DataFrame(data)


def fetch_navy_daylight_hours():
    url = "https://aa.usno.navy.mil/data/Dur_OneYear"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(" Failed to fetch data from US Naval Observatory.")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        print("No valid table found on US Naval Observatory website.")
        return None

    data = []
    for row in table.find_all("tr")[1:]: 
        cols = row.find_all("td")
        if len(cols) >= 2:
            state = cols[0].text.strip()
            daylight_hours = cols[1].text.strip()
            data.append({"state": state, "daylight_hours": daylight_hours})

    return pd.DataFrame(data)


def merge_daylight_data():
    print(" Fetching daylight duration data from Time and Date...")
    timeanddate_df = fetch_timeanddate_daylight()
    
    print(" Fetching daylight duration data from US Naval Observatory...")
    navy_df = fetch_navy_daylight_hours()
    
    if timeanddate_df is None and navy_df is None:
        print(" Failed to process daylight data.")
        return None
    

    daylight_data = pd.concat([timeanddate_df, navy_df], ignore_index=True).drop_duplicates(subset=["state"])

    daylight_data["daylight_hours"] = pd.to_numeric(daylight_data["daylight_hours"], errors="coerce")
    daylight_data["daylight_hours"].fillna(daylight_data["daylight_hours"].median(), inplace=True)

    return daylight_data

daylight_data = merge_daylight_data()
if daylight_data is not None:
    output_path = "processed_daylight_data.tsv"
    daylight_data.to_csv(output_path, sep="\t", index=False)
    print(f" Processing complete. Data saved to: {output_path}")



