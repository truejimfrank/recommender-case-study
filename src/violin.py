from surprise import SVD, Dataset, accuracy, Reader
from surprise.model_selection import cross_validate

# https://surprise.readthedocs.io/en/stable/getting_started.html
# Load the movielens-100k dataset (download it if needed),
# data = Dataset.load_builtin('ml-100k')
# We'll use the famous SVD algorithm.
algo = SVD()
# Run 5-fold cross-validation and print results
# cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# alright, now lets load the csv data and work with it

reader = Reader(name=None,
                line_format='user item rating',
                sep=',',
                rating_scale=(1,5),
                skip_lines=1)

datacsv = Dataset.load_from_file('../data/movies/ratings.csv', reader=reader)

cross_validate(algo, datacsv, measures=['RMSE', 'MAE'], cv=5, verbose=True)




# Create array of predictions for violinplot
# data = [predictions_df['prediction'][predictions_df['rating'] == rating].values for rating in range(1, 6)]
# plt.violinplot(data, range(1,6), showmeans=True)
# plt.xlabel('True Ratings')
# plt.ylabel('Predicted Ratings')
# plt.title('True vs. ALS Recommender Predicted Ratings')
# plt.show()