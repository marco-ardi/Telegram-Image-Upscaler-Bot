import cv2
from cv2 import dnn_superres
#creating an sr object
class imageEnhancer:
    sr2 = dnn_superres.DnnSuperResImpl_create()
    sr3 = dnn_superres.DnnSuperResImpl_create()
    sr4 = dnn_superres.DnnSuperResImpl_create()

    def __init__(self):
        #sr2 = dnn_superres.DnnSuperResImpl_create()
        self.sr2.readModel("./models/EDSR_x2.pb")
        self.sr2.setModel("edsr", 2)
        self.sr3.readModel("./models/EDSR_x3.pb")
        self.sr3.setModel("edsr", 3)
        self.sr4.readModel("./models/EDSR_x4.pb")
        self.sr4.setModel("edsr", 4)
    
    def Enhance(self, sr_type : str) : 
        img = cv2.imread("./input.png")
        if sr_type == "x2":
            result = self.sr2.upsample(img)
        elif sr_type == "x3":
            result = self.sr3.upsample(img)
        elif sr_type == "x4":
            result = self.sr2.upsample(img)
        cv2.imwrite("./output.png", result)
    #sr = dnn_superres.DnnSuperResImpl_create()

    #image = cv2.imread("./input.png")
    #load the desired model
    #path = "./models/EDSR_x4.pb"
    #sr.readModel(path)
    #set the desired model and scale
    #sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    #sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    
    #sr.setModel("edsr", 4)
    #upscale and save
    #result = sr.upsample(image)
    #cv2.imwrite("./output.png", result)
