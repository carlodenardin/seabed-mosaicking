from Dependencies import *

class Stitcher:
    
    def __init__(self, main_path, plane_size_x, plane_size_y):
        """
            main_path: percorso principale
            plane_size_x: grandezza piano di stitching (asse x)
            plane_size_y: grandezza piano di stitching (asse y)
        """
        self.main_path = main_path
        self.plane_size_x = plane_size_x
        self.plane_size_y = plane_size_y

    def homographyRecursive(self, H_all):
        """
            Functions:
                Funzione per calcolare il valore delle matrici omografiche in successione.
            
            Args:
                H_array: lista contenente le matrici omografiche tra immagini [H12, H23, ..., H(N)(N+1)]

            Return:
                H_recursive: lista contenente le matrici omografiche calcolate ricorsivamente dalla fine.
        """
        H_recursive = []
        j = len(H_all) - 1
        for i in range(len(H_all)):
            if i == 0:
                H_recursive.append(H_all[j])
                j = j - 1
            else:
                H_recursive.append(np.dot(H_recursive[i - 1], H_all[j]))
                j = j - 1
        return H_recursive

    def warpImages(self, images, H_recursive):
        """
            Functions:
                Funzione che modifica la prospettiva delle immagini in base al corrispondente valore
                della matrice omografica ricorsiva. Salva inoltre le immagini nella cartella processing
                per eseguire lo stitch finale.
            
            Args:
                images: lista di immagini
                H_recursive: lista delle matrici omografiche ricorsive

            Return:
                images_warped: lista contenente le immagini modificate
        """

        print('Inizio processo di cambio prospettiva delle immagini..')
        first_move = np.float32([[1, 0, 0], [0, 1, 0]])
        first_image = cv2.warpAffine(images[len(H_recursive)], first_move, (self.plane_size_x, self.plane_size_y))
        cv2.imwrite(self.main_path + '\\processing\\' + str(len(H_recursive)) + '.tif', first_image)

        j = len(H_recursive) - 1
        images_warped = []
        for i in range(len(H_recursive)):
            images_warped.append(cv2.warpPerspective(images[i], H_recursive[j], (self.plane_size_x, self.plane_size_y)))
            cv2.imwrite(self.main_path + '\\processing\\' + str(i) + '.tif', images_warped[i])
            j = j - 1

        return images_warped
    
    def stitchImages(self, images_warped):
        """
            Functions:
                Funzione di cucitura delle immagini. Vengono cucite insieme le immagini
                prcedentemente modificate in base alla matrice omografica ricorsiva.
            
            Args:
                images_warped: lista di immagini con prospettiva modificata

            Return:
                NULL: viene salvata la mappa finale nella cartella output.
        """

        print('Inizio processo di cucitura delle immagini..')
        final_map = Image.new('RGB', (self.plane_size_x, self.plane_size_y))

        for i in range(len(images_warped) + 1):
            img_open = Image.open(self.main_path + '\\processing\\' + str(i) + '.tif')
            
            image = img_open.convert('RGBA')
            datas = image.getdata()
            
            newData = []
            for item in datas:
                if item[:3] == (0, 0, 0):
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            
            image.putdata(newData)

            final_map.paste(image, (0,0), image)
        
        final_map.save(self.main_path + '\\output\\mappa.png', 'PNG')
        
    def run(self, images, H_all):
        """
            Functions:
                Funzione di gestione del processo di stitching:
                1.  Calcolo matrici omografiche ricorsive;
                2.  Eseguo la trasformazione prospettica;
                3.  Eseguo la cucitura delle immagini
            
            Args:
                images: lista di immagini
                H_all: lista di matrici omografiche [H12, H23, H34, ..]

            Return:
                NULL: FINE PROCESSO DI IMAGE MOSAICKING
        """
        
        H_recursive = self.homographyRecursive(H_all)
        images_warped = self.warpImages(images, H_recursive)
        self.stitchImages(images_warped)
        print('Processo di image mosaicking terminato.')

    




    

    