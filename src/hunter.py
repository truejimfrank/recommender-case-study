import sys
import numpy as np
from surprise import Dataset, SVD, accuracy, Reader
from surprise.model_selection import train_test_split
from surprise.model_selection.validation import cross_validate

reader = Reader(name=None,
                line_format='user item rating',
                sep=',',
                rating_scale=(1,5),
                skip_lines=1)

data = Dataset.load_from_file('../data/movies/ratings.csv', reader=reader)

if __name__ == "__main__":
    
    algo = SVD()

    

    cross_validate(algo, data, verbose=True)

    # trainset, testset = train_test_split(data, test_size=.25)

    # Train the algorithm on the trainset, and predict ratings for the testset
    # algo.fit(trainset)
    # predictions = algo.test(testset)

    # # Then compute RMSE
    # accuracy.rmse(predictions)