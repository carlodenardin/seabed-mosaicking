"""
Autore: De Nardin Carlo

Il seguente programma esegue il processo di creazione di un mosaico tramite i seguenti step:
1.  Identificazione caratteristiche mediante un algoritmo a scelta:
    a.  AKAZE;
    b.  BRISK;
    c.  ORB;
    d.  SIFT.
2.  Matching tra immagini adiacenti delle caratteristiche identificate;
3.  Calcolo delle matrici omografiche tra immagini adiacenti;
4.  Stitching finale delle immagini.

N.B.
L'algoritmo realizzato non tiene conto della distorsione causata dalla lente della camera.
I mosaici creati tramite l'iterazione della cucitura delle immagini risulteranno sempre più distorti.
Future implementazioni potrebbero eliminare la distorsione delle immagini mediante parametri relativi
alla camera. A causa della distorsione per ottenere risultati utitli bisogna utilizzare circa 8 immagini
aventi un movimento lineare.

La funzione extract_frame è stata implementata per estrarre singoli frame da video.
"""

from Dependencies import *
from FeaturesDetection import *
from Ransac import *
from Stitcher import *

def extractFrame(video_path, save_path, frame_split):
    """
        Functions:
            Estrapola i frame di un video e li salva nella cartella input
        
        Args:
            video_path: percorso del video dal quale estrapolare i frame (string)
            save_path: percorso nel quale salvare i frame estrapolati (string)
            frame_split: intervallo di estrazione dei frame (int)
        
        Return:
            Non viene ritornato niente
    """

    video = cv2.VideoCapture(video_path) 
    current_frame = 0
    frame_number = 1

    while(True):

        #is_end = True -> il video non è finito
        #is_end = False -> il video è finito
        is_end, frame = video.read()

        if is_end:
            current_frame += 1
            frame_path = save_path + "input\\f" + str(frame_number) + ".jpg"

            if current_frame % frame_split == 0:
                cv2.imwrite(frame_path, frame)
                frame_number += 1

        else:
            break

class Mosaic:

    def __init__(self, main_path, images_name, images_number, algorithm, plane_size_x, plane_size_y):
        """
        Stato dell'oggetto mosaico
        main_path: percorso principale nel quale vengono gestiti gli input e gli output dei processi
        image_list: lista contenente i nomi delle immagini
        algorithm: algoritmo di features detection utilizzato
        """
        self.main_path = main_path
        self.images_name = images_name
        self.images_number = images_number
        self.algorithm = algorithm
        self.plane_size_x = plane_size_x
        self.plane_size_y = plane_size_y

    def run(self, images, images_name):
        """
            Functions:
                Funzione principale del programma. Per ogni coppia di immagini adiacente:
                1. Trova le features delle immagini tramite l'algoritmo SIFT ed esegue un matching delle features;
                2. Rimuove gli outliers per rendere più corretta la successiva sovrapposizione;
                3. Esegue la sovrapposizione delle immagini.
        """

        H_all = []

        for i in range(self.images_number - 2):
            print("Identificazione Features e match tra l'immagine " + str(self.images_name[i]) + " e l'immagine " + str(self.images_name[i + 1]))
    
            #   Features Detecion & Matching tra immagini (i, i + 1)
            featuresDetection = FeaturesDetection(self.main_path, self.images_name[i], self.images_name[i + 1], self.algorithm)
            correspondence = featuresDetection.run(images[i], images[i + 1])

            #   Salvataggio immagini numero match
            """save_path_match = self.main_path + "match\\" + img1_name.split('.')[0] + "_" + img2_name
            drawLines(correspondence, img1_open, img2_open, save_path_match, 0)"""

            #   Calcolo matrice omografica mediante RANSAC tra immagini (i, i + 1)
            ransac = Ransac()
            H, inliers, outliers = ransac.run(correspondence)

            H_all.append(H)

            #   Salvataggio immagini numero di inliers ed outliers
            """save_path_inliers = self.main_path + "inliers\\" + img1_name.split('.')[0] + "_" + img2_name
            save_path_outliers = self.main_path + "outliers\\" + img1_name.split('.')[0] + "_" + img2_name
            drawLines(inliers, img1_open, img2_open, save_path_inliers, 1)
            drawLines(outliers, img1_open, img2_open, save_path_outliers, 2)"""

        #   Processo di cambio prospettiva e cucitura delle immagini
        stitcher = Stitcher(self.main_path, self.plane_size_x, self.plane_size_y)
        stitcher.run(images, H_all)

        #----FINE IMAGE STITCHING (CUCITURA)----#


if __name__ == '__main__':

    if len(sys.argv) == 3:

        print('Processo di image mosaicking iniziato.')

        #   Percorsi
        current_path = os.getcwd()
        images_path = '\\Images'
        test_folder = '\\' + sys.argv[1]
        main_path = current_path + images_path + test_folder

        #   Nomi immagini
        image_list = []

        #   Impostazioni
        features_detection_algorithm = sys.argv[2]   #DA PROMPT
        plane_size_x = 2000
        plane_size_y = 4000

        #   Caricamento immagini
        images, images_name, images_number = loadImages(main_path)

        #   Esecuzione processo di mosaicking
        mosaic = Mosaic(main_path, images_name, images_number, features_detection_algorithm, plane_size_x, plane_size_y)
        mosaic.run(images, images_name)
    else:
        print("Non sono stati inseriti tutti gli argomenti.")
    