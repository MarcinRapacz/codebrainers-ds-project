---Task 1 executed---
Shape: (10000, 20)
     Body Type     Sex         Diet How Often Shower Heating Energy Source  ... How Long Internet Daily Hour Energy efficiency                               Recycling                        Cooking_With CarbonEmission
0   overweight  female  pescatarian            daily                  coal  ...                            1                No                               ['Metal']                   ['Stove', 'Oven']           2238
1        obese  female   vegetarian  less frequently           natural gas  ...                            5                No                               ['Metal']              ['Stove', 'Microwave']           1892
2   overweight    male     omnivore  more frequently                  wood  ...                            6         Sometimes                               ['Metal']               ['Oven', 'Microwave']           2595
3   overweight    male     omnivore      twice a day                  wood  ...                            7         Sometimes  ['Paper', 'Plastic', 'Glass', 'Metal']  ['Microwave', 'Grill', 'Airfryer']           1074
4        obese  female   vegetarian            daily                  coal  ...                            6               Yes                               ['Paper']                            ['Oven']           4743
5   overweight    male   vegetarian  less frequently                  wood  ...                            9         Sometimes             ['Paper', 'Glass', 'Metal']      ['Stove', 'Oven', 'Microwave']           1647
6  underweight  female        vegan  less frequently                  wood  ...                           19         Sometimes                                      []               ['Grill', 'Airfryer']           1832
7  underweight  female        vegan  more frequently                  coal  ...                           15                No           ['Paper', 'Plastic', 'Glass']              ['Stove', 'Microwave']           2322
8   overweight    male     omnivore            daily                  wood  ...                           15               Yes                               ['Glass']  ['Microwave', 'Grill', 'Airfryer']           2494
9  underweight  female  pescatarian            daily                  wood  ...                           18         Sometimes                               ['Glass']  ['Microwave', 'Grill', 'Airfryer']           1178

[10 rows x 20 columns]
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
---Task 1 completed---
