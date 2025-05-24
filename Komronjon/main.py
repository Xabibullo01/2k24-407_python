from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json

def scrape_weather_project():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://shaxzodbek.com/projects/weather-forecast-app/"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        card_data = {}
        card_data["Title"] = driver.find_element(By.TAG_NAME, "h1").text
        card_data["Publish Date"] = driver.find_element(By.CLASS_NAME, "project-date").text
        card_data["Project Types"] = [elem.text for elem in driver.find_elements(By.CLASS_NAME, "type-badge")]

        image_elem = driver.find_element(By.CLASS_NAME, "project-featured-image").find_element(By.TAG_NAME, "img")
        card_data["Image URL"] = image_elem.get_attribute("src")

        card_data["Description"] = driver.find_element(By.CLASS_NAME, "project-description").text

        technologies = []
        for item in driver.find_elements(By.CLASS_NAME, "technology-item"):
            tech_img = item.find_element(By.TAG_NAME, "img").get_attribute("src")
            tech_name = item.find_element(By.TAG_NAME, "span").text
            technologies.append({"Icon": tech_img, "Name": tech_name})
        card_data["Technologies"] = technologies

        project_links_elements = driver.find_elements(By.CLASS_NAME, "project-links")
        if project_links_elements:
            links = {
                link.text: link.get_attribute("href")
                for link in project_links_elements[0].find_elements(By.TAG_NAME, "a")
            }
        else:
            links = {}
        card_data["Links"] = links

        file_path = os.path.join(os.path.dirname(__file__), "weather_forecast_app_data.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(card_data, f, ensure_ascii=False, indent=2)
        print(f"✅ Data successfully saved to '{file_path}'")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_weather_project()
