def coeficentsToPolynomial(imput):
    listIn = imput.split(",")
    strOut = ""
    degree = len(listIn)
    for i in listIn:
        strOut = strOut+i+"x^"+str(degree)+"+"
        degree -= 1
    strOut = strOut.strip("+")
    return (strOut)

print(coeficentsToPolynomial(input("text: ")))
