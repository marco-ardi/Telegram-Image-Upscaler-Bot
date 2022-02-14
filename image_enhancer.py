import torch
import cv2
from cv2 import dnn_superres
# creating an sr object


class imageEnhancer:
    sr2 = dnn_superres.DnnSuperResImpl_create()
    sr3 = dnn_superres.DnnSuperResImpl_create()
    sr4 = dnn_superres.DnnSuperResImpl_create()

    def __init__(self):
        # Loading models
        self.sr2.readModel("./models/EDSR_x2.pb")
        self.sr3.readModel("./models/EDSR_x3.pb")
        self.sr4.readModel("./models/EDSR_x4.pb")

        # sets GPU instead of CPU if CUDA is available
        if torch.cuda.is_available():
            print("Setting GPU instead of CPU")
            self.sr2.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.sr2.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
            self.sr3.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.sr3.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
            self.sr4.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.sr4.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        # setting models
        self.sr2.setModel("edsr", 2)
        self.sr3.setModel("edsr", 3)
        self.sr4.setModel("edsr", 4)

    def Enhance(self, sr_type: str, path: str):
        '''
        Upscale the input image
        '''
        img = cv2.imread(path)
        if sr_type == "x2":
            result = self.sr2.upsample(img)
        elif sr_type == "x3":
            result = self.sr3.upsample(img)
        elif sr_type == "x4":
            result = self.sr4.upsample(img)
        cv2.imwrite(path[:len(path)-4] + "out.png", result)
