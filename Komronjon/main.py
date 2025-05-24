from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the target URL
url = "https://shaxzodbek.com/projects/weather-forecast-app/"
driver.get(url)

# Allow time for the page to load
time.sleep(3)

# Extract project card information
try:
    # Initialize a dictionary to store extracted data
    card_data = {}

    # Extract title
    title = driver.find_element(By.TAG_NAME, "h1").text
    card_data["Title"] = title

    # Extract publish date (project date)
    project_date = driver.find_element(By.CLASS_NAME, "project-date").text
    card_data["Publish Date"] = project_date

    # Extract project types (e.g., Website, API)
    project_types = [elem.text for elem in driver.find_elements(By.CLASS_NAME, "type-badge")]
    card_data["Project Types"] = project_types

    # Extract featured image URL
    image_elem = driver.find_element(By.CLASS_NAME, "project-featured-image").find_element(By.TAG_NAME, "img")
    image_url = image_elem.get_attribute("src")
    card_data["Image URL"] = image_url

    # Extract project description
    description = driver.find_element(By.CLASS_NAME, "project-description").text
    card_data["Description"] = description

    # Extract technologies used (icons and text)
    tech_items = driver.find_elements(By.CLASS_NAME, "technology-item")
    technologies = []
    for item in tech_items:
        tech_img = item.find_element(By.TAG_NAME, "img").get_attribute("src")
        tech_name = item.find_element(By.TAG_NAME, "span").text
        technologies.append({"Icon": tech_img, "Name": tech_name})
    card_data["Technologies"] = technologies

    # Extract project links (GitHub, Live Demo, etc.)
    project_links = driver.find_elements(By.CLASS_NAME, "project-links")[0].find_elements(By.TAG_NAME, "a")
    links = {link.text: link.get_attribute("href") for link in project_links}
    card_data["Links"] = links

    # Save the extracted data to a text file
    with open("weather_forecast_app_data.txt", "w", encoding="utf-8") as file:
        for key, value in card_data.items():
            file.write(f"{key}: {value}\n")
        print("Data successfully saved to 'weather_forecast_app_data.txt'")

except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
