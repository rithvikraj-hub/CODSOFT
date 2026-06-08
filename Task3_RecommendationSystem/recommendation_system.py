def movie_recommendation():

    movies = {

        "action": [
            ("Avengers: Endgame", 4.9),
            ("John Wick", 4.8),
            ("Mission Impossible", 4.7),
            ("Mad Max: Fury Road", 4.8),
            ("The Dark Knight", 5.0)
        ],

        "comedy": [
            ("3 Idiots", 4.9),
            ("Jathi Ratnalu", 4.8),
            ("F2", 4.6),
            ("Hangover", 4.7),
            ("Ready", 4.5)
        ],

        "romance": [
            ("Titanic", 4.9),
            ("The Notebook", 4.8),
            ("Ye Maaya Chesave", 4.7),
            ("Sita Ramam", 4.9),
            ("Geetha Govindam", 4.6)
        ],

        "sci-fi": [
            ("Interstellar", 5.0),
            ("Inception", 4.9),
            ("The Matrix", 4.8),
            ("Avatar", 4.7),
            ("Dune", 4.8)
        ],

        "thriller": [
            ("Drishyam", 4.9),
            ("Vikram Vedha", 4.8),
            ("Gone Girl", 4.7),
            ("Shutter Island", 4.9),
            ("Se7en", 4.8)
        ]
    }

    print("=" * 60)
    print("           MOVIE RECOMMENDATION SYSTEM")
    print("=" * 60)

    while True:

        print("\nAvailable Genres:")
        for genre in movies:
            print("-", genre.title())

        choice = input("\nEnter your preferred genre: ").lower().strip()

        if choice not in movies:
            print("\nGenre not available. Please try again.")
            continue

        print(f"\nTop {choice.title()} Movie Recommendations:\n")

        for movie, rating in movies[choice]:
            print(f"🎬 {movie} | ⭐ Rating: {rating}/5")

        again = input(
            "\nWould you like more recommendations? (yes/no): "
        ).lower().strip()

        if again != "yes":
            print("\nThank you for using the Movie Recommendation System!")
            break


movie_recommendation()
