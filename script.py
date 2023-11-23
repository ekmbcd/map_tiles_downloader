import os
import requests
import argparse

def download_tiles(min_zoom=0, max_zoom=5, url="https://tile.openstreetmap.org/"):
    headers = {
    'User-Agent': 'Chrome v22.2 Linux Ubuntu',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    }

    for x in range(min_zoom, max_zoom + 1):
        y = 0
        while True:
            z = 0
            while True:
                try:
                    file_name = f"{x}/{y}/{z}.png"
                    # avoid slowdown due to failed requests
                    response = requests.get(url + file_name, headers=headers, timeout=0.5)
                    if response.status_code == 200:
                            # Create directories if they don't exist
                            file_path = "tiles/" + file_name
                            os.makedirs(os.path.dirname(file_path), exist_ok=True)

                            # Save the image
                            with open(file_path, 'wb') as f:
                                f.write(response.content)
                            print(f"Image downloaded and saved at: {file_path}")
                            z += 1
                    else:
                        print(f"Image not found at: {file_name}")
                        break
                except:
                    print(f"Image not found at: {file_name}")
                    break
            if z == 0:
                break
            y += 1
        if y == 0:
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download tiles with optional parameters.')
    parser.add_argument('--min_zoom', type=int, default=0, help='Minimum zoom level')
    parser.add_argument('--max_zoom', type=int, default=5, help='Maximum zoom level')
    parser.add_argument('--url', type=str, default="https://tile.openstreetmap.org/", help='Tile URL')

    args = parser.parse_args()

    download_tiles(args.min_zoom, args.max_zoom, args.url)
