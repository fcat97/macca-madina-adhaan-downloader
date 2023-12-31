# Download Macca Madina Adhaan from youtube

---

### Step 1: configure parser
- open main2.py file
- open https://www.youtube.com/@Haramain_Recordings/videos in browser and scroll down as much as you want
- save the webpage with ctrl+s
- put the downloaded html file inside /website/ directory
- copy the relative path of the html file
- set it to `html_file_path` variable
- run `python ./src/main2.py`

### Step 2: download video
- download youtube-dl nightly src file, extract, and put youtube-dl folder to current directory
- run `python download.py`
