import requests
import os

# Multiple catalogs to increase tracked objects
TLE_URLS = [
    "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?GROUP=cosmos-2251-debris&FORMAT=tle",
    "https://celestrak.org/NORAD/elements/gp.php?GROUP=fengyun-1c-debris&FORMAT=tle"
]


def download_tle():

    print("Downloading satellite catalogs...")

    os.makedirs("../data", exist_ok=True)

    output_file = "../data/tle_cache.txt"

    with open(output_file, "w") as f:

        for url in TLE_URLS:

            print("Fetching:", url)

            r = requests.get(url)

            if r.status_code == 200:
                f.write(r.text + "\n")

    print("All catalogs merged into data/tle_cache.txt")