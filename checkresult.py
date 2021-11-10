import urllib.request as urllib2
import time
import winsound

urlToCheck = 'https://www.comvest.unicamp.br/vestibular-2022'
stringToSearchFor = "GABARITO"

page = urllib2.urlopen(urlToCheck)
pageWithoutResut = page.read().decode('utf-8').upper()

resultNot = pageWithoutResut.count(stringToSearchFor)


while True:
    
    t = 0
    for t in range(5):
        print("."),
        time.sleep(1)
    newPageRaw = urllib2.urlopen(urlToCheck)
    newPage = newPageRaw.read().decode('utf-8').upper()
    newResult = newPage.count(stringToSearchFor)
    if resultNot != newResult :
        while True:
            print("CHANGE DETECTED !!!!!")
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

    if resultNot == newResult :
        print("-------------------------   " + str(resultNot) + " - " + str(newResult) + "   ------------------------")
        i = 0
        lastIndex = 0
        for i in range(newResult):
            a = newPage.index(stringToSearchFor,lastIndex)
            lastIndex = a + 9
            print(str(i+1) + "-"),
            print("..." + newPage[a-50:a+50] + "...")
            
    
    