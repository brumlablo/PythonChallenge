import urllib.request
import re
import pickle
import zipfile

def readIt(url):
    # get the url comments
    html = urllib.request.urlopen(url).read().decode()
    return html


def analyseComments(html):
    comments = re.findall("<!--(.*)-->", html, re.DOTALL)
    return comments


def shiftalpha(toDec):
    out = ""
    for ch in toDec:
        if "a" <= ch <= "z":
            out += chr(((ord(ch) + 2) - ord("a")) % 26 + ord("a"))
        else:
            out += ch
    print(out)


def countrare(todec):
    # count the occurence of characters in string
    rarity = {}
    for c in todec:
        if c in rarity:
            rarity[c] = (rarity[c] + 1)
        else:
            rarity[c] = 1

    # sort the dict by values
    rarity_sorted = sorted(rarity, key=rarity.get)
    result = ""
    for k in rarity_sorted:
        if rarity[k] <= 2:
            result += k
        # print("{} : {}".format(k, rarity[k]))
    print(result)


def find3(todec):
    big3 = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', todec, re.DOTALL)
    result = ""
    for c in big3:
        result += c
    print(result)


# find number in html
def findnumber(url):
    html = urllib.request.urlopen(url).read().decode()
    found = re.search('([0-9]+)$', html)
    if found is None:
        # print(html + " a jsme tu: " + url)
        # divide by 2
        todiv = re.search('.*=([0-9]+)$', url)
        if todiv is not None and html == "Yes. Divide by two and keep going.":
            return str(int(int(todiv.group(1)) / 2))
        else:
            # result...
            return html
    else:
        return found.group(1)


def numberz(url):
    urlgroups = re.match('(.*=)([0-9]+)$', url)

    foundNext = urlgroups[2]
    tmp = ""
    while True:
        # get number of new url from html
        foundNext = findnumber(url)
        print(foundNext)
        try:
            float(foundNext)
        except ValueError:
            break
        # form new url
        url = urlgroups[1] + foundNext
    print(foundNext)


def deserialize(url):
    res = ""
    html = pickle.load(urllib.request.urlopen(url))
    for item in html:
        for val, count in item:
            res += str(val) * count
        res += "\n"
    print(res)

def openzip(zip_name):
    if not zipfile.is_zipfile(zip_name):
        raise ValueError('Could not read zip file: ' + zip_name)
    zf = zipfile.ZipFile(zip_name, 'r')
    hint = '90052'
    res = ""
    while 42:
        data = zf.read(hint + ".txt").decode("utf-8")
        res += zf.getinfo(hint + ".txt").comment.decode("utf-8")
        found = re.search('([0-9]+)$', data)
        if found is None:
            break
        else:
            hint = found[0]
    print(res)
    zf.close()