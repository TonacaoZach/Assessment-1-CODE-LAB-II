movies = [
    {
        "Title": "Spider-Man: Homecoming",
        "Director": "Jon Watts",
        "Release Year": 2017,
        "Genre": "Action"
    },
    {
        "Title": "Iron Man 3",
        "Director": "Shane Black",
        "Release Year": 2013,
        "Genre": "Action"
    },
    {
        "Title": "The Avengers (2012)",
        "Director": "Joss Whedon",
        "Release Year": 2012,
        "Genre": "Action"
    },
    {
        "Title": "Avengers: Endgame",
        "Director": "Anthony and Joe Russo",
        "Release Year": 2019,
        "Genre": "Action"
    }
]

# Display film details using a loop
for movie in movies:
    print("Title:", movie["Title"])
    print("Director:", movie["Director"])
    print("Release Year:", movie["Release Year"])
    print("Genre:", movie["Genre"])
    print()