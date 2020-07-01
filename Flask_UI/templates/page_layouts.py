##################################################
## FileName: page_layouts.py
##################################################
## Author: RDinmore
# Date: 2020.06.22
# Purpose: return html to be displayed
# Libs: yattag, flask, urllib
## Path: Flask_UI/templates
##################################################

from yattag import Doc
from flask import url_for
import urllib.parse
import os
import sys
from video import get_videos
import pandas as pd

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4'}


def get_page(page_name):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())

    if page_name == "data_page":
        doc.asis(view_data_page())
    elif page_name == "upload_files":
        doc.asis(upload_files())
    elif page_name == "choose_video":
        doc.asis(choose_video())
    elif page_name == "more_info":
        doc.asis(buttons())
        doc.asis(info_page())
    elif page_name == "learn_face":
        doc.asis(learn_face())
    else:
        doc.asis(buttons())

    doc.asis(footer())
    return doc.getvalue()


def data_page(datatable):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    with tag('div', id='container'):
        doc.asis('<span>This provides a view that our data API is actually working with; it will eventually provide more visibility in order to ensure data is uniform (correctly dimensioned, colored greyscale, etc).</span>')
        html = datatable.to_html()
        doc.asis(html)
    doc.asis(footer())
    return doc.getvalue()

def display_page(directory_in):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    display_image(directory_in)
    doc.asis(footer())
    return doc.getvalue()

def display_image(directory_in):
    doc, tag, text, line = Doc().ttl()
    with tag('div', id='photo-container'):
        doc.asis('<iframe width="1000" height="500" src="' + url_for('video_feed',
                                                                     video_name=directory_in) + '" frameborder="0" allowfullscreen></iframe>')
    return doc.getvalue()

def feature_page():
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            text("Feature under development, please press button below to view example")
            doc.asis('<form action="/">')
            doc.asis('<button type="submit" id="button2" value="view_data" class="tooltip"> PLAY MEDIA <span class="tooltiptext">This page will then allow you to play that file using our technique that will scrape images of faces detected in the video stream, and identify them as a known character (actor) in the stream. Prior to playing the stream, the user can select what they would like to have happen when known faces are identified in the stream (i.e. mute, change the channel, etc.).</br></br>Currently, this function is limited to finding faces in the stream; identifying them has not yet been implemented. You can see, however, that as the stream is played, the face that is detected in the stream is identified and marked by a green square.</span></button>')
            doc.asis('<textarea name="content" id="hide" method="post">choose_video</textarea>')
            doc.asis('</form>')

    doc.asis(footer())
    return doc.getvalue()


def eval_face(response, image_name, output_count):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    doc.asis(footer())

    with tag('div', id='display_face'):
        with tag('div', id='photo-container'):
            doc.asis(response)
            doc.asis('</br>')
            doc.asis('</br>')
            text("Name: " + urllib.parse.unquote_plus(image_name))
            doc.asis('</br>')
            text("Face count: " + str(output_count))
            doc.asis('</br>')
            doc.asis('</br>')
    doc.asis(footer())
    return doc.getvalue()

def info_page():
    doc, tag, text, line = Doc().ttl()
    with tag('div'):
        with tag('div', id='container'):
            with tag('div', id='display_info'):
                doc.asis(
                    '<div class="alert"><span class="closebtn" onclick="this.parentElement.style.display='+"'none'"+';">x</span>')
                text("This is a facial recognition media player. After selecting a media file the software will parse facial images and insert them into the database. ")
                text("These images will then be compared to current images and highlighted if recognized. The images will also be used to continue to grow the facial ")
                text("recognition data set.")
                doc.asis('</br></br>')
                text('At a high level, this project\'s purpose is to be able to compare the image of a face against a database of known faces for identification, utilizing the concept known as Eigenface. Specifically, the vision I have for the way this project will be implemented is to take a video stream and "scrape" faces from it, turn them into X x Y images, then into a vector (XY x 1), and then measure the Euclidean distance between that face and all others in the database. Novel vectors that are outside a certain distance from known faces/vectors (i.e. faces that are in the database) will be classified as not recognized, and vectors that are within the distance will be classified as a certain individual contained within the database. This step could likely be implemented using K-means.')
                text("")
                doc.asis('</div>')

    return doc.getvalue()

def footer():
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('form', id='menu'):
                with tag('footer'):
                    with tag('p'):
                        text("Developed for CIS4390")
                        doc.asis("<br>")
                        text(
                            "Developers: Remee A., Martin L., Luke O., Zihan S., Xinxin W.")

    return doc.getvalue()

def header():
    doc, tag, text, line = Doc().ttl()
    stylesheet = open(os.path.join(sys.path[0], "templates/stylesheet.txt"))

    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8"/>')
            with tag('title'):
                text('Oh My Py')
            with tag('style'):
                doc.asis(stylesheet.read())

    with tag('div', id='container'):
        doc.asis('<a href="'+url_for('home')+'"')
        with tag('div', id='photo-container'):
            doc.stag(
                'img', src='https://raw.githubusercontent.com/remeeliz/ohmypy/master/header.JPG', id="header")
        doc.asis('</a>')

    return doc.getvalue()

def buttons():
    doc, tag, text, line = Doc().ttl()

    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            doc.asis('<form method=post id="menu1"  action="/upload_file" enctype=multipart/form-data>')
            doc.asis('<label id="button1" for="test"  class="tooltip"> SELECT YOUR MEDIA FILE <span class="tooltiptext">The page will allow you to select media files (formatted as .mp4) that have been provided from some source, currently, these are part of the repo itself, and are limited to short clips of the television show "The Office." It is not necessary for the user to provide a novel file.</span></label><br>')
            doc.asis('<textarea name="content" id="hide" method="post">upload_file</textarea>')
            doc.asis('<input type="file" onchange="form.submit()" name="file" id="test" accept="image/png, image/jpeg, video/mp4">')
            doc.asis('</form>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button2" value="view_data" class="tooltip"> PLAY MEDIA <span class="tooltiptext">This page will then allow you to play that file using our technique that will scrape images of faces detected in the video stream, and identify them as a known character (actor) in the stream. Prior to playing the stream, the user can select what they would like to have happen when known faces are identified in the stream (i.e. mute, change the channel, etc.).</br></br>Currently, this function is limited to finding faces in the stream; identifying them has not yet been implemented. You can see, however, that as the stream is played, the face that is detected in the stream is identified and marked by a green square.</span></button>')
                doc.asis('<textarea name="content" id="hide" method="post">choose_video</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button4" value="learn_data" class="tooltip"> LEARN FACE <span class="tooltiptext">In terms of the capabilities of the program, it will be initially trained on an image set derived from main characters in the show "The Office." As the program runs, however, and more faces are discovered, they should allow the model that identifies faces to be updated with these new faces so they can be categorized appropriately (as new characters, or commercial actors). On this page</br></br>, this is simply a mechanism to directly provide the model itself a novel face for incorporation into the model. Ultimately this will be a function that operates automatically during stream playback.</span></button>')
                doc.asis(
                    '<textarea name="content" id="hide" method="post">learn_face</textarea>')
            with tag('form', id='menu'):
                doc.asis('<button type="submit" id="button5" value="database" class="tooltip"> VIEW DATA <span class="tooltiptext">This provides a view that our data API is actually working with; it will eventually provide more visibility in order to ensure data is uniform (correctly dimensioned, colored greyscale, etc).</span></button>')
                doc.asis(
                    '<textarea name="content" id="hide" method="post">database</textarea>')
            with tag('form', id='menu'):
                doc.asis(
                    '<button type="submit" id="button3" value="more_info" > MORE INFO </button>')
                doc.asis(
                    '<textarea name="content" id="hide" method="post">more_info</textarea>')

    return doc.getvalue()

def choose_video():
    doc, tag, text, line = Doc().ttl()
    videolist = get_videos.video_list()
    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            doc.asis('<span> This page will then allow you to play that file using our technique that will scrape images of faces detected in the video stream, and identify them as a known character (actor) in the stream.Prior to playing the stream, the user can select what they would like to have happen when known faces are identified in the stream (i.e.mute, change the channel, etc.). Currently, this function is limited to finding faces in the stream; identifying them has not yet been implemented.You can see, however, that as the stream is played, the face that is detected in the stream is identified and marked by a green square.</span></br></br>')
            with tag('form', id='menu'):
                for video in videolist:
                    videoname = (video[7:])[:-4]
                    if len(videoname) > 0:
                        doc.asis('<button type="submit" id="button2" name="video_name" value="' +
                                 videoname+'">' + videoname + '</button>')
                doc.asis(
                    '<textarea name="content" id="hide" method="post">data_page</textarea>')
    return doc.getvalue()

def video_page(videoname):
    doc, tag, text, line = Doc().ttl()
    doc.asis(header())
    doc.asis(view_data_page(videoname))
    doc.asis(footer())
    return doc.getvalue()

def view_data_page(videoname):
    doc, tag, text, line = Doc().ttl()
    doc, tag, text, line = Doc().ttl()
    with tag('div', id='photo-container'):
        video_url = 'https://ohmypy-summer2020.s3.amazonaws.com/videos/' + videoname + '.mp4'
        doc.asis('<div style="background-color:white"></br></br>')
        doc.asis('<input type="checkbox" for="cb1"><label for="cb1">Block Face</label><input type="checkbox" for="cb2"><label for="cb2">Block Commercials</label><input type="checkbox" for="cb3"><label for="cb3">Replace Face</label></br>')
        doc.asis('<audio controls autoplay><source src="' + video_url + '"></audio></br>')
        doc.asis('<span><strong>This is a mock controller. In the future release the video will be able to be controlled to adjust your media output.</strong></br></br></br>')
        doc.asis('</div>')
        with tag('div', id='photo-container'):
            doc.asis('<iframe width="100%" height="100%" src="'+url_for('video_feed', video_name=videoname)+'" frameborder="0" allowfullscreen></iframe>')
    return doc.getvalue()


def learn_face():
    doc, tag, text, line = Doc().ttl()
    with tag('div', id='container'):
        with tag('div', id='photo-container'):
            with tag('div'):
                doc.asis('<span>In terms of the capabilities of the program, it will be initially trained on an image set derived from main characters in the show "The Office." As the program runs, however, and more faces are discovered, they should allow the model that identifies faces to be updated with these new faces so they can be categorized appropriately (as new characters, or commercial actors).On this page, this is simply a mechanism to directly provide the model itself a novel face for incorporation into the model.Ultimately this will be a function that operates automatically during stream playback.</span></br></br>')
                doc.asis("<strong>Choose an image with a single face to train facial recognition</strong>")
                with tag('div', id='learn_face'):
                    doc.asis('<form method=post enctype=multipart/form-data>')
                    doc.asis(
                        '<label for="file-upload" class="custom-file-upload"><i class="fa fa-cloud-upload"></i>Choose File</label></br>')
                    doc.asis(
                        '<input type="file" name="file" id="file-upload" accept="image/png,image/jpeg" required></br></br>')
                    doc.asis(
                        '<input type="text" name="name_in" placeholder="Eigen Face" required>')
                    doc.asis('</br></br>')
                    doc.asis(
                        '<button type="submit" id="eval_button" value="Upload"> Evaluate </button>')
                    doc.asis('</form>')

    return doc.getvalue()
