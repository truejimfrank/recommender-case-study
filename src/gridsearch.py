import sys
import numpy as np
import pandas as pd
from collections import defaultdict
from surprise import Dataset, SVD, accuracy, Reader, NMF
from surprise.model_selection import train_test_split, GridSearchCV
from surprise.model_selection.validation import cross_validate
from baselines import GlobalMean, MeanofMeans

reader = Reader(name=None,
                line_format='user item rating',
                sep=',',
                rating_scale=(1,5),
                skip_lines=1)

data = Dataset.load_from_file('../data/movies/ratings.csv', reader=reader)

svd_grid = {'n_epochs': [5, 10, 20],
              'n_factors': [1, 5, 10, 20, 50],
              'lr_all': [0.002, 0.005, 0.01],
              'reg_all': [0.2, 0.4, 0.6],
              'init_mean': [0, 3.5]}

als_grid = {'n_epochs': [5, 10, 20, 50],
            'n_factors': [1, 5, 10, 20, 50, 100],
            'biased': [True, False]}

gs_svd = GridSearchCV(SVD, svd_grid, measures=['rmse', 'mae'], cv=5, n_jobs=-2, joblib_verbose=True)

gs_nmf = GridSearchCV(NMF, als_grid, measures=['rmse', 'mae'], cv=5, n_jobs=-2, joblib_verbose=5)

svd = SVD(n_epochs=20, n_factors=50, lr_all=0.01, reg_all=0.02, init_mean=0)

nmf = NMF(n_epochs=50, n_factors=1, biased=True)


if __name__ == "__main__":    

    gs_nmf.fit(data)
    print(gs_nmf.best_score['rmse'])
    print(gs_nmf.best_params['rmse'])

    gs_svd.fit(data)
    print(gs_svd.best_score['rmse'])
    print(gs_svd.best_params['rmse'])


    # cross_validate(algo, data, verbose=True)

    
    # trainset = data.build_full_trainset()
    # testset = trainset.build_anti_testset()

    # trainset, testset = train_test_split(data, test_size=.25)

    # Train the algorithm on the trainset, and predict ratings for the testset
    # algo.fit(trainset)
    # predictions = algo.test(testset)

    # # Then compute RMSE
    # accuracy.rmse(predictions)