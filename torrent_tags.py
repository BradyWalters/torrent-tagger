import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import re

qbitUrl = sys.argv[1]
if qbitUrl[-1] == "/":
    qbitUrl = qbitUrl[:-1]
nameRegex = sys.argv[2]
tag = sys.argv[3]

with urlopen(qbitUrl + "/api/v2/torrents/info") as response:
    jsonObject = json.loads(response.read().decode("utf-8"))

def getFiltedHashList(torrentList, nameRegex):
    filteredHashes = []
    for torrent in torrentList:
        if re.search(nameRegex, torrent["name"], flags=re.IGNORECASE) != None:
            filteredHashes.append(torrent["hash"])
    
    return filteredHashes

def getAddTagsBody(hashList, tag):
    bodyString = "hashes="
    for hash in hashList:
        bodyString += (hash + "|")

    bodyString = bodyString[:-1]
    bodyString += ("&tags=" + tag)

    return bodyString


filteredHashes = getFiltedHashList(jsonObject, nameRegex)
bodyString = getAddTagsBody(filteredHashes, tag).encode("utf-8")

postReq = Request((qbitUrl + "/api/v2/torrents/addTags"), method="POST")
postReq.add_header("Content-Type", "application/x-www-form-urlencoded")
try:
    urlopen(postReq, data=bodyString)
except HTTPError as e:
    print("Something went wrong", file=sys.stderr)
    print("Error code: ", e.code, file=sys.stderr)
