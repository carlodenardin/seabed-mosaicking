from Dependencies import *

class FeaturesDetectionInfo():

    def __init__(self, key_points_list, key_points, descriptors):
        """
            key_points_list: lista punti chiave corrispondenti alle features (KeyPoints), per eseguire il match
            key_points: lista punti chiave in formato [x1, y1]
            descriptors: matrice descrittrice del singolo punto chiave. Invarianza di scala e orientamento
        """
        self.key_points_list = key_points_list
        self.key_points = key_points
        self.descriptors = descriptors

class FeaturesDetection:

    def __init__(self, main_path, image1_name, image2_name, algorithm):
        """
            main_path: percorso principale nel quale vengono gestiti gli input e gli output dei processi
            img1_name: nome immagine1
            img2_name: nome immagine2
            img1_open: immagine1 letta
            img2_open: immagine2 letta
            features: numero di features da ricercare
        """
        self.main_path = main_path
        self.image1_name = image1_name
        self.image2_name = image2_name
        self.algorithm = algorithm

    def get_features(self, image, image_name):
        """
            Functions:
                Identifica le caratteristiche (punti chiave) dell'immagine passata come parametri
            
            Args:
                img_open: immagine letta della quale ricavare le features / caratteristiche
                img_name: nome immagine

            Return:
                key_points_list: lista punti chiave corrispondenti alle features (KeyPoints), per eseguire il match
                key_points: lista punti chiave in formato [x1, y1]
                descriptors: matrice descrittrice del singolo punto chiave. Invarianza di scala e orientamento
        """

        #   Trasformazione immagine nella scala di grigi per ottenere caratteristiche più accurate
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

        #   Esecuzione dell'algoritmo di features detection
        if self.algorithm == "AKAZE":
            akaze = cv2.AKAZE_create() 
            key_points_list, descriptors = akaze.detectAndCompute(img_gray, None)
        elif self.algorithm == "BRISK":
            brisk = cv2.BRISK_create() 
            key_points_list, descriptors = brisk.detectAndCompute(img_gray, None)
        elif self.algorithm == "ORB":
            orb = cv2.ORB_create(nfeatures=4000) 
            key_points_list, descriptors = orb.detectAndCompute(img_gray, None)
        elif self.algorithm == "SIFT":
            sift = cv2.SIFT_create(nfeatures=4000)
            key_points_list, descriptors = sift.detectAndCompute(img_gray, None)
        else:
            print("Non è stato selezionato un algoritmo corretto")

        #Salvataggio punti chiave in formato [[x1, y1], ..., [xfeatures, yfeatures]]
        key_points = [x.pt for x in key_points_list]

        #Salvataggio immagini SIFT
        """save_path_feature = self.main_path + "featuresDetection\\" + image_name
        drawPoints(key_points, img_open, save_path_feature, 0)"""

        return FeaturesDetectionInfo(key_points_list, key_points, descriptors)

    def match(self, obj1, obj2):
        """
            Functions:
                Confronta i descrittori dei punti chiave delle due immagini, passate come oggetto, e mantiene i punti chiave più precisi
            
            Args:
                obj1: oggetto SiftInfo contenente le informazioni (key_points_list, key_points, descriptors) riferite all'immagine1
                obj2: oggetto SiftInfo contenente le informazioni (key_points_list, key_points, descriptors) riferite all'immagine2

            Return:
                correspondence: [x1, y1, x2, y2]
        """

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(obj1.descriptors, obj2.descriptors, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append([m])
        
        matched_points = []
        for match in good:
            p1 = obj1.key_points_list[match[0].queryIdx].pt
            p2 = obj2.key_points_list[match[0].trainIdx].pt 
            px1 = p1[0]
            py1 = p1[1]
            px2 = p2[0]
            py2 = p2[1]
            
            matched_points.append([px1, py1, px2, py2])   
            
        return matched_points
        

    def run(self, image1, image2):
        """
            Functions:
                Funzione per la ricerca e il matching delle features.

            Return:
                matched_points: punti chiave corrispondenti di due immagini [x1, y1, x2, y2]
        """
        #Feature (caratteristiche) dell'immagine 1 e 2
        obj1 = self.get_features(image1, self.image1_name)
        obj2 = self.get_features(image2, self.image2_name)

        #Punti chiavi corrispondenti [x1, y1, x2, y2]
        matched_points = self.match(obj1, obj2)

        return matched_points


        
