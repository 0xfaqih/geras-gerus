import requests

def get_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises error for bad response status
        data = response.text  # Get the response text
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def save_data_to_txt(data, filename):
    try:
        with open(filename, 'w') as file:
            file.write(data)
        print("Data berhasil disimpan ke", filename)
    except IOError as e:
        print("Error saat menyimpan data:", e)

def main():
    api_urls = [
        ""
    ]
    filename = "proxy_list.txt"

    for api_url in api_urls:
        # Mengambil data dari API
        data = get_data_from_api(api_url)
        if data:
            # Menyimpan data ke dalam file teks
            save_data_to_txt(data, filename)

if __name__ == "__main__":
    main()
