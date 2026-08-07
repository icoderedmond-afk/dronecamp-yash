import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            params={"q": artist}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request.")
        return

    content = response.json()
    artworks = content.get("data", [])
    
    # Filter results to see if the artist name is actually in the returned items
    matching_artworks = [
        art for art in artworks 
        if art.get("artist_display") and artist["artist_display"].lower() == artist.lower()
    ]

    if not matching_artworks:
        print("No artworks found. Perhaps you spelled it wrong.")
        return

    for artwork in matching_artworks:
        print(f"{artwork['title']}")


main()