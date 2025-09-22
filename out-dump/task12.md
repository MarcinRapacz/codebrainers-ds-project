## Podsumuj wyniki projektu:

### **Klasyfikacja:** który model był lepszy (ROC-AUC, precyzja/recall)? Jaki wpływ miał wybór progu kwantyla?

```
=== task9 - KNN (best) ===
ROC-AUC: 0.9182
              precision    recall  f1-score   support

           0     0.9029    0.9700    0.9352      1600
           1     0.8292    0.5825    0.6843       400

    accuracy                         0.8925      2000
   macro avg     0.8660    0.7762    0.8098      2000
weighted avg     0.8881    0.8925    0.8850      2000


=== task9 - LogisticRegression (best) ===
ROC-AUC: 0.9904
              precision    recall  f1-score   support

           0     0.9722    0.9844    0.9783      1600
           1     0.9342    0.8875    0.9103       400

    accuracy                         0.9650      2000
   macro avg     0.9532    0.9359    0.9443      2000
weighted avg     0.9646    0.9650    0.9647      2000

```

#### Wnioski:

- Logistic Regression była zdecydowanie lepsza pod kątem wszystkich metryk (ROC-AUC, precyzja, recall, F1-score).
- Zwiększenie progu kwantyla, zwększył precyzje kosztem czułości. Model ostrożniej przypsiuje wartości do danej klasy (1). F1 może spadać lub wzrastać w zależności od tego jak bardzo spadnie recall do wzrostu precyzji.

### **Regresja:** który model ma niższy RMSE/MAE? Czy R² jest satysfakcjonujące?

```
=== task10 - KNNRegressor (best) ===
RMSE=521.438  MAE=382.022  R2=0.738


=== task10 - LinearRegression ===
RMSE=261.230  MAE=175.201  R2=0.934
```

#### Wnioski:

- LinearRegression bardzo dobrze dopasowuje sie do danych. Nizsze błędy RMSE i MAE oraz wyzszy R2
- r2 jest bardzo dobry, pokazeuje ze model wyjasnia ponad 93% wariancji w dancyh
- na dodatkowym wykresie widac liniowosc danych (scatterplot.png)

## **Klasteryzacja:** interpretacja klastrów — czy widzisz sensowne segmenty?

```
# Task 11 Report

Dla n_clusters = 2, średni silhouette_score wynosi: 0.0919  Inertia: 521755.9018

Dla n_clusters = 3, średni silhouette_score wynosi: 0.0383  Inertia: 506447.4688

Dla n_clusters = 4, średni silhouette_score wynosi: 0.0268  Inertia: 499556.8360

Dla n_clusters = 5, średni silhouette_score wynosi: 0.0328  Inertia: 490752.3092

Dla n_clusters = 6, średni silhouette_score wynosi: 0.0400  Inertia: 482203.9819

Dla n_clusters = 7, średni silhouette_score wynosi: 0.0494  Inertia: 471458.1190

Dla n_clusters = 8, średni silhouette_score wynosi: 0.0302  Inertia: 475349.3815

Dla n_clusters = 9, średni silhouette_score wynosi: 0.0317  Inertia: 471962.1776

Dla n_clusters = 10, średni silhouette_score wynosi: 0.0506  Inertia: 455502.7811
```

### Wnioski:

- silhouette_score bardzo niski dla wszystkich opcji, co wskazuje na to ze dane nie tworza wyraznych segmentow
- inertia spada, ale nie ma wyraznego załamania co sugerowałby tzw kolano
- ogolnie wyniki bardzo słaba i raczej ciezko mówić o wiarygodnosci modelu

---

**Ograniczenia:** potencjalne źródła biasu, rozkłady cech, brak walidacji czasowej, możliwe przecieki cech, balans klas.

**Kolejne kroki:** inżynieria cech, walidacja krzyżowa stratified, analiza metryk kosztowych, testy stabilności.
