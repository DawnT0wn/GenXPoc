import json

nuclei_poc_path = ""
xray_poc_path = ""
config = {}
nuclei_path = ""
xray_path = ""

def set_nuclei_poc_path(path):
    global nuclei_poc_path
    nuclei_poc_path = path

def get_nuclei_poc_path():
    return nuclei_poc_path

def set_xray_poc_path(path):
    global xray_poc_path
    xray_poc_path = path

def get_xray_poc_path():
    return xray_poc_path

def get_binary_nuclei():
    return nuclei_path

def get_binary_xray():
    return xray_path

def set_binary_xray(path):
    xray_path = path

def set_binary_nuclei(path):
    nuclei_path = path

def load_config():
    global config
    global xray_path
    global nuclei_path
    with open('config.json') as f:
        config = json.load(f)
    xray_path = config["xray_path"]
    nuclei_path = config["nuclei_path"]