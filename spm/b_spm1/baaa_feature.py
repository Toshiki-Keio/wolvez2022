import cv2
from FEATURE import Feature_img
import tempfile

class ReadFeaturedImg():
    """画像読込関数
    
    Args:
        importPath (str): Original img path
        saveDir (str): Save directory path that allowed tmp
        Save(bool):Save or not, defalt:False
    """
    def __init__(self, importPath:str=None, saveDir:str=None, Save:bool=False):
        self.imp_p = importPath
        if Save:
            self.sav_d = saveDir
        #else:
        #    self.sav_d = tempfile.TemporaryDirectory()
        self.save = Save
    
    def feature_img(self, frame_num, feature_names=None):
        '''Change to treated img
        Args:
            frame_num(int):Frame number or time
            feature_name(str):
        '''
        self.treat = Feature_img(self.imp_p, frame_num, self.sav_d)
        
        if feature_names == None:
            self.treat.normalRGB()
            self.treat.vari()
            self.treat.rgbvi()
            self.treat.grvi()
            self.treat.ior()
            self.treat.enphasis()
            self.treat.edge()
            self.treat.hsv()
            self.treat.r()
            self.treat.b()
            self.treat.g()
            self.treat.rb()
            self.treat.gb()
            self.treat.rg()
        else:
            for feature_name in feature_names:
                if feature_name == "normalRGB":
                    self.treat.normalRGB()
                elif feature_name == "vari":
                    self.treat.vari()
                elif feature_name == "rgbvi":
                    self.treat.rgbvi()
                elif feature_name == "grvi":
                    self.treat.grvi()
                elif feature_name == "ior":
                    self.treat.ior()
                elif feature_name == "enphasis":
                    self.treat.enphasis()
                elif feature_name == "edge":
                    self.treat.edge()
                elif feature_name == "hsv":
                    self.treat.hsv()
                elif feature_name == "r":
                    self.treat.r()
                elif feature_name == "b":
                    self.treat.b()
                elif feature_name == "g":
                    self.treat.g()
                elif feature_name == "rb":
                    self.treat.rb()
                elif feature_name == "rg":
                    self.treat.rg()
                elif feature_name == "gb":
                    self.treat.gb()
            
        
        fmg_list = self.treat.output()
        
        return fmg_list


    def read_img(self, path):
        #print("===== func read_img starts =====")
        self.img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        self.img = self.img[int(0.25*self.img.shape[0]):int(0.75*self.img.shape[0])]
        # 読み込めないエラーが生じた際のロバスト性も検討したい
        return self.img