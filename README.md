# Mosaicking

Questo progetto prevede la creazione di un mosaico di immagini a partire da un video come sistema di mappatura.

## Librerie
* OpenCV
* NumPy
* Pyplot

## Struttura

### File

* [main.py](https://github.com/denardincarlo/Mosaicking/tree/master/main.py): file principale. Contiene le istruzioni per l'estrapolazione dei frame e generazione del mosaico;
* [sift.py](https://github.com/denardincarlo/Mosaicking/tree/master/sift.py): file contenente ricerca e matching delle features;
* [ransac.py](https://github.com/denardincarlo/Mosaicking/tree/master/ransac.py): file contenente la ricerca delle omografie tra immagini adiacenti (H1 H2, H2 H3, H3 H4, ...) e degli inliers ed outliers;
* [dependencies.py](https://github.com/denardincarlo/Mosaicking/tree/master/dependencies.py): file contenente le dependencies utilizzate e le funzioni per disegnare punti e linee.

### Cartelle

Il programma è stato strutturato per avere una visione completa di tutti i passaggi.

* [Immagini](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini): Cartella principale delle immagini
  * [input](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini/input): contiene le immagini (frame) estratti dal video [video.mp4](https://github.com/denardincarlo/Mosaicking/tree/master/Video/video.mp4)
  * [sift](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini/sift): contiene le immagini con feature evidenziate tramite l'algoritmo sift
  * [match](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini/match): contiene le immagini adiacenti unite tra di loro con feature evidenziate
  * [inliers](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini/inliers): contiene le immagini adiacenti unite tra di loro con feature evidenziate più accurate
  * [outliers](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini/outliers): contiene le immagini adiacenti unite tra di loro con feature evidenziate meno accurate
  * [output](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini/output): contiene il risultato finale (stitch) step-by-step
* [Video](https://github.com/denardincarlo/Mosaicking/tree/master/Video): Cartella principale dei video
  * [video.mp4](https://github.com/denardincarlo/Mosaicking/tree/master/Video/video.mp4): esempio video

## Processo

Il programma prevede la creazione di una mappa da video. L'idea prevede l'ottenimento di dei frame del video, quindi immagini ordinate. Successivamente tramite l'utilizzo di algoritmi come: SIFT e RANSAC si possono cucire (stitch) le immagini tra di loro mediante la matrice di omografia delle immagini adiacenti. Avendo immagini ordinate è stata calcolata la matrice di omografia solamente per le immagini adiacenti quindi H1_H2, H2_H3, H3_H4, etc. 

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




