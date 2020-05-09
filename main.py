import cv2

def paintToFieldToAverageColor(colors):
    red, green, blue=colors
#    print(str(k) + ". alan boyandı  x=" + str(dotx) + " y= " + str(doty))
    for line in range(0,lengthOfASquare):
        for column in range (0,lengthOfASquare):
            img.itemset((column+doty, line+dotx, 0), red)
            img.itemset((column+doty, line+dotx, 1), green)
            img.itemset((column+doty, line+dotx, 2), blue)
def Average(lst):
    return sum(lst) / len(lst)
def averageOfField(dotx,doty):
    red=[]
    green=[]
    blue=[]
    averageRed=[]
    averageGreen=[]
    averageBlue=[]
    for column in range (1,lengthOfASquare):
        for line in range (1,lengthOfASquare):

            red.append(img[column+doty,line+dotx][0])
            green.append(img[column+doty,line+dotx][1])
            blue.append(img[column+doty,line+dotx][2])

        averageRed.append(Average(red))
        averageGreen.append(Average(green))
        averageBlue.append(Average(blue))

    return int(Average(averageRed)),int(Average(averageGreen)),int(Average(averageBlue))
def showTheImage():
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def getNextDot(dotx,doty):
    if(dotx+(lengthOfASquare*2) >= imageWidth):
        dotx=1
        doty=doty+lengthOfASquare
    else:
        dotx=dotx+lengthOfASquare
    return dotx,doty
def getSimilarColor(avgColors):

    avgRed, avgGreen, avgBlue=avgColors
    diffrence=[]
    for i in range (0,len(smartCupeColors)):
        diffrence.append(abs((smartCupeColors[i][0]-avgRed))+abs((smartCupeColors[i][1]-avgGreen))+abs((smartCupeColors[i][2]-avgBlue)))
    best=0
    for i in range (0,len(diffrence)-1):
        if(abs(diffrence[0])>abs(diffrence[i+1])):
            diffrence[0]=diffrence[i+1]
            best=i+1
    #print(str(best)+" renkler= "+str(smartCupeColors[best]))
    return best
def getMainColor(number):
    colorname=smartCupeColors[number][3]
    a=2
    if (colorname=="Mavi"):
        a= 0
    elif(colorname=="Yesil"):
        a= 1
    elif (colorname=="K"):
        a= 2
    elif (colorname=="Turuncu"):
        a= 3
    elif (colorname=="Beyaz"):
        a= 4
    elif (colorname=="Sarı"):
        a= 5
    elif (colorname=="Siyah"):
        a= 6
    return mainColors[a]
#tanımlamalar
img = cv2.imread('test.png')
lengthOfASquare=3
imageWidth = img.shape[1]
imageHeight = img.shape[0]
dotx=1
doty=1
mainColors=[]
mainColors.append((255,0,0))#mavi
mainColors.append((0,255,0))#yeşil
mainColors.append((0,0,255))#kırmızı
mainColors.append((255,128,0))#turuncu
mainColors.append((255,255,255))#beyaz
mainColors.append((0,255,255))#sarı
mainColors.append((0,0,0))#Siyah

smartCupeColors=[]

#sarı-----------------
smartCupeColors.append((61,82,160,"Sarı"))
smartCupeColors.append((99,124,218,"Sarı"))
smartCupeColors.append((111,158,239,"Sarı"))
smartCupeColors.append((125,162,239,"Sarı"))
smartCupeColors.append((93,101,172,"Sarı"))
smartCupeColors.append((121,157,229,"Sarı"))
smartCupeColors.append((131,186,253,"Sarı"))
smartCupeColors.append((92,137,204,"Sarı"))
smartCupeColors.append((113,184,222,"Sarı"))
smartCupeColors.append((93,156,204,"Sarı"))
smartCupeColors.append((105,172,217,"Sarı"))
#Beyaz----------------
smartCupeColors.append((187,220,237,"Beyaz"))
smartCupeColors.append((189,242,253,"Beyaz"))
smartCupeColors.append((196,243,253,"Beyaz"))
smartCupeColors.append((200,242,251,"Beyaz"))
smartCupeColors.append((195,238,253,"Beyaz"))
smartCupeColors.append((188,216,231,"Beyaz"))
#Siyah----------------
smartCupeColors.append((5,4,20,"Siyah"))
smartCupeColors.append((10,5,46,"Siyah"))
smartCupeColors.append((39,19,27,"Siyah"))
smartCupeColors.append((31,49,81,"Siyah"))
smartCupeColors.append((21,23,23,"Siyah"))
#Kırmızı-------------
smartCupeColors.append((96,76,232,"K"))
smartCupeColors.append((77,67,221,"K"))
smartCupeColors.append((91,94,203,"K"))
smartCupeColors.append((104,118,224,"K"))
smartCupeColors.append((0,0,255,"K"))
smartCupeColors.append((48,48,255,"K"))
smartCupeColors.append((44,44,238,"K"))
smartCupeColors.append((38,38,205,"K"))
smartCupeColors.append((26,26,139,"K"))
smartCupeColors.append((11,11,200,"K"))
smartCupeColors.append((117,117,235,"K"))
smartCupeColors.append((70,70,168,"K"))
smartCupeColors.append((22,22,132,"K"))
smartCupeColors.append((49,49,198,"K"))
smartCupeColors.append((49,79,198,"K"))
smartCupeColors.append((50,100,198,"K"))
smartCupeColors.append((50,110,200,"K"))
# yeşil------------------
smartCupeColors.append((98,233,30,"Yesil"))
smartCupeColors.append((141,240,91,"Yesil"))
smartCupeColors.append((183,240,155,"Yesil"))
smartCupeColors.append((166,175,86,"Yesil"))
smartCupeColors.append((79,152,43,"Yesil"))
smartCupeColors.append((54,142,9,"Yesil"))
smartCupeColors.append((31,218,62,"Yesil"))
smartCupeColors.append((44,189,68,"Yesil"))
smartCupeColors.append((93,166,106,"Yesil"))
smartCupeColors.append((45,233,114,"Yesil"))
smartCupeColors.append((128,242,195,"Yesil"))
smartCupeColors.append((102,240,192,"Yesil"))
smartCupeColors.append((106,238,192,"Yesil"))
#Mavi-----------------
smartCupeColors.append((220,26,39,"Mavi"))
smartCupeColors.append((226,92,101,"Mavi"))
smartCupeColors.append((161,27,36,"Mavi"))
smartCupeColors.append((218,112,119,"Mavi"))
smartCupeColors.append((223,86,45,"Mavi"))
smartCupeColors.append((238,127,94,"Mavi"))
smartCupeColors.append((156,48,15,"Mavi"))
smartCupeColors.append((203,63,20,"Mavi"))
smartCupeColors.append((219,171,13,"Mavi"))
smartCupeColors.append((240,200,68,"Mavi"))
smartCupeColors.append((242,213,117,"Mavi"))
smartCupeColors.append((192,170,97,"Mavi"))
smartCupeColors.append((145,28,19,"Mavi"))

print("Image width= " + str(imageWidth) + " Image Height = " + str(imageHeight))


while (True):
    paintToFieldToAverageColor(getMainColor(getSimilarColor(averageOfField(dotx, doty))))
    dotx,doty = getNextDot(dotx, doty)
    if (doty+lengthOfASquare > imageHeight):
        break

showTheImage()
