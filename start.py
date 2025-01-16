
import requests
from tqdm import tqdm

def download_with_progress(url, save_path):
    try:
        print("[+]Calculating file...")
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('Content-Length', 0))

            with open(save_path, "wb") as file, tqdm(
                desc="Downloading",
                total=total_size,
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
                    bar.update(len(chunk))

        print("[+] Download completed successfully!")

    except requests.exceptions.RequestException as e:
        print(f"[+] Error downloading file: {e}")
    # URL của tệp cần tải
url = "https://github.com/Namtheskidder/trash/releases/download/1.3/roblox.zip"  # Thay bằng URL tệp của bạn
save_path = "largefile.zip"  # Tên tệp lưu về

download_with_progress(url, save_path)
