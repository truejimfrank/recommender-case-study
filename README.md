
# Improving Movie Recommender For **Movies-Legit**

[GroupLens Move Dataset](https://grouplens.org/datasets/movielens/)

## explore new solutions! is todays motto

There are three aims we followed for todays EXCITING results

1. Make a new recommender
2. Compare to the baseline recommender
3. Show why it is better

## EDA Movie Ratings

Ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).

![Work Flow](img/counts_hist.png)

![Work Flow](img/distribution_of_user_ratings.png)


## Baseline Recommender vs. Surprise SVD Recommender

Model error & percentage improvement table

![Work Flow](img/error_table.png)

Distribution of rating predictions

![Work Flow](img/violin_means.png)

![Work Flow](img/violin_svd.png)

## Looking At The Predictions

movie titles SVD recommendations

![Work Flow](img/recom1.png)

![Work Flow](img/recom2.png)

* User ID: 1

|   movieId | title                                                            | genres                            |
|----------:|:-----------------------------------------------------------------|:----------------------------------|
|      2810 | Perfect Blue (1997)                                              | Animation|Horror|Mystery|Thriller |
|      2563 | Dangerous Beauty (1998)                                          | Drama                             |
|     73290 | Hachiko: A Dog's Story (a.k.a. Hachi: A Dog's Tale) (2009)       | Drama                             |
|     26840 | Sonatine (Sonachine) (1993)                                      | Action|Comedy|Crime|Drama         |
|      5114 | Bad and the Beautiful, The (1952)                                | Drama                             |
|      2267 | Mortal Thoughts (1991)                                           | Mystery|Thriller                  |
|     65642 | Timecrimes (Cronocrímenes, Los) (2007)                           | Sci-Fi|Thriller                   |
|      4965 | Business of Strangers, The (2001)                                | Action|Drama|Thriller             |
|      1289 | Koyaanisqatsi (a.k.a. Koyaanisqatsi: Life Out of Balance) (1983) | Documentary                       |
|      1754 | Fallen (1998)                                                    | Crime|Drama|Fantasy|Thriller      |


* User ID: 2

|   movieId | title                                                                                       | genres               |
|----------:|:--------------------------------------------------------------------------------------------|:---------------------|
|     73290 | Hachiko: A Dog's Story (a.k.a. Hachi: A Dog's Tale) (2009)                                  | Drama                |
|     83318 | Goat, The (1921)                                                                            | Comedy               |
|     67504 | Land of Silence and Darkness (Land des Schweigens und der Dunkelheit) (1971)                | Documentary          |
|     83411 | Cops (1922)                                                                                 | Comedy               |
|     83359 | Play House, The (1921)                                                                      | Comedy               |
|    132333 | Seve (2014)                                                                                 | Documentary|Drama    |
|      2563 | Dangerous Beauty (1998)                                                                     | Drama                |
|     65188 | Dear Zachary: A Letter to a Son About His Father (2008)                                     | Documentary          |
|      3067 | Women on the Verge of a Nervous Breakdown (Mujeres al borde de un ataque de nervios) (1988) | Comedy|Drama         |
|     89904 | The Artist (2011)                                                                           | Comedy|Drama|Romance |

User # 200 NMF/ALS Recs:  
['Art of War, The (2000)', 'King Is Alive, The (2000)', 'Maelström (2000)', 'Journey, The (El viaje) (1992)', 'Ice Princess (2005)', 'Family Stone, The (2005)', 'Flicka (2006)', 'Secretariat (2010)', 'Innocence (2000)', 'I Know That Voice (2013)']

## Conclusion

Our new recommender is THE BEST. Let's use it!


