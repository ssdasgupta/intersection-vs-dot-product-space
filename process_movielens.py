import pandas as pd
import numpy as np
from collections import defaultdict

def create_item_tag_dict():
    """
    Create an item-tag dictionary from MovieLens data where tags are movie genres.
    """
    # Read the movies data
    movies = pd.read_csv('data/movies.csv')
    
    # Create item-tag dictionary
    item_tag_dict = {}
    
    for _, row in movies.iterrows():
        movie_id = str(row['movie_id'])
        # Split genres and clean them
        genres = [genre.strip().lower() for genre in row['genres'].split('|')]
        item_tag_dict[movie_id] = genres
    
    return item_tag_dict

def analyze_genre_distribution(item_tag_dict):
    """
    Analyze the distribution of genres in the dataset.
    """
    genre_counts = defaultdict(int)
    for tags in item_tag_dict.values():
        for tag in tags:
            genre_counts[tag] += 1
    
    print("\nGenre Distribution:")
    for genre, count in sorted(genre_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{genre}: {count} movies")
    
    return genre_counts

if __name__ == "__main__":
    # Create item-tag dictionary
    item_tag_dict = create_item_tag_dict()
    
    # Analyze genre distribution
    genre_counts = analyze_genre_distribution(item_tag_dict)
    
    # Print some example items
    print("\nExample Items:")
    for movie_id, tags in list(item_tag_dict.items())[:5]:
        print(f"Movie {movie_id}: {tags}")
    
    # Save the item-tag dictionary
    with open('data/item_tag_dict.txt', 'w') as f:
        for movie_id, tags in item_tag_dict.items():
            f.write(f"{movie_id}: {', '.join(tags)}\n")
    
    print("\nItem-tag dictionary has been saved to data/item_tag_dict.txt") 