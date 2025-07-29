# main.py

import os
from core.manga_cover import fetch_manga_cover
from core.x_poster import post_tweet_with_image
from core.rate_guard import can_post_now, update_last_post_time

def main():
    if not can_post_now():
        print("⏱️ Skipped: Rate limit active. Try again later.")
        return

    try:
        title, image_path = fetch_manga_cover()
        response = post_tweet_with_image(title, image_path)

        if response:  # Only update post time if successful
            update_last_post_time()

        if os.path.exists(image_path):
            os.remove(image_path)

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
