# Final Project: CST 205
# Team 798
# Members:
# #   Hasem Trejo
# #   Justin Ho
# #   Jaden Bussard
# #   Autumn Benton

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from pagesInfo import info
import random
from PIL import Image
import math

app = Flask(__name__)
bootstrap = Bootstrap(app)



@app.route('/')
def home():
    #random.shuffle(info)
    title = info[0][2]
    temp = info[0][3]
    return render_template('homeTemplate.html', name=title)


@app.route('/page1/')
def page1():
    #Autumn's Page
    myImage = Image.open('static/jelly.jpg')
    background = Image.open("static/csumb.jpg")
    negatives(myImage)
    greys(myImage)

    return render_template('p1Template.html')



@app.route('/page2/')
def page2():
    #Hasem's Page: use p2template
    
    return render_template('p2Template.html')


@app.route('/page3/')
def page3():
    #Justin's Page: use p3template
    
    return render_template('p3Template.html')


@app.route('/page4/')
def page4():
    #Jaden's Page: use p4template
    
    return render_template('p4Template.html')


#Any extra functions go down here

def sepia(im):
    new_list=[]
    for p in im.getdata():
        new_list.append((p[0], p[1]//2, p[2]//2))
        im.putdata(new_list)
    im.save('static/imSepia.jpg')

def negatives(im):      
    negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
    im.putdata(negative_list)
    im.save('static/imNegative.jpg')

def greys(im):
    new_list = [( (a[0]+a[1]+a[2])//3, ) * 3 for a in im.getdata() ]
    im.putdata(new_list)
    im.save('static/imGrey.jpg')



