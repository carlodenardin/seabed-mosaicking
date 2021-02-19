from Dependencies import *

class Ransac:
    
    def find_inliers_outliers(self, mask, points1, points2):
        """
            Functions:
                Funzione utilizzata per trovare inliers ed outliers tramite l'utilizzo della maschera ottenuta
                dalla funzione find_homography.
            
            Args:
                mask: lista booleana: 1 -> inliers, 0 -> outliers
                pts_src: punti corrispondenti prima immagine
                pts_dst: punti corrispondenti seconda immagine

            Return:
                matched_inliers: punti matched precisi
                matched_outliers: punti matched non precisi scartati
        """

        matched_inliers = []
        matched_outliers = []

        for i in range(len(points1)):
            if mask[i] == 1:
                matched_inliers.append([points1[i][0], points1[i][1], points2[i][0], points2[i][1]])
            else:
                matched_outliers.append([points1[i][0], points1[i][1], points2[i][0], points2[i][1]])

        return matched_inliers, matched_outliers

    def run(self, matched_points):
        """
            Functions:
                Funzione per la ricerca delle omografie tra immagini adiacenti. Inoltre trova outliers ed inliers per avere
                una precisione più accurata

            Return:
                H: omografia immagini adiacenti. (H1 H2, H2 H3, H3 H4...)
                inliers: punti più precisi
                outliers: punti imprecisi o vicini al bordo
        """

        #Estrazione punti da matched_points [x1, y1, x2, y2]
        matched_points_img1 = []
        matched_points_img2 = []
        for x1, y1, x2, y2 in matched_points:
            matched_points_img1.append([x1, y1])
            matched_points_img2.append([x2, y2])

        if isinstance(matched_points_img1, list):
            pts_src = np.array(matched_points_img1)

        if isinstance(matched_points_img2, list):
            pts_dst = np.array(matched_points_img2)

        
        #   Calcolo matrice omografia tra le due immagini. Viene ritorana la maschera per l'ottenimento di inliers ed outliers
        H, mask = cv2.findHomography(pts_src, pts_dst, cv2.RANSAC)

        #   Identificazione inliers ed outliers mediante la maschera
        inliers, outliers = self.find_inliers_outliers(mask, pts_src, pts_dst)

        return H, inliers, outliers
        