from rest.restapi import restAPI

def dance():
    rest = restAPI("/api/dance")
    return rest["url"]

def feed():
    rest = restAPI("/api/feed")
    return rest["url"]

def hug():
    rest = restAPI("/api/hug")
    return rest["url"]

def kiss():
    rest = restAPI("/api/kiss")
    return rest["url"]

def pat():
    rest = restAPI("/api/pat")
    return rest["url"]

def poke():
    rest = restAPI("/api/poke")
    return rest["url"]


def slap():
    rest = restAPI("/api/slap")
    return rest["url"]


def tickle():
    rest = restAPI("/api/tickle")
    return rest["url"]

