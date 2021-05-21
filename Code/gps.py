from gmplot import gmplot
import csv

gmap=gmplot.GoogleMapPlotter(19.128601,72.9279,15)
gmap.coloricon= "http://www.googlemapsmarkers.com/v1/%s/"

with open("data.csv", 'r', encoding="cp437", errors='ignore') as f:
    reader=csv.reader(f)
    k=0
    for row in reader:
        lat=float(row[0])
        long=float(row[1])


        if(k==0):
            gmap.marker(lat,long,'yellow')
            k=1
        else:
            gmap.marker(lat,long,'blue')
gmap.marker(lat,long,'red')
gmap.draw("mymap.html")
