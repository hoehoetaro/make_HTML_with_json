import os
import json

# Change the working directory to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Get the current folder name
current_folder_name = os.path.basename(os.getcwd())

# Create the data to output
data = {
    "title": {
        "type": "title",
        "name": current_folder_name,
        "thumbnail_source": f"{current_folder_name}_thumbnail.png"
    },
    "contents": []
}

# Serialize to JSON format and write to a file
with open(f'{current_folder_name}_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
