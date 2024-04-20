import json

nuclei_poc_path = ""
xray_poc_path = ""
config = {}

def set_nuclei_poc_path(path):
    global nuclei_poc_path
    nuclei_poc_path = path

def get_nuclei_poc_path():
    return nuclei_poc_path

def set_xray_poc_path(path):
    global xray_poc_path
    xray_poc_path = path

def get_xrry_poc_path():
    return xray_poc_path

def get_binary_nuclei():
    return config["nuclei_path"]

def get_binary_xray():
    return config["xray_path"]

def load_config():
    global config
    with open('config.json') as f:
        config = json.load(f)