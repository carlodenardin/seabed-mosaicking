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

```
python Mosaic.py cartella_test algoritmo_utilizzato
ES: python Mosaic.py test3 ORB
```

Sono stati forniti una serie di test composti da, circa, 8 immagini catturate mediante una avanzamento progressivo frontale della camera per evitare fenomeni riguardanti eccessiva distorsione.

- [Images](https://github.com/denardincarlo/Mosaicking/tree/master/Immagini): Cartella principale delle immagini
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
4. Eseguto lo script nella cartella processing si potranno vedere i cambiamenti di prospettiva delle immagini e nella cartella output i risultati.

## Risultati Test

Vengono di seguito riportati dei risultati dei Test effettuati:
![alt text](https://github.com/denardincarlo/seabed-mosaicking/blob/main/Risultati%20test/test3/ORB.png)

## Considerazioni finali

Il programma implementa tutti i passaggi per la creazione di un mosaico di immagini di fondali marini. Soffre del progressivo aumento di distorsione dovuta dalla cucitura di immagini aventi distorsione.

## Possibili migliorie

Conoscendo diversi parametri relativi al dispositivo di acquisizione delle immagini e al dispositivo subacqueo (velocità, correnti..) è possibile apportare migliorie al mosaico finale e creare una struttura dinamica di stiching in base al calcolo della posizione del AUV.

