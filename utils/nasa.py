import requests
from datetime import date
from utils.config import NASA_API_KEY, NASA_APOD_URL


def get_apod(target_date=None):
    """
    Fetch NASA Astronomy Picture of the Day.
    Returns a dictionary on success.
    Raises an exception on failure so we can actually debug it.
    """

    params = {
        "api_key": NASA_API_KEY
    }

    if target_date:
        if isinstance(target_date, date):
            params["date"] = target_date.isoformat()
        else:
            params["date"] = target_date

    response = requests.get(
        NASA_APOD_URL,
        params=params,
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    return {
        "title": data.get("title", ""),
        "explanation": data.get("explanation", ""),
        "url": data.get("url", ""),
        "hdurl": data.get("hdurl", ""),
        "media_type": data.get("media_type", ""),
        "date": data.get("date", ""),
        "copyright": data.get("copyright", ""),
    }