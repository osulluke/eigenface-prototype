# **EigenFace Filter**

## **Usage**

First, you need to get the environment set up to be able to run the code:
```
pip3 install --user -r requirements.txt
```

Once that is complete, navigate to the `Flask_UI` folder and then start the webserver:

```
cd Flask_UI
python3 main.py
```
Once the server is running, navigate to http://localhost:5000/. From this point, you should be able to interact with our program.
## **Purpose**

At a high level, this project's purpose is to be able to compare the image of a face against a *database* of known faces for identification. Specifically, the vision I have for the way this project will be implemented is to take a video stream and "scrape" faces from it, turn them into X x Y images, then into a vector (XY x 1), and then measure the Euclidean distance between that face and all others in the database. Novel vectors that are outside a certain distance from known faces/vectors (i.e. faces that are in the database) will be classified as not recognized, and vectors that are within the distance will be classified as a certain individual contained within the database. This step could likely be implemented using K-means.

As individuals are identified as known or unknown, different functions a user may desire can be implemented.

In order to accomplish this, here is a high-level list of features and capabilities that I think will likely be needed in order to realize this project - it's by no means complete.

## **Required high-level features**

1. *Create/Compute* a database of known faces to be used as a basis for comparing new/novel faces
2. *Identify* faces in a picture or video stream
3. *Scrape* faces from the video stream and turn them into image files
4. *Transform/Scale/Normalize* scraped faces into an MxN matrix of the same size (it's important that all the vectors be of the same length)
5. *Project* the face-vector into the *FaceSpace* (i.e. the database we computed in step #1)
6. *Compare* that face to other faces/vectors in the database
7. *Grow* the "face" database: update the database with the new faces that have been found/identified in order to increase the ability of the program to recognize facial images

Once this set of capabilities is implemented, it should be rather trivial to implement different user functionalities on top of this basic capability.

### **Expanded discussion of high-level features**

#### 1. *Create/Compute* a database of known faces to be used as a basis for comparing new/novel faces

With regards to the concept of Eigenfaces, the concept of a *database* of faces is used to refer to a large co-variance matrix (i.e. it isn't something that is a traditional relational database such as MySQL or Oracle, etc).

Put simply, there are a set of training faces that are used to construct a matrix **T**; each column of **T** is one of the training images. From this set of images, the "average face" **a** is computed and then a new matrix **Phi** = **Ti - a** is formed.

Each column in this new matrix **Phi_i** represents how much a given face vector **Ti** differs from the average face **a**. Basically it is the "average difference" matrix: it describes *how* a given face is different from the mean face. The "average face" matrix is called **A** and is composed of these differences **Ai**.

From this point, the computation would be infeasible, but Linear Algebra makes it possible: instead of computing the Eigenvectors of the covariance matrix **C = A*A^T**, we can compute the Eigenvectors of a much smaller matrix **A^T * A**. 

This calculation will form set of "vectors" **V = {Vi,...}** that forms a basis upon which images scraped from a video stream can be "projected". From here, it is a simple calculation to compare how close a **new** image is to a **training/known** image (i.e an image that is contained in the database).

Images that are "close enough" are identified. Images that are "far away" are counted as new, turned into vectors (vectorized), placed into a new iteration of the matrix **T** from above, and the calculation is done again - thereby increasing the number of faces that the database (matrix) is capable of recognizing.

See the following for more information:

[Wikipedia article](https://en.wikipedia.org/wiki/Eigenface)

[Computing Eigenfaces](http://www.scholarpedia.org/article/Eigenfaces)

[Computing Eigenfaces with C++](https://eigen.tuxfamily.org/dox/classEigen_1_1EigenSolver.html)

[Practical implementation; getting faces from ghosts](https://towardsdatascience.com/eigenfaces-recovering-humans-from-ghosts-17606c328184)

[Eigenfaces with OpenCV](https://www.learnopencv.com/eigenface-using-opencv-c-python/)

[Eigenfaces with Python](https://pythonmachinelearning.pro/face-recognition-with-eigenfaces/)

#### 2. *Identify* faces in a picture or video stream

In order to have vectors to project onto the database (matrix), it will be necessary to gather faces from a video stream. I think there are a lot of libraries and current technologies that will be able to do this.

[Beginner's guide to OpenCV and Video Processing](https://medium.com/@Ralabs/the-beginners-guide-for-video-processing-with-opencv-aa744ec04abb)

[Haar cascade object detection](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

[OpenCV Python face recognition tutorial](https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/)

[Face detection in 2 minutes with Python/OpenCV](https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81)

[OpenCV face recognition documentation/tutorial](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html)

[OpenCV/Haar cascade Example](http://opencv-tutorials-hub.blogspot.com/2016/03/how-to-do-real-time-face-detection-using-haar-cascade.html)

[OpenCV and C++ for Face detection](https://www.geeksforgeeks.org/opencv-c-program-face-detection/)

#### 3. *Scrape* faces from the video stream and turn them into image files

This step will likely be more or less trivial; slicing the "face component" from a larger image and pushing it along the datapath.

[Scraping Faces](https://www.codementor.io/@shashwatjain661/how-detect-faces-using-opencv-and-python-c-nwyssng68)

[Python and images](https://www.pythonforengineers.com/image-and-video-processing-in-python/)

#### 4. *Transform / Scale / Normalize* scraped faces into an MxN matrix of the same size (it's important that all the vectors be of the same length)

This part of the project will likely be very important, as the idea of an Eigenface is highly dependent on having images that are of similar *size, dimension, and orientation*.

Thus, it will be necessary to do some amount of "pre" processing of images that are scraped from the video stream to ensure that they are the same size (MxN), and same orientation (i.e. no faces are sideways or upside-down) - all faces should be pictures that seem like they have been taken from the same camera, from the same distance, with the same zoom. This may be a sub-step to #3 listed above.

#### 5. *Grow* the "face" database: update the database with the new faces that have been found/identified in order to increase the ability of the program to recognize facial images

When a vector is identified as a face, but is not matched against a face in the database (i.e. its Euclidian distance is too far away from any known face), it will be transformed into a new vector **Ti**, and appended to the original training matrix **T**.

As new vectors (faces) are added to **T**, we will re-compute the Eigenbasis **V = {Vi}** (FaceSpace) from step #1 above so the program can learn to recognize new people.

## **Implementation / Vertical Prototype ideas**

1. As far as actual implementation/Vertical Prototype is concerned, I propose we use a popular TV show such as *The Office* from which to build our training matrix. It would not be difficult to gather high-quality images from the internet of all the actors in that show.
   
2. Instead of using a full 30-minute episode, I suggest we use shorter clips that we can download from YouTube along with other commercials that do not feature actors from the show.

## **Production version**

1. In terms of the actual full system, I think a few libraries / languages could be used:

   * C / C++
   * OpenCV
   * Linear Algebra Libraries:
     * [Armadillo](http://arma.sourceforge.net/)
     * [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page)
