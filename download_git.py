import requests
import subprocess

organisation="tryton"

repo_data = requests.get(
    "https://api.github.com/orgs/{organisation}/repos?per_page=1000".format(
        organisation=organisation))
for repo in repo_data.json():

    proc = subprocess.Popen(
        ["git", "clone", repo['html_url'], "--branch", "5.0"],
        stdout=subprocess.PIPE
    )
    proc.communicate()
