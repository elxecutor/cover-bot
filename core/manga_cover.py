# manga_cover.py

import httpx
import random
import math
import os

BASE_API_URL = "https://api.mangadex.org"
COVER_CDN_URL = "https://uploads.mangadex.org/covers"

def get_top_manga_list(total=608):
    limit = 100
    pages = math.ceil(total / limit)
    all_manga = []

    for page in range(pages):
        offset = page * limit
        response = httpx.get(f"{BASE_API_URL}/manga", params={
            "limit": limit,
            "offset": offset,
            "availableTranslatedLanguage[]": "en",
            "order[rating]": "desc",
        })
        response.raise_for_status()
        manga_batch = response.json()["data"]
        if not manga_batch:
            break
        filtered = [m for m in manga_batch if "en" in m["attributes"]["title"]]
        all_manga.extend(filtered)

    if not all_manga:
        raise ValueError("No valid English manga found.")
    return all_manga

def get_random_cover_art_url(manga_id):
    # Step 1: Get total cover count
    res = httpx.get(f"{BASE_API_URL}/cover", params={
        "manga[]": manga_id, "limit": 1, "offset": 0
    })
    res.raise_for_status()
    total = res.json()["total"]

    if total == 0:
        raise ValueError("No cover art found.")

    # Step 2: Fetch one randomly
    rand_offset = random.randint(0, total - 1)
    res = httpx.get(f"{BASE_API_URL}/cover", params={
        "manga[]": manga_id, "limit": 1, "offset": rand_offset
    })
    res.raise_for_status()
    cover = res.json()["data"][0]
    return f"{COVER_CDN_URL}/{manga_id}/{cover['attributes']['fileName']}"

def download_image(url, filename="cover.jpg"):
    response = httpx.get(url)
    response.raise_for_status()
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename

def fetch_manga_cover():
    manga_list = get_top_manga_list()
    selected = random.choice(manga_list)
    title = selected["attributes"]["title"]["en"]
    manga_id = selected["id"]

    cover_url = get_random_cover_art_url(manga_id)
    image_path = download_image(cover_url)

    return title, image_path

if __name__ == "__main__":
    try:
        title, cover_path = fetch_manga_cover()
        print(f"Fetched cover for: {title}")
        print(f"Cover saved to: {cover_path}")
    except Exception as e:
        print(f"Error fetching manga cover: {e}")