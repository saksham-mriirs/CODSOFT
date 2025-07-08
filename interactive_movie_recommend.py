import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset
movies = pd.DataFrame({
    'title': [
        'The Matrix', 'John Wick', 'Avengers: Endgame', 'Inception',
        'The Notebook', 'Titanic', 'Interstellar', 'The Godfather'
    ],
    'genre': [
        'sci-fi action', 'action thriller', 'superhero action', 'sci-fi thriller',
        'romance drama', 'romance drama', 'sci-fi drama', 'crime drama'
    ]
})

# Vectorize genres
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genre'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Recommend function
def recommend_movies(title, num_recommendations=3):
    title = title.strip().title()
    if title not in indices:
        return None
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# Extra commands
def show_help():
    print("\n🛠️ Available commands:")
    print("  • Enter a movie title (e.g. Inception)")
    print("  • list movies — show all available movies")
    print("  • what can you do — explains features")
    print("  • who made you — shows author info")
    print("  • exit — quits the program")

def list_movies():
    print("\n🎬 Available movies:")
    for title in movies['title']:
        print("  •", title)

def main():
    print("🎥 Welcome to the Movie Recommender Bot!")
    print("Type 'help' for commands or 'exit' to quit.\n")

    while True:
        user_input = input("🎬 Enter a movie you like: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Enjoy your movies!")
            break
        elif user_input.lower() == "help":
            show_help()
        elif user_input.lower() == "list movies":
            list_movies()
        elif user_input.lower() == "what can you do":
            print("\n🤖 I can recommend movies based on genre similarity. Try typing a movie name!")
        elif user_input.lower() == "who made you":
            print("\n🧠 I was coded by Saksham !")
        elif user_input == "":
            print("⚠️ Please enter a movie title or command. Type 'help' if you're unsure.")
        else:
            recommendations = recommend_movies(user_input)
            if recommendations:
                print(f"\n✅ Because you liked '{user_input.title()}', you might also like:")
                for rec in recommendations:
                    print("  •", rec)
            else:
                print(f"❌ Movie '{user_input}' not found. Type 'list movies' to see available titles.")

# Run the interactive loop
if __name__ == "__main__":
    main()
