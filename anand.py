#!/usr/bin/env python3

import os

orderNumbers = open("orders.txt", "r")  #Order numbers to match

#Network path to a directory of files that has full details of the order
directoryEntries = os.scandir("")
outputFile = open("matchedData.dat", "w")

for entry in directoryEntries:
    print("Currently parsing file ", entry.path)
    fullOrderData = open(entry.path, "r")
    #loop through each order from the ordernumber file
    for orderNo in OrderNumbers:
        for row in fullOrderData:
            if orderNo.strip() in row:
                outputFile.write(row)
        #go back to start of orderdetails data to match on next order number
        fullOrderData.seek(0)
    #go back to order numbers again to match on the next order details file
    orderNumbers.seek(0)
    fullOrderData.close()
OrderNumbers.close()
outputFile.close()
print("done")
