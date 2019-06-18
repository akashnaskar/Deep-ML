#!/usr/bin/env python
# coding: utf-8



from flask import Flask, request #import main Flask class and request object
import traceback
from IPython import get_ipython
app = Flask(__name__) #create the Flask app



@app.route('/query-example')
def query_example():
    videoFull = request.args.get('video') #if key doesn't exist, returns None
    vidName = videoFull.split('.')[0]
    print(vidName)
#     !ipython two_digits.py 2 3
#     %run two_digits 3 5                   https://softwebsolutions.co.in/Upload/5_June.mp4
    if videoFull == '5_June.mp4':
        try:
#             %python main.py --data data/Cam_10_1_V.yml --video video/Cam_10_1_V.mp4
            get_ipython().system('python main.py --data data/coordinates_jay.yml --video videos/5_June.mp4')
        except:
            traceback.print_exc()        
        return '''<h1>The running video is: {}</h1>'''.format(videoFull)
    elif videoFull == '6_June.mp4':
        try:
#             %python main.py --data data/Cam_10_1_V.yml --video video/Cam_10_1_V.mp4
            get_ipython().system('python main.py --data data/coordinates_jay.yml --video videos/6_June.mp4')
        except:
            traceback.print_exc()        
        return '''<h1>The running video is: {}</h1>'''.format(videoFull)
    elif videoFull == '7_June.mp4':
        try:
#             %python main.py --data data/Cam_10_1_V.yml --video video/Cam_10_1_V.mp4
            get_ipython().system('python main.py --data data/coordinates_jay.yml --video videos/7_June.mp4')
        except:
            traceback.print_exc()        
        return '''<h1>The running video is: {}</h1>'''.format(videoFull)
    else:
        return '''<h1>The video is: {}</h1>'''.format(videoFull)


if __name__ == '__main__':
    print('out main')
    # start api
    app.run(host='192.168.4.11', port=8000) #run app in debug mode on port 5000   debug=True,


