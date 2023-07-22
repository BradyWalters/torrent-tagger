import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json

qbitUrl = sys.argv[1]
if qbitUrl[-1] == "/":
    qbitUrl = qbitUrl[:-1]
nameSearch = sys.argv[2]
tag = sys.argv[3]

with urlopen(qbitUrl + "/api/v2/torrents/info") as response:
    jsonObject = json.loads(response.read().decode("utf-8"))

def getFiltedHashList(torrentList, nameSearch):
    filteredHashes = []
    for torrent in torrentList:
        if nameSearch in torrent["name"]:
            filteredHashes.append(torrent["hash"])
    
    return filteredHashes

def getAddTagsBody(hashList, tag):
    bodyString = "hashes="
    for hash in hashList:
        bodyString += (hash + "|")

    bodyString = bodyString[:-1]
    bodyString += ("&tags=" + tag)

    return bodyString


filteredHashes = getFiltedHashList(jsonObject, nameSearch)
bodyString = getAddTagsBody(filteredHashes, tag).encode("utf-8")

postReq = Request((qbitUrl + "/api/v2/torrents/addTags"), method="POST")
postReq.add_header("Content-Type", "application/x-www-form-urlencoded")
try:
    urlopen(postReq, data=bodyString)
except HTTPError as e:
    print("Something went wrong", file=sys.stderr)
    print("Error code: ", e.code, file=sys.stderr)
