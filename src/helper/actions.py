import sys
import subprocess
import time
import json

voiceAction = {}
voiceResponse = {}

def load_data(data):
    with open(data) as json_file:
        data = json.load(json_file)
        global voiceAction,voiceResponse
        voiceAction = data["action"]
        voiceResponse = data["response"]

def terminal(cmd):
    time.sleep(1)
    cmd = ";sleep 2;".join(cmd.split(";"))
    subprocess.Popen(["/bin/bash", "-c", cmd])
    time.sleep(0.05)

def action(cmd):
    if(cmd in voiceAction):
        terminal(voiceAction[cmd])
        return True
    else:
        print("Action for the command not found")
        return False

def preprocess(message):
    message = message.replace("plus ","+")
    message = message.replace("close","run pkill")
    return message
    
def process(message):
    if message=="stop listening" or message=="quit":
        print("Thank you! See you again!")
        sys.exit()
    
    message = preprocess(message)
    
    if message.startswith("open"): # CHECKS DICTIONARY
        message = message.replace("open","run")
        if action(message):
            pass
    if message.startswith("run"): # EXECUTES COMMAND
        message = message[4:]
        print("Running bash command:",message)
        terminal(message)
    else:
        action(message)
