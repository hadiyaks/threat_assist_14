import requests
import base64

API_KEY = "api key here"

def check_url(url):
    headers = {"x-apikey": API_KEY}

    # Encode URL
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

    endpoint = f"https://www.virustotal.com/api/v3/urls/{url_id}"

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        return stats
    else:
        return {"error": "Unable to fetch results"}
