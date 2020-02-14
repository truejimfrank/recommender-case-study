import sys
import numpy as np
import pandas as pd
from collections import defaultdict
from surprise import Dataset, SVD, accuracy, Reader
from surprise.model_selection import train_test_split
from surprise.model_selection.validation import cross_validate
from baselines import GlobalMean, MeanofMeans

reader = Reader(name=None,
                line_format='user item rating',
                sep=',',
                rating_scale=(1,5),
                skip_lines=1)

data = Dataset.load_from_file('../data/movies/ratings.csv', reader=reader)

def get_top_n(predictions, n=5):

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


def recs_dict(top_n, name_df):
    recs_dict = dict()
    for uid, user_ratings in top_n.items():
        # print(uid, [name_df.loc[int(iid)]['title'] for (iid, _) in user_ratings])
        recs_dict[int(uid)] = [name_df.loc[int(iid)]['title'] for (iid, _) in user_ratings]
    return recs_dict


if __name__ == "__main__":
    
    name_df = pd.read_csv('../data/movies/movies.csv', header=0, index_col=0)
    # # cross_validate(algo, data, verbose=True)
    
    trainset = data.build_full_trainset()
    testset = trainset.build_anti_testset()
    
    user = 600

    # algo = SVD()
    # algo.fit(trainset)
    # predictions = algo.test(testset)
    
    # top_n = get_top_n(predictions, n=10)
    # svd_dict = recs_dict(top_n, name_df)
    # print(recs_dict[user])

    # algo = GlobalMean()
    # algo.fit(trainset)
    # predictions = algo.test(testset)
    
    # top_n = get_top_n(predictions, n=10)
    # mean_dict = recs_dict(top_n, name_df)
    # print(recs_dict[user])

    algo = MeanofMeans()
    algo.fit(trainset)
    predictions = algo.test(testset)
    
    top_n = get_top_n(predictions, n=10)
    mean_mean_dict = recs_dict(top_n, name_df)
    print(recs_dict[user])



    # trainset, testset = train_test_split(data, test_size=.25)

    # Train the algorithm on the trainset, and predict ratings for the testset
    # algo.fit(trainset)
    # predictions = algo.test(testset)

    # # Then compute RMSE
    # accuracy.rmse(predictions)