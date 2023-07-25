import os
from jinja2 import Environment, FileSystemLoader
import json

# Change the working directory to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Get the current directory name
dir_name = os.path.basename(os.getcwd())

# JSONファイルの読み込み
with open("test.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Jinja2環境の設定
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# テンプレートにデータを適用
html_output = template.render(data)

# HTMLファイルとして出力、出力するファイル名を現在のフォルダ名.htmlにする
with open(f"{dir_name}.html", "w", encoding='utf-8') as html_file:
    html_file.write(html_output)
