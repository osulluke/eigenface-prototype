# Page functionality descriptions.

## Home page

At a high level, this project's purpose is to be able to compare the image of a face against a *database* of known faces for identification, utilizing the concept known as **Eigenface**. Specifically, the vision I have for the way this project will be implemented is to take a video stream and "scrape" faces from it, turn them into X x Y images, then into a vector (XY x 1), and then measure the **Euclidean distance** between that face and all others in the database. Novel vectors that are outside a certain distance from known faces/vectors (i.e. faces that are in the database) will be classified as not recognized, and vectors that are within the distance will be classified as a certain individual contained within the database. This step could likely be implemented using K-means.

## Select your media file

The page will allow you to select media files (formatted as .mp4) that have been provided from some source, currently, these are part of the repo itself, and are limited to short clips of the television show "The Office." **It is not necessary for the user to provide a novel file.**

## Play media

This page will then allow you to play that file using our technique that will scrape images of faces detected in the video stream, and identify them as a known character (actor) in the stream. Prior to playing the stream, the user can select what they would like to have happen when known faces are identified in the stream (i.e. mute, change the channel, etc.).

Currently, this function is limited to finding faces in the stream; identifying them has not yet been implemented. You can see, however, that as the stream is played, the face that is detected in the stream is identified and marked by a green square.

## Learn face

In terms of the capabilities of the program, it will be initially trained on an image set derived from main characters in the show "The Office." As the program runs, however, and more faces are discovered, they should allow the model that identifies faces to be updated with these new faces so they can be categorized appropriately (as new characters, or commercial actors).

On this page, this is simply a mechanism to directly provide the model itself a novel face for incorporation into the model. Ultimately this will be a function that operates automatically during stream playback.

## View data

This provides a view that our data API is actually working with; it will eventually provide more visibility in order to ensure data is uniform (correctly dimensioned, colored greyscale, etc).

## More info

Provides a user expanded information regarding the sites' operation.