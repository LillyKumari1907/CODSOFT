import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def main():
    # 1. Create a mock database of books and their descriptions
    data = {
        'Book Title': [
            'The Hobbit',
            'Harry Potter and the Scorcerer\'s Stone',
            '1984',
            'Brave New World',
            'The Hunger Games',
            'To Kill a Mockingbird'
        ],
        'Description': [
            'Fantasy adventure featuring elves, dwarves, and a dragon.',
            'Fantasy novel about a young wizard, magic, and a dark lord.',
            'Dystopian science fiction about totalitarianism and surveillance.',
            'Dystopian science fiction exploring a futuristic society and genetic engineering.',
            'Dystopian action novel about a survival tournament and rebillion.',
            'Classic fiction exploring racial injustice and moral growth in the south.'
        ]
    }

    # Load data into a Pandas DataFrame
    df = pd.DataFrame(data)

    # 2. Convert the text descriptions into numerical vectors (TF-IDF)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['Description'])

    # 3. Calculate the similarity between all books
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def recommend_books(title, num_recommendations=2):
        """Finds books similar to the given title"""
        # Check if the exact title exists in our database
        if title not in df['Book Title'].values:
            return["Book not found."] 
        
        # Get the ID of the book the user searched for
        idx = df.index[df['Book Title'] == title].tolist()[0]

        # Get a list of similarity scores for that book
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the books based on the highest similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Grab the top matches
        sim_scores = sim_scores[1:num_recommendations+1]

        # Get the actual book indices
        book_indices = [i[0] for i in sim_scores]

        # Return the titles of the recommended books
        return df['Book Title'].iloc[book_indices].tolist()
    
    # --- INTERACTIVE TERMINAL APP ---
    print("\n--- Welcome to the Book Recommendation System ---")
    print("Available books in our database:")
    for book in df['Book Title']:
       print(f"- {book}")

    # This loop keeps the program running until the user types 'quit'
    while True:
        # Get the input from the user
        user_input = input("\nEnter a book you liked (or type 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Thanks for using the recmmendation system. Goodbye!")
            break

        recommendations = recommend_books(user_input)
    
        if recommendations == ["Book not found."]:
            print("Sorry, that book isn't in our database. Please check your spelling and try again!")
        else:
            print(f"\nBecause you read '{user_input}', we recommend:")
            for i, book in enumerate(recommendations, 1):
                print(f"{i}. {book}")

if __name__ == "__main__":
    main()
