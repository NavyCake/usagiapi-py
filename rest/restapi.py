
import requests

def restAPI(endpoint):
    http = requests.get("https://usagiapi.danielagc.repl.co" + endpoint)
    return http.json()