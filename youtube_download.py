# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:09:53 2020

@author: Javier
"""



from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=OWU3EiE-ndM&t=51s').streams[0].download()


#import cv2
#vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
#success,image = vidcap.read()
#count = 0
#while success:
#  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
#  success,image = vidcap.read()
#  print('Read a new frame: ', success)
#  count += 1

