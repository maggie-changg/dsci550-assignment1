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


daylight_data = {
    "state": ["California", "Texas", "Florida", "New York", "Illinois"],
    "Avg Daylight Hours": [10.5, 9.8, 10.1, 9.2, 8.9]  
}

daylight_df = pd.DataFrame(daylight_data)


df = df.merge(daylight_df, on="state", how="left")


output_path = "/mnt/data/processed_haunted_places.csv"
df.to_csv(output_path, index=False)


import pandas as pd

print("Processed Haunted Places Data:")
print(df.head())  


output_path = "processed_haunted_places.csv"
df.to_csv(output_path, index=False)

print("Processing complete. Data saved to:", output_path)
