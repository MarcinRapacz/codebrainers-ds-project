# Task 1 Report

## Kształt danych
Liczba wierszy i kolumn: (10000, 20)

## Pierwsze 10 wierszy
```
  Body Type    Sex        Diet How Often Shower Heating Energy Source    Transport Vehicle Type Social Activity  Monthly Grocery Bill Frequency of Traveling by Air  Vehicle Monthly Distance Km Waste Bag Size  Waste Bag Weekly Count  How Long TV PC Daily Hour  How Many New Clothes Monthly  How Long Internet Daily Hour Energy efficiency                              Recycling                       Cooking_With  CarbonEmission
 overweight female pescatarian            daily                  coal       public          NaN           often                   230                    frequently                          210          large                       4                          7                            26                             1                No                              ['Metal']                  ['Stove', 'Oven']            2238
      obese female  vegetarian  less frequently           natural gas walk/bicycle          NaN           often                   114                        rarely                            9    extra large                       3                          9                            38                             5                No                              ['Metal']             ['Stove', 'Microwave']            1892
 overweight   male    omnivore  more frequently                  wood      private       petrol           never                   138                         never                         2472          small                       1                         14                            47                             6         Sometimes                              ['Metal']              ['Oven', 'Microwave']            2595
 overweight   male    omnivore      twice a day                  wood walk/bicycle          NaN       sometimes                   157                        rarely                           74         medium                       3                         20                             5                             7         Sometimes ['Paper', 'Plastic', 'Glass', 'Metal'] ['Microwave', 'Grill', 'Airfryer']            1074
      obese female  vegetarian            daily                  coal      private       diesel           often                   266               very frequently                         8457          large                       1                          3                             5                             6               Yes                              ['Paper']                           ['Oven']            4743
 overweight   male  vegetarian  less frequently                  wood       public          NaN       sometimes                   144                    frequently                          658          large                       1                         22                            18                             9         Sometimes            ['Paper', 'Glass', 'Metal']     ['Stove', 'Oven', 'Microwave']            1647
underweight female       vegan  less frequently                  wood      private       hybrid           never                    56                        rarely                         5363         medium                       4                          9                            11                            19         Sometimes                                     []              ['Grill', 'Airfryer']            1832
underweight female       vegan  more frequently                  coal walk/bicycle          NaN       sometimes                    59               very frequently                           54    extra large                       3                          5                            39                            15                No          ['Paper', 'Plastic', 'Glass']             ['Stove', 'Microwave']            2322
 overweight   male    omnivore            daily                  wood       public          NaN           never                   200                    frequently                         1376         medium                       3                          3                            31                            15               Yes                              ['Glass'] ['Microwave', 'Grill', 'Airfryer']            2494
underweight female pescatarian            daily                  wood       public          NaN           often                   135                        rarely                          440    extra large                       1                          8                            23                            18         Sometimes                              ['Glass'] ['Microwave', 'Grill', 'Airfryer']            1178
```

## Informacje o kolumnach
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 20 columns):
 #   Column                         Non-Null Count  Dtype 
---  ------                         --------------  ----- 
 0   Body Type                      10000 non-null  object
 1   Sex                            10000 non-null  object
 2   Diet                           10000 non-null  object
 3   How Often Shower               10000 non-null  object
 4   Heating Energy Source          10000 non-null  object
 5   Transport                      10000 non-null  object
 6   Vehicle Type                   3279 non-null   object
 7   Social Activity                10000 non-null  object
 8   Monthly Grocery Bill           10000 non-null  int64 
 9   Frequency of Traveling by Air  10000 non-null  object
 10  Vehicle Monthly Distance Km    10000 non-null  int64 
 11  Waste Bag Size                 10000 non-null  object
 12  Waste Bag Weekly Count         10000 non-null  int64 
 13  How Long TV PC Daily Hour      10000 non-null  int64 
 14  How Many New Clothes Monthly   10000 non-null  int64 
 15  How Long Internet Daily Hour   10000 non-null  int64 
 16  Energy efficiency              10000 non-null  object
 17  Recycling                      10000 non-null  object
 18  Cooking_With                   10000 non-null  object
 19  CarbonEmission                 10000 non-null  int64 
dtypes: int64(7), object(13)
memory usage: 1.5+ MB

```

## Statystyki opisowe (kolumny numeryczne)
```
       Monthly Grocery Bill  Vehicle Monthly Distance Km  Waste Bag Weekly Count  How Long TV PC Daily Hour  How Many New Clothes Monthly  How Long Internet Daily Hour  CarbonEmission
count          10000.000000                 10000.000000            10000.000000               10000.000000                  10000.000000                  10000.000000    10000.000000
mean             173.875200                  2031.485900                4.024600                  12.139200                     25.109000                     11.889100     2269.147300
std               72.234018                  2769.715597                1.990375                   7.106369                     14.698725                      7.277218     1017.675247
min               50.000000                     0.000000                1.000000                   0.000000                      0.000000                      0.000000      306.000000
25%              111.000000                    69.000000                2.000000                   6.000000                     13.000000                      6.000000     1538.000000
50%              173.000000                   823.000000                4.000000                  12.000000                     25.000000                     12.000000     2080.000000
75%              237.000000                  2516.750000                6.000000                  18.000000                     38.000000                     18.000000     2768.000000
max              299.000000                  9999.000000                7.000000                  24.000000                     50.000000                     24.000000     8377.000000
```

