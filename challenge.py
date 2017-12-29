import parseurl


def cha1():
    print(2 ** 38)


def cha2(toDec):
    out = ""
    for ch in toDec:
        if "a" <= ch <= "z":
            out += chr(((ord(ch) + 2) - ord("a")) % 26 + ord("a"))
        else:
            out += ch

    print(out)


def cha3():
    comments = parseurl.readIt("http://www.pythonchallenge.com/pc/def/ocr.html")
    parseurl.countrare(comments[0][50:])

def cha4():
    comments = parseurl.readIt("http://www.pythonchallenge.com/pc/def/equality.html")
    print(comments)


def main():
    cha1()
    print("-------------------------------------------------")
    cha2("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr" \
         " ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
    cha2("map")
    print("-------------------------------------------------")
    cha3()


if __name__ == "__main__":
    main()
