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

Il programma prevede la creazione di un mosaico di immagini a partire da successioni di immagini aventi sezioni sovrapposte. Nello specifico:


### Test

Il programma è stato strutturato per avere una visione completa di tutti i passaggi.

* [Images](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini): Cartella principale delle immagini
  * [input](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini/input): contiene le immagini (frame) estratti dal video

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




