import pyspark as ps
from pyspark.sql import SparkSession

import random

import pandas as pd
import numpy as np

from pyspark.ml.recommendation import ALS


from pyspark.ml import Pipeline
from pyspark.ml.linalg import Vectors
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.regression import LinearRegression
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

from pyspark.sql import Row


class Recommender(object):

    def __init__(self, ratings, movies):
        '''
        Input 
            ratings: ratings DataFrame
            movies: movies DataFrame
        '''
        spark_df = spark.createDataFrame(ratings_df)
        spark_df = spark_df.drop("timestamp") #drop timestamp
        
        als_model = ALS(
        itemCol='movieId',
        userCol='userId',
        ratingCol='rating',
        nonnegative=True,    
        regParam=0.1,
        rank=10)

        self.model = als_model.fit(spark_df)
        self.movies = movies

    def recommend_for_user(self, userid):

        one_row_pandas_df = pd.DataFrame({'userId': [userid]})
        one_row_spark_df = spark.createDataFrame(one_row_pandas_df)
        rec_movies = self.model.recommendForUserSubset(one_row_spark_df, 10).collect()
        movie_ids = [row.movieId for row in rec_movies[0].recommendations]
        
        return movie_ids
        #return self.movies.loc[movie_ids,:].values.tolist()


# Setup a SparkSession
spark = SparkSession.builder.getOrCreate()

ratings_df = pd.read_csv('../data/movies/ratings.csv',sep=',', header=0)
movies_df = pd.read_csv('../data/movies/movies.csv',sep=',', header=0, index_col="movieId")


#ratings_df.drop("timestamp", axis=1)
movies_df.drop("genres", axis=1)

# Convert a Pandas DF to a Spark DF
spark_df = spark.createDataFrame(ratings_df)
spark_df = spark_df.drop("timestamp") #drop timestamp


# Convert a Spark DF to a Pandas DF
#pandas_df = spark_df.toPandas()

train, test = spark_df.randomSplit([0.8, 0.2], seed=427471138)

num_ratings = train.count()
num_users = train.select("userId").distinct().count()
num_items = train.select("movieId").distinct().count()

print(num_ratings / (num_users * num_items))

als_model = ALS(
    itemCol='movieId',
    userCol='userId',
    ratingCol='rating',
    nonnegative=True,    
    regParam=0.1,
    rank=10)

model = als_model.fit(train)

predictions = model.transform(test)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                predictionCol="prediction")
predictions = predictions.na.drop(how='any')
rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))

rec = Recommender(ratings_df, movies_df)
result_ids = rec.recommend_for_user(2)
print(result_ids)

#HOW TO USE
#result_ids = rec.recommend_for_user(2)
#movies_df.loc[result_ids,:].to_markdown()



# #prediction user=1, item=100 by dot product by transform
# one_row_pandas_df = pd.DataFrame({'userId': [1], 'movieId': [100]})
# one_row_spark_df = spark.createDataFrame(one_row_pandas_df)
# model.transform(one_row_spark_df).collect()

# model.itemFactors.show(truncate=False, vertical=False)
# model.userFactors.show(truncate=False, vertical=False)

# #prediction user=1, item=100 by dot product
# factors = model.userFactors
# user_features = factors.where(factors.id==1).select(factors.features).first()
# factors = model.itemFactors
# item_features = factors.where(factors.id==100).select(factors.features).first()
# user_item_rating = np.sum([a * b for a, b in zip(user_features[0], item_features[0])])

#Prediction for training dataset by transform
#prediction = model.transform(train)

#is there none value expected rating?
#prediction.where(prediction["prediction"] == None).select(prediction["userId"]).show()

#describe
#prediction.describe().show()



