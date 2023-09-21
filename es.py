import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
#os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
def process(filename):
    import os
    #os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
    IMAGE_PATH = filename
    print("filepath==",IMAGE_PATH)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(IMAGE_PATH,paragraph="True")
    #print("result",result[0])
    es=str(result[0])
    resultString = es.rsplit(',', 1)[1]
    print("resultString==",resultString)
    finalres=resultString[2:-2]
    print("finalres==",finalres)
    return finalres
#process("demo3.png")