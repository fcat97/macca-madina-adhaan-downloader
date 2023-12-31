import json
from bs4 import BeautifulSoup

# open https://www.youtube.com/@Haramain_Recordings/videos in browser and scroll down as much as you want
# save the webpage with ctrl+s
# put the downloaded html file inside /website/ directory
# copy the relative path of the html file
# set it to `html_file_path` variable

def extract_distinct_links(html_file_path, json_file_path='output.json', progress_file='progress.json'):
    try:
        with open(progress_file, 'r') as progress_file:
            progress_data = json.load(progress_file)
            processed_combinations = set(progress_data.get('processed_combinations', set()))
    except FileNotFoundError:
        processed_combinations = set()

    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    links_data = []

    # select all <a id="video-title-link"> tag
    for link in soup.find_all('a', {'id': 'video-title-link'}):
        title: str = link.get('title', '')
        url = link.get('href', '')

        if title.lower().find("adhaan") == -1:
            continue

        # Split the title by space and get <time> and <name> using indices
        title_parts = title.split()
        if len(title_parts) >= 5:
            time = title_parts[4].strip()

        if len(title_parts) >= 7:
            name = ' '.join(title_parts[6:]).strip()

        if time in ["Dhuhr", "'Asr", "Maghrib", "'Isha"]:
            time = "OtherWaqt"
        

        # Check if the combination of <time> and <name> is unique
        combination = f"{time}_{name}"
        if combination not in processed_combinations:
            links_data.append({
                'title': title,
                'url': url
            })
            processed_combinations.add(combination)

    # Save the processed_combinations set to the progress file
    progress_data = {'processed_combinations': list(processed_combinations)}
    with open(progress_file, 'w', encoding='utf-8') as progress_file:
        json.dump(progress_data, progress_file, indent=2, ensure_ascii=False)

    # Save the links data to the output JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(links_data, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    html_file_path = "تسجيلات الحرمين _ Haramain Recordings - YouTube.html"  # Replace with the actual path to your HTML file
    json_file_path = "output2.json"  # Replace with the desired output JSON file path
    progress_file = "muajjin.json"  # Replace with the progress JSON file path

    extract_distinct_links(html_file_path, json_file_path, progress_file)

    print(f"Links extracted and saved to {json_file_path}")
