
import requests

def restAPI(endpoint):
    http = requests.get("https://usagiapi.danielagc.repl.co/api/" + endpoint)
    return http.json()["url"]
