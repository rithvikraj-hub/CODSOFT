# Movie Recommendation System

## Overview

This project implements a simple Movie Recommendation System using Python. The system recommends movies to users based on their preferred genre. It provides a list of highly rated movies from the selected category, helping users discover movies that match their interests.

The project demonstrates the basic concepts of recommendation systems and user preference-based suggestions.

## Features

* Recommends movies based on genre preferences
* Multiple movie categories available
* Displays movie ratings along with recommendations
* User-friendly command-line interface
* Handles invalid inputs gracefully
* Allows users to receive multiple recommendations in one session

## Technologies Used

* Python 3
* Dictionaries
* Lists and Tuples
* Loops
* Conditional Statements
* Functions

## Project Structure

```text
FUTURE_ML_04/
│
├── movie_recommendation.py
├── README.md
└── requirements.txt
```

## How It Works

1. The system displays available movie genres.
2. The user selects a preferred genre.
3. The program retrieves movies belonging to that genre.
4. Recommended movies are displayed along with their ratings.
5. The user can continue exploring recommendations or exit the program.

## Available Genres

* Action
* Comedy
* Romance
* Sci-Fi
* Thriller

## Sample Output

```text
============================================================
           MOVIE RECOMMENDATION SYSTEM
============================================================

Available Genres:
- Action
- Comedy
- Romance
- Sci-Fi
- Thriller

Enter your preferred genre: sci-fi

Top Sci-Fi Movie Recommendations:

🎬 Interstellar | ⭐ Rating: 5.0/5
🎬 Inception | ⭐ Rating: 4.9/5
🎬 The Matrix | ⭐ Rating: 4.8/5
🎬 Avatar | ⭐ Rating: 4.7/5
🎬 Dune | ⭐ Rating: 4.8/5
```

## Learning Outcomes

* Understanding recommendation systems
* Working with Python dictionaries and lists
* Implementing user preference-based suggestions
* Handling user input and validation
* Designing menu-driven applications

## Future Enhancements

* Add more movie genres and recommendations
* Store movie data in a CSV file or database
* Implement content-based filtering
* Implement collaborative filtering
* Build a graphical user interface
* Develop a web-based recommendation platform

## Requirements

This project uses only Python's standard library.

Example requirements.txt:

```text
# No external dependencies required
```

## How to Run

Run the following command in the terminal:

```bash
python movie_recommendation.py
```

## Conclusion

This Movie Recommendation System provides personalized movie suggestions based on user preferences. It serves as a beginner-friendly introduction to recommendation systems and demonstrates how user interests can be used to generate relevant recommendations.

