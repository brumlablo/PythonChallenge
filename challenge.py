import parseurl
import re


def cha1():
    print(2 ** 38)


def cha2():
    parseurl.shiftalpha("g fmn3c wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw "
                              "fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq "
                              "pcamkkclbcb. lmu ynnjw ml rfc spj.")
    parseurl.shiftalpha("map")

def cha3():
    comments = parseurl.readIt("http://www.pythonchallenge.com/pc/def/ocr.html")
    parseurl.countrare(comments[0][50:]) #todo: fix this piggy thingy

def cha4():
    comments = parseurl.readIt("http://www.pythonchallenge.com/pc/def/equality.html")
    result = parseurl.find3(comments[0])

def cha5():
    parseurl.numberz("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")

def runFunc(ch_n):
    # call chosen challenge
    return globals()['cha' + ch_n]

def main():

    #input jungle
    while(True):
        ch_n = input("challenge number? [1-33] or run all [ALL/all] or quit program [Q/q]?\n")

        if ch_n == "q" or ch_n == "Q":
            exit(0)
        #run all
        elif ch_n == "ALL" or ch_n == "all":
            i = 1
            while True:
                try:
                    func = runFunc(str(i))
                except KeyError:
                    break
                else:
                    func()
                i += 1
            break #done
        # test if function number is valid, if not, another prompt
        else:
            try:
                int(ch_n)
            except ValueError:
                print("Wrong input...\n")
                continue
            else:
                # run one with valid name
                try:
                    func = runFunc(ch_n)
                except KeyError:
                    print("There is no such function! I'm working on it :)...")
                else:
                    func()
                    print("---------------------------------------------------------")
                    break #done


if __name__ == "__main__":
    main()
