# Programma

Questo programma prevede la creazione di un mosaico di immagini di fondali marini.

## Librerie
* OpenCV
* NumPy
* glob
* PIL.Image
* os
* sys

## Struttura

### File

* [Mosaic.py](https://github.com/denardincarlo/seabed-mosaicking/Mosaic.py): file principale contenente la gestione dell'intero processo;
* [FeaturesDetection.py](https://github.com/denardincarlo/Mosaicking/tree/master/sift.py): file per l'identificazione di caratteristiche e corrispondenze tra due immagini;
* [Ransac.py](https://github.com/denardincarlo/seabed-mosaicking/Ransac.py): file per la ricerca delle omografie tra immagini adiacenti (H1 H2, H2 H3, H3 H4, ...) e dei relativi tra inliers ed outliers tra immagini adiacenti;
* [Stitcher.py](https://github.com/denardincarlo/seabed-mosaicking/Stitcher.py): file per il processo di calcolo delle omografie ricorsive e gestione della cucitura;
* [dependencies.py](https://github.com/denardincarlo/seabed-mosaicking/Dependencies.py): file contenente funzioni di supporto e librerie utilizzate.

## Processo

Il programma prevede la creazione di un mosaico di immagini a partire da successioni di immagini aventi sezioni sovrapposte. I passaggi eseguiti sono i seguenti:
1. Identificazione caratteristiche delle immagini tramite la possibile scelta di 4 diversi algoritmi di features detection (AKAZE, BRISK, ORB, SIFT);
2. Match delle caratteristiche identificate tra immagini adiacenti mediante un approccio Brute-Force basato sulla distanza minima;
3. Calcolo della matrice omografica tra immagini adiacenti su un sottoinsieme di match identificato tramite RANSAC [H12, H23, H34..];
4. Calcolo omografie ricorsive  [H12, H13, H14..] = [H12, H12 * H23, H13 * H34..]
5. Cambiamento di prospettiva delle immagini;
6. Cucitura delle immagini.


### Test

Il programma è stato reso testabile tramite:

Sono stati forniti una serie di test composti da, circa, 8 immagini catturate mediante una avanzamento progressivo frontale della camera per evitare fenomeni riguardanti eccessiva distorsione.

```
python Mosaic.py cartella_test algoritmo_utilizzato
ES: python Mosaic.py test3 ORB
```

* [Images](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini): Cartella principale delle immagini
*  test1: dataset1 (Numero frame 42 - 49)
*  test2: dataset1 (481 - 488)
*  test3: dataset2 (117 - 124)
*  test4: dataset2 (937 - 945)
*  test5: dataset3 (301 - 308)
*  test6: dataset3 (992 - 999)
*  test7: dataset4 (75 - 82)
*  test8: dataset4 (644 - 651)
*  test9: dataset5 (106 - 113)
*  test10: dataset5 (520 - 527) 

Note: Akaze non ha trovato features sufficenti ad eseguire il processo di mosaicking nel test10

I risultati si possono trovare nella cartella [Images](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Risultati%20test)


### Esempio 1
1. Video

![video](/esempio/video1.gif)

2. Risultato

![risultato](/esempio/risultato1.jpg)


### Esempio 2
1. Video

![video](/esempio/video2.gif)

2. Risultato

![risultato](/esempio/risultato2.jpg)

### Esempio

Consideriamo di avere una lista di immagini.

1. Estrapolazione frame da video;

![video](/esempio/video.gif)

2. Ottenimento punti chiave immagine[i] e immagine[i + 1];

![immagine[i]](/Immagini/sift/f1.jpg)
![immagine[i + 1]](/Immagini/sift/f1.jpg)

3. Matching descrittori dei punti chiave delle due immagini;

![match](/Immagini/match/f1_f2.jpg)

4. Calcolo matrice di omografia, inliers (linee verdi) ed outliers (linee rosse);

![inliers](/Immagini/inliers/f1_f2.jpg)
![outliers](/Immagini/outliers/f1_f2.jpg)

5. Cucitura immagine[i] e immagine[i + 1].

![stitch](/Immagini/output/result2.jpg)

6. Ripetere le istruzioni da (2) con input immagine[i + 1] e immagine[i + 2], così fino a completare il mosaico.

![output](/Immagini/output/result21.jpg)




