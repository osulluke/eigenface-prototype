import sys
sys.path.append("..")
from filestore import *

aws_path = "https://ohmypy-summer2020.s3.amazonaws.com/"
videolist = get_s3objectList("videos/")

def video_list():
    return videolist["Key"]