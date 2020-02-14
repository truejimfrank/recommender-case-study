import sys
import numpy as np
import pandas as pd 
from surprise import SVD
from surprise import accuracy
from surprise import AlgoBase, Dataset
from surprise.model_selection.validation import cross_validate
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation
import sys
import pickle

#MINE aka joshr

class GlobalMean(AlgoBase):
    def __init__(self):

        # Always call base method before doing anything.
        AlgoBase.__init__(self)

    def fit(self, trainset):

        # Here again: call base method before doing anything.
        AlgoBase.fit(self, trainset)

        # Compute the average rating. We might as well use the
        # trainset.global_mean attribute ;)
        self.the_mean = np.mean([r for (_, _, r) in
                                 self.trainset.all_ratings()])

        return self

    def estimate(self, u, i):

        return self.the_mean


class MeanofMeans(AlgoBase):
    def __init__(self):

    # Always call base method before doing anything.
        AlgoBase.__init__(self)


    def fit(self, trainset):

        # Here again: call base method before doing anything.
        AlgoBase.fit(self, trainset)

        users = np.array([u for (u, _, _) in self.trainset.all_ratings()])
        items = np.array([i for (_, i, _) in self.trainset.all_ratings()])
        ratings = np.array([r for (_, _, r) in self.trainset.all_ratings()])

        user_means,item_means = {},{}
        for user in np.unique(users):
            user_means[user] = ratings[users==user].mean()
        for item in np.unique(items):
            item_means[item] = ratings[items==item].mean()

        self.global_mean = ratings.mean()
        self.user_means = user_means
        self.item_means = item_means

    def estimate(self, u, i):
        """
        return the mean of means estimate
        """

        if u not in self.user_means:
            return(np.mean([self.global_mean,
                            self.item_means[i]]))

        if i not in self.item_means:
            return(np.mean([self.global_mean,
                            self.user_means[u]]))

        return(np.mean([self.global_mean,
                        self.user_means[u],
                        self.item_means[i]]))


if __name__ == "__main__":

    # data = Dataset.load_builtin('ml-100k')
    # print("\nGlobal Mean...")
    # algo_global_mean = GlobalMean()
    # cross_validate(algo_global_mean, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

    # print("\nMeanOfMeans...")
    # algo_mean_means = MeanofMeans()
    # cross_validate(algo_mean_means, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

    # print("\nSVD...")
    # algo_svd = SVD()
    # #cross_validate(algo_svd, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

    movies = pd.read_csv('/Users/ramozo_88/DSI/repos/recommender-case-study/data/movies/movies.csv')
    df_ratings = pd.read_csv('/Users/ramozo_88/DSI/repos/recommender-case-study/data/movies/ratings.csv')
    df_links = pd.read_csv('/Users/ramozo_88/DSI/repos/recommender-case-study/data/movies/links.csv')
    df_tags = pd.read_csv('/Users/ramozo_88/DSI/repos/recommender-case-study/data/movies/tags.csv')
    df_movies = movies.copy()
    df_movies['genres'] = df_movies['genres'].str.replace('|',' ')
    # ratings_f = df_ratings.groupby('userId').filter(lambda x: len(x) >= 55)
    # movie_list_rating = ratings_f.movieId.unique().tolist()
    #movies = df_movies[movies.movieId.isin(movie_list_rating)]
    # Mapping_file = dict(zip(movies.title.tolist(), movies.movieId.tolist()))
    # df_tags.drop(['timestamp'],1, inplace=True)
    # ratings_f.drop(['timestamp'],1, inplace=True)
    mixed = pd.merge(df_tags, df_movies, on='movieId', how='right')
    print(mixed)
    print(mixed.columns)
    print(mixed.tag)
    mixed.fillna("", inplace=True)
    mixed = pd.DataFrame(mixed.groupby('movieId')['tag'].apply(
                                          lambda x: "%s" % ' '.join(x)))
    Final = pd.merge(movies, mixed, on='movieId', how='left')
    Final ['metadata'] = Final[['tag', 'genres']].apply(
                                          lambda x: ' '.join(x), axis = 1)
    Final[['movieId','title','metadata']].head(3)