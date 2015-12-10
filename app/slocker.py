############################
#### Slocker - DockerHub to Slack Hook
#### v1.0 - Julien Stroheker
############################
#### Before run this awesome project you need to :
#### 1. to define a OS variable Slack_Hook_Url...
####    Example : export Slack_Hook_Url='https://hooks.slack.com/services/XXXXXXXX/XXXXX/XXXXXXX'
#### 2. Edit the redirectChannel.json
####    Example : "NameUserDocker/NameRepoDocker":"#YourSlackChannel"
#### 3. Execute the slocker.py file
####    python2 slocker.py
############################
############################
#### Import
############################
from flask import Flask
from flask import jsonify
from flask import request
from flask import json
import requests
import os
############################
#### Global Variables
############################
url = os.environ['Slack_Hook_Url']
docker_icon_url = 'https://pbs.twimg.com/profile_images/378800000124779041/fbbb494a7eef5f9278c6967b6072ca3e_200x200.png'
headers = {'content-type': 'application/json'}
############################
#### Define
############################
def SearchRepoName(repo_name):
    with open('redirectChannel.json', 'r') as json_file:
        channel_selector = json.load(json_file)
    if repo_name in channel_selector:
        return channel_selector[repo_name]
    else:
        return None
############################
#### API
############################
app = Flask(__name__)
############################
#### Hello World
############################
@app.route('/')
def Hello():
   return '...Relay ON....'
############################
#### Where the magic is...
############################      
@app.route('/', methods=['POST'])
def ReceiveBuild():
    value = request.json    
    if request.json:
        app.logger.debug("JSON received...")
        valueRepo=value.get("repository")
        valueURL=valueRepo.get("repo_url")
        valueName=valueRepo.get("repo_name")
        toSend= {
            'channel': SearchRepoName(valueName),
            'username': 'Docker Hub',
            'text': '<{}|{}> built successfully.'.format(valueURL, valueName),
            'icon_url': docker_icon_url
        }
        app.logger.debug("Creation Respond...")
        app.logger.debug(json.dumps(toSend))
        return requests.post(url, data=json.dumps(toSend), headers=headers)
        app.logger.debug("Respond SENT")
    else:
        return "Error..."
############################
#### Config
############################
if __name__ == "__main__":
        app.debug = False
        app.run(host='0.0.0.0', port=8080)
    
