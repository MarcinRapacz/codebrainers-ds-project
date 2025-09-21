# Task 8 Report

```
X:         Body Type     Sex         Diet  ... Energy efficiency                               Recycling                                 Cooking_With
0      overweight  female  pescatarian  ...                No                               ['Metal']                            ['Stove', 'Oven']
1           obese  female   vegetarian  ...                No                               ['Metal']                       ['Stove', 'Microwave']
2      overweight    male     omnivore  ...         Sometimes                               ['Metal']                        ['Oven', 'Microwave']
3      overweight    male     omnivore  ...         Sometimes  ['Paper', 'Plastic', 'Glass', 'Metal']           ['Microwave', 'Grill', 'Airfryer']
4           obese  female   vegetarian  ...               Yes                               ['Paper']                                     ['Oven']
...           ...     ...          ...  ...               ...                                     ...                                          ...
9995        obese    male     omnivore  ...               Yes                                      []                                ['Microwave']
9996       normal  female        vegan  ...         Sometimes                    ['Paper', 'Plastic']                       ['Stove', 'Microwave']
9997   overweight  female   vegetarian  ...               Yes           ['Paper', 'Plastic', 'Metal']           ['Microwave', 'Grill', 'Airfryer']
9998  underweight    male        vegan  ...         Sometimes                      ['Paper', 'Metal']  ['Stove', 'Microwave', 'Grill', 'Airfryer']
9999        obese    male  pescatarian  ...         Sometimes           ['Plastic', 'Glass', 'Metal']                ['Oven', 'Grill', 'Airfryer']

[10000 rows x 19 columns]
y_reg: 0       2238
1       1892
2       2595
3       1074
4       4743
        ... 
9995    2408
9996    3084
9997    2377
9998    4574
9999     826
Name: CarbonEmission, Length: 10000, dtype: int64
y_clf: 0       0
1       0
2       0
3       0
4       1
       ..
9995    0
9996    1
9997    0
9998    1
9999    0
Name: CarbonEmission, Length: 10000, dtype: int64
thr: 2966.0
```

