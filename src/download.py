import youtube_dl
import json

# step 1
# download youtube-dl nightly src file, extract, and put youtube-dl folder to current directory

def download_videos(video_urls, output_path='.', options=None, progress_file='progress.json'):
    try:
        with open(progress_file, 'r') as f:
            progress_data = json.load(f)
    except FileNotFoundError:
        progress_data = {}

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }

    if options:
        ydl_opts.update(options)

    for url in video_urls:
        if url in progress_data and progress_data[url] == 'completed':
            print(f"Skipping {url} - Already downloaded")
            continue

        print(f"Downloading: {url}")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        progress_data[url] = 'completed'

    with open(progress_file, 'w') as progress_file:
        json.dump(progress_data, progress_file, indent=2)

if __name__ == "__main__":
    output_file = "output2.json"  # Path to the output JSON file
    output_directory = "./videos/"  # Replace with the desired output directory

    with open(output_file, 'r') as json_file:
        data = json.load(json_file)
        youtube_urls = [item['url'] for item in data]

    download_videos(youtube_urls, output_directory)
