import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def fetch_images(query):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=10"
    headers = {"Authorization": PEXELS_API_KEY}

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                image_urls = [photo['src']['large'] for photo in data.get('photos', [])]

                if not image_urls:
                    print("No images found from Pexels.")
                    return []

                image_files = []

                for i, img_url in enumerate(image_urls):
                    img_data = requests.get(img_url).content
                    filename = f"image_{i}.jpg"

                    with open(filename, "wb") as f:
                        f.write(img_data)

                    image_files.append(filename)

                return image_files

            else:
                print(f"API returned status code {response.status_code}")

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2)

    print("All retries failed. Returning empty image list.")
    return []
