import urllib.request
import re


def readIt(url):

    #get tyhe url comments
    html = urllib.request.urlopen(url).read().decode()
    comments = re.findall("<!--(.*)-->", html, re.DOTALL)
    return comments

def countrare(todec):
    #count the occurence of characters in string
    rarity = {}
    for c in todec:
        if c in rarity:
            rarity[c] = (rarity[c] + 1)
        else:
            rarity[c] = 1

    #sort the dict by values
    rarity_sorted = sorted(rarity, key=rarity.get)
    result = ""
    for k in rarity_sorted:
        if rarity[k] <= 2:
            result += k
        #print("{} : {}".format(k, rarity[k]))
    print(result)



