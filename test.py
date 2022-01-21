from PASE.processing.camera import prespective
from PASE.sensors.camera import fetch
import cv2
import numpy as np
import matplotlib.pyplot as plt
import yaml

if __name__ == "__main__":
    with open('PASE/config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        frame = fetch.Camera(data['BACK_CAM_SMALL'],True,data['extension'])
        height = data['output_image_height']
        width = data['output_image_width']
        w_1 = data['w_1']
        w_2 = data['w_2']
        w_3 = data['w_3']
        w_4 = data['w_4']

        h_1 = data['h_1']
        h_2 = data['h_2']
        src = [(w_1,h_1),(w_2,h_1),(w_3,h_2),(w_4,h_2)]
        vision=prespective.TopVis([width,height],frame='Output',src=src)
        nxt=True
        while(nxt):
            img,nxt=frame.get()
            if nxt:
                img=vision.transform(img)
                cv2.imshow('View',img)
            if cv2.waitKey(3000)==27:
                cv2.destroyAllWindows()
                break