import requests
import csv


# Function to fetch plant data from API and save to a CSV file
def fetch_and_save_plant_data(api_url, filename):
    all_plants = []

    # Iterate over each page of the API response
    current_page = 1
    while current_page <= 90:
        # Make GET request to the API with the current page number
        response = requests.get(api_url, params={"page": current_page})

        # Check if request was successful
        if response.status_code == 200:
            # Extract plant data from the response
            api_data = response.json()
            plants = api_data.get("data")

            # If there are no more plants, break the loop
            if not plants:
                break

            # Append plant data to the list of all plants
            all_plants.extend(plants)

            # Move to the next page
            current_page += 1
        else:
            print("Error: Failed to fetch data from the API")
            break

    # Save plant data to a CSV file
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "common_name", "scientific_name", "cycle", "watering", "sunlight"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header row
        writer.writeheader()

        # Write plant data rows
        for plant in all_plants:
            scientific_name = ", ".join(plant.get("scientific_name", []))
            sunlight = ", ".join(plant.get("sunlight", []))

            writer.writerow({
                "id": plant.get("id", ""),
                "common_name": plant.get("common_name", ""),
                "scientific_name": scientific_name,
                "cycle": plant.get("cycle", ""),
                "watering": plant.get("watering", ""),
                "sunlight": sunlight
            })

    print(f"Plant data saved to {filename}")

# Example usage
api_url = "https://perenual.com/api/species-list?key=sk-C0K5661db3590e58f5114"
fetch_and_save_plant_data(api_url, "plants_data.csv")

'''
# Function to fetch plant data from API and save to a CSV file
def fetch_and_save_plant_data(api_url, filename):
    all_plants = []

    # Iterate over each page of the API response
    current_page = 2
    # Make GET request to the API with the current page number
    response = requests.get(api_url, params={"page": current_page})

    # Check if request was successful
    if response.status_code == 200:
        # Extract plant data from the response
        api_data = response.json()
        plants = api_data.get("data")

        # Append plant data to the list of all plants
        all_plants.extend(plants)
    else:
        print("Error: Failed to fetch data from the API")
        

    # Save plant data to a CSV file
    with open(filename, "a", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "common_name", "scientific_name", "cycle", "watering", "sunlight"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header row
        writer.writeheader()

        # Write plant data rows
        for plant in all_plants:
            scientific_name = ", ".join(plant.get("scientific_name", []))
            sunlight = ", ".join(plant.get("sunlight", []))

            writer.writerow({
                "id": plant.get("id", ""),
                "common_name": plant.get("common_name", ""),
                "scientific_name": scientific_name,
                "cycle": plant.get("cycle", ""),
                "watering": plant.get("watering", ""),
                "sunlight": sunlight
            })

    print(f"Plant data saved to {filename}")

# Example usage
api_url = "https://perenual.com/api/species-list?key=sk-C0K5661db3590e58f5114"
fetch_and_save_plant_data(api_url, "plants_data.csv")
'''