movies = {
    "action": [
        "John Wick",
        "Mad Max",
        "The Dark Knight"
    ],
    "comedy": [
        "3 Idiots",
        "Hera Pheri",
        "Dhamaal"
    ],
    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix"
    ],
    "horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle"
    ],
    "drama": [
        "Forrest Gump",
        "The Pursuit of Happyness",
        "The Shawshank Redemption"
    ]
}

while True:

    print("\n===== MOVIE RECOMMENDER =====")
    print("Genres:")

    for genre in movies:
        print("-", genre)

    choice = input(
        "\nChoose Genre: "
    ).lower()

    if choice in movies:

        print("\n🎬 Recommended Movies:\n")

        for movie in movies[choice]:
            print(movie)

    else:

        print("Genre not found.")

    again = input(
        "\nSearch Again? (y/n): "
    )

    if again.lower() != "y":
        break