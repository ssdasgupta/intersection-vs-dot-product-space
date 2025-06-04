import os
import requests
import zipfile
import pandas as pd
import numpy as np

def download_movielens_1m():
    """
    Download and extract the MovieLens 1M dataset.
    Returns the paths to the downloaded files.
    """
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Download URL for MovieLens 1M
    url = "https://files.grouplens.org/datasets/movielens/ml-1m.zip"
    zip_path = "data/ml-1m.zip"
    
    # Download the dataset
    print("Downloading MovieLens 1M dataset...")
    response = requests.get(url, stream=True)
    with open(zip_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # Extract the zip file
    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall('data')
    
    # Remove the zip file
    os.remove(zip_path)
    
    # Return paths to the main files
    base_path = 'data/ml-1m'
    return {
        'ratings': os.path.join(base_path, 'ratings.dat'),
        'movies': os.path.join(base_path, 'movies.dat'),
        'users': os.path.join(base_path, 'users.dat')
    }

def load_movielens_data(file_paths):
    """
    Load the MovieLens data into pandas DataFrames.
    """
    # Load ratings
    ratings = pd.read_csv(
        file_paths['ratings'],
        sep='::',
        names=['user_id', 'movie_id', 'rating', 'timestamp'],
        engine='python',
        encoding='latin1'  # Using latin1 encoding which can handle more characters
    )
    
    # Load movies
    movies = pd.read_csv(
        file_paths['movies'],
        sep='::',
        names=['movie_id', 'title', 'genres'],
        engine='python',
        encoding='latin1'  # Using latin1 encoding which can handle more characters
    )
    
    # Load users
    users = pd.read_csv(
        file_paths['users'],
        sep='::',
        names=['user_id', 'gender', 'age', 'occupation', 'zip_code'],
        engine='python',
        encoding='latin1'  # Using latin1 encoding which can handle more characters
    )
    
    return ratings, movies, users

if __name__ == "__main__":
    # Download and extract the dataset
    file_paths = download_movielens_1m()
    
    # Load the data
    ratings, movies, users = load_movielens_data(file_paths)
    
    # Print basic statistics
    print("\nDataset Statistics:")
    print(f"Number of ratings: {len(ratings)}")
    print(f"Number of users: {len(users)}")
    print(f"Number of movies: {len(movies)}")
    print(f"Average rating: {ratings['rating'].mean():.2f}")
    
    # Save processed data
    print("\nSaving processed data...")
    ratings.to_csv('data/ratings.csv', index=False, encoding='utf-8')
    movies.to_csv('data/movies.csv', index=False, encoding='utf-8')
    users.to_csv('data/users.csv', index=False, encoding='utf-8')
    
    print("Done!") 