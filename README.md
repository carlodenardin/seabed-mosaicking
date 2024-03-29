# Programma

Questo programma prevede la creazione di un mosaico di immagini di fondali marini. Il seguente programma non tiene conto di problematiche relative alla distorsione delle immagini causata dalla lente della camera e alla posizione del AUV. Tramite la raccolta di questi parametri è possibile migliorare l'implementazione andando ad evitare fenomeni quali la distorsione prospettica crescente a causa del calcolo ricorsivo delle matrici omografiche.

## Librerie
* OpenCV (testato 4.5.1)
* NumPy (testato 1.19.4)
* glob
* PIL.Image
* os
* sys

## Struttura

### File

* [Mosaic.py](https://github.com/denardincarlo/seabed-mosaicking/blob/main/Mosaic.py): file principale contenente la gestione dell'intero processo;
* [FeaturesDetection.py](https://github.com/denardincarlo/seabed-mosaicking/blob/main/FeaturesDetection.py): file per l'identificazione di caratteristiche e corrispondenze tra due immagini;
* [Ransac.py](https://github.com/denardincarlo/seabed-mosaicking/blob/main/Ransac.py): file per la ricerca delle omografie tra immagini adiacenti (H1 H2, H2 H3, H3 H4, ...) e dei relativi inliers ed outliers tra immagini adiacenti;
* [Stitcher.py](https://github.com/denardincarlo/seabed-mosaicking/blob/main/Stitcher.py): file per il processo di calcolo delle omografie ricorsive e gestione della cucitura;
* [Dependencies.py](https://github.com/denardincarlo/seabed-mosaicking/blob/main/Dependencies.py): file contenente funzioni di supporto e librerie utilizzate.

## Processo

Il programma prevede la creazione di un mosaico di immagini a partire da successioni di immagini aventi sezioni sovrapposte. I passaggi eseguiti sono i seguenti:
1. Identificazione caratteristiche delle immagini tramite la possibile scelta di 4 diversi algoritmi di features detection (AKAZE, BRISK, ORB, SIFT);
2. Match delle caratteristiche identificate tra immagini adiacenti mediante un approccio Brute-Force basato sulla distanza minima;
3. Calcolo della matrice omografica tra immagini adiacenti su un sottoinsieme di match identificato tramite RANSAC [H12, H23, H34..];
4. Calcolo omografie ricorsive  [H12, H13, H14..] = [H12, H12 * H23, H13 * H34..]
5. Cambiamento di prospettiva delle immagini;
6. Cucitura delle immagini.


## Test

Il programma è stato reso testabile tramite:

```
python Mosaic.py cartella_test algoritmo_utilizzato
```
- cartella_test: nome della cartella test;
- algoritmo_utilizzato: scelta tra (AKAZE, BRISK, ORB, SIFT);

Esempio:

```
python Mosaic.py test1 ORB
```
Sono stati forniti una serie di test composti da, circa, 8 immagini catturate mediante una avanzamento progressivo frontale della camera per evitare fenomeni riguardanti eccessiva distorsione.

N.B. Se si intende clonare la seguente repository per eseguire i test ricordarsi di aggiungere le due cartelle 'processing' e 'output' all'interno delle cartella 'Images\test*'.

- [Images](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images): Cartella principale delle immagini
  -  [test1](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test1): dataset1 (Numero frame 42 - 49)
  -  [test2](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test2): dataset1 (481 - 488)
  -  [test3](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test3): dataset2 (117 - 124)
  -  [test4](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test4): dataset2 (937 - 945)
  -  [test5](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test5): dataset3 (301 - 308)
  -  [test6](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test6): dataset3 (992 - 999)
  -  [test7](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test7): dataset4 (75 - 82)
  -  [test8](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test8): dataset4 (644 - 651)
  -  [test9](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test9): dataset5 (106 - 113)
  -  [test10](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Images/test10): dataset5 (520 - 527) 

Note: Akaze non ha trovato features sufficenti ad eseguire il processo di mosaicking nel test10

I risultati del processo dei test, mediante i diversi algoritmi, si possono trovare nella cartella [Images](https://github.com/denardincarlo/seabed-mosaicking/tree/main/Risultati%20test)

Per effettuare nuovi testi seguire i seguenti passaggi:
1. Creare cartella test* all'interno di 'Images';
2. Nella cartella test creare 3 sottocartelle (input, processing, output);
3. Nella cartella input inserire in ordine di spostamento frontale della camera (dal basso verso l'alto per evitare distorsioni maggiori) circa 8 frame successivi;
4. Eseguito lo script nella cartella processing si potranno vedere i cambiamenti di prospettiva delle immagini e nella cartella output il mosaico risultante.

## Esempi risultati Test
<p>
  <img src="https://github.com/denardincarlo/seabed-mosaicking/blob/main/Risultati%20test/test3/ORB.png" width="250" height="500" alt="dataset2 test3 ORB"/>
  <em>Dataset2 test3 ORB</em>
</p>
<p>
  <img src="https://github.com/denardincarlo/seabed-mosaicking/blob/main/Risultati%20test/test9/SIFT.png" width="250" height="500" alt="dataset5 test9 SIFT"/>
  <em>Dataset5 test9 SIFT</em>
</p>
<p>
  <img src="https://github.com/denardincarlo/seabed-mosaicking/blob/main/Risultati%20test/test4/AKAZE.png" width="250" height="500" alt="dataset2 test4 AKAZE"/>
  <em>Dataset2 test4 AKAZE</em>
</p>
<p>
  <img src="https://github.com/denardincarlo/seabed-mosaicking/blob/main/Risultati%20test/test1/BRISK.png" width="250" height="500" alt="dataset1 test1 BRISK"/>
  <em>Dataset1 test1 BRISK</em>
</p>

## Considerazioni finali e possibili migliorie

Il programma implementa tutti i passaggi per la creazione di un mosaico di immagini di fondali marini. Soffre del progressivo aumento di distorsione dovuta alla cucitura di immagini catturate con una determinata lente non lineare. Di seguito sono riportate delle possibili migliorie:
1. Ottenimento parametri riguardanti la camera per eliminare la distorsione;
2. Utilizzo di frames successivi con un maggiore sezione sovrapposta superiore al 70 %;
3. Utilizzo di parametri relativi al dispositivo subaqueo (velocità, profondità, ..) per calcolare la posizione globale del dispositivo e realizzare un piano di stitch dinamico.


