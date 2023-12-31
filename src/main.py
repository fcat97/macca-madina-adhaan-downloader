import json
from bs4 import BeautifulSoup

def extract_links(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    links_data = []
    for link in soup.find_all('a', {'id': 'video-title-link'}):
        title: str = link.get('title', '')
        if title.lower().find("adhaan") == -1:
            continue
        url = link.get('href', '')

        links_data.append({
            'title': title,
            'url': url
        })

    return links_data

def save_to_json(links_data, json_file_path):
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(links_data, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    html_file_path = "تسجيلات الحرمين _ Haramain Recordings - YouTube.html"  # Replace with the actual path to your HTML file
    json_file_path = "output.json"  # Replace with the desired output JSON file path

    extracted_links = extract_links(html_file_path)
    save_to_json(extracted_links, json_file_path)

    print(f"Links extracted and saved to {json_file_path}")
