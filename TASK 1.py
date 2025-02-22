# project 1 
def fizz_buzz():
    for i in range(1, 101):  
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()


# project 2
def movie_budget_analysis():
    movies = [
        ("Horror Excellence", 20000000),
        ("Laugh Riot", 9000000),
        ("Fantasy Saga", 4500000),
        ("Tearjerker Drama", 379000000),
        ("Comic Gold", 365000000),
        ("Fictional Masterpiece", 356000000),
        ("Magical Voyage", 200000000)
    ]

    num_movies_to_add = int(input("How many movies would you like to add? "))
    for _ in range(num_movies_to_add):
        name = input("Enter the movie name: ")
        budget = int(input("Enter the movie budget: "))
        movies.append((name, budget))
    total_budget = sum(movie[1] for movie in movies)
    average_budget = total_budget / len(movies)

    print(f"\nThe average budget is: ${average_budget:,.2f}")

    high_budget_movies = [(name, budget) for name, budget in movies if budget > average_budget]
    print("\nMovies with budgets higher than the average:")
    for name, budget in high_budget_movies:
        difference = budget - average_budget
        print(f"- {name}: ${budget:,.2f} (exceeds by ${difference:,.2f})")

    print(f"\nNumber of movies with budgets higher than the average: {len(high_budget_movies)}")
movie_budget_analysis()