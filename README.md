# RecommendationSystem

In this recommendation system, we used the publicly available MoveLens dataset.
The MovieLens dataset contains information about movie ratings by users, information about
movies and users. The number of movies in the dataset is 1682 and number of users is 943.
The movie data has been split based on their genre and later outer joined with ratings of
movies in order to get user preference, average rating and consumption ratio for each genre
of movies in three separate approaches. This resulted in each tuple having 18 attributes in all
the approaches since there are 18 genres listed in MovieLens dataset. Clustering was used
to separate dissimilar users and the result was compared in the three approaches to choose
the best one. Principal Component Analysis (PCA) was used to decrease the dimension for
a better clustering result. Feature scaling was done to normalize the input matrix. Then for
each cluster, the ratings of the movies were predicted using a neural network.
Recommendations were made based on the average rating given to different movies by a
user and the predicted rating for a user.

Scripts:

recommender.py takes as input a user id and prints top 5 recommended movies for a user.
