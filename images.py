import requests
from dotenv import load_dotenv
import os


class PexelsAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("PEXELS_API_KEY")
        self.base_url = "https://api.pexels.com/v1/search"

    def get_image_url(self, query):
        headers = {"Authorization": self.api_key}
        params = {"query": query, "per_page": 1}
        response = requests.get(self.base_url, headers=headers, params=params)
        return self.parse_response(response.json())

    def parse_response(self, response):
        try:
            return response["photos"][0]["src"]["original"]
        except IndexError:
            return "No image found for that query."


if __name__ == "__main__":
    pexels_api = PexelsAPI()
    print(pexels_api.get_image_url("applefdksjaf"))
