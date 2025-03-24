"""
JokeMachine - A fun tool that generates jokes, puns, and programming humor
using Python's standard library.
"""
# ruff: noqa: W291

import argparse
import json
import os
import random
import sys
import textwrap
import time
from datetime import datetime

__version__ = "0.1.0"

# Collection of jokes organized by category
JOKES = {
    "programming": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why did the developer go broke? Because he used up all his cache!",
        "!false - It's funny because it's true!",
        "A programmer puts two glasses on his bedside table before going to sleep. One full of water in case he gets thirsty, and one empty in case he doesn't.",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "Why do Python programmers wear glasses? Because they can't C#.",
        "What's a programmer's favorite hangout place? The Foo Bar.",
    ],
    "dad": [
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What did the ocean say to the beach? Nothing, it just waved.",
        "I would tell you a joke about pizza, but it's too cheesy.",
        "Why don't eggs tell jokes? They'd crack each other up.",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a fake noodle? An impasta!",
        "How do you organize a space party? You planet!",
    ],
    "puns": [
        "I was wondering why the ball was getting bigger. Then it hit me.",
        "I'm on a seafood diet. I see food and I eat it.",
        "What's the best time to go to the dentist? Tooth-hurty!",
        "I used to be a baker, but I couldn't make enough dough.",
        "Becoming a vegetarian is a huge missed steak.",
        "I've got a great joke about construction, but I'm still working on it.",
        "I was going to tell a time traveling joke, but you didn't like it.",
        "What do you call a parade of rabbits hopping backwards? A receding hare-line.",
        "The shovel was a ground-breaking invention.",
        "I was addicted to the hokey pokey... but then I turned myself around.",
    ],
}

# Collection of fun facts
FUN_FACTS = [
    "A day on Venus is longer than a year on Venus.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    "The average person will spend six months of their life waiting for red lights to turn green.",
    "A group of flamingos is called a 'flamboyance'.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat.",
    "The first computer 'bug' was an actual real-life bug. A moth was found trapped in a Harvard Mark II computer in 1947.",
    "In Python, the 'antigravity' module opens a web browser to a comic about Python.",
    "The average person walks the equivalent of five times around the world in their lifetime.",
    "Cats can't taste sweet things because of a genetic mutation.",
    "The inventor of the Pringles can is buried in one (at his request).",
]

# ASCII art for the header
HEADER_ART = """
     _       _         __  __            _     _            
    | | ___ | | _____ |  \\/  | __ _  ___| |__ (_)_ __   ___ 
 _  | |/ _ \\| |/ / _ \\| |\\/| |/ _` |/ __| '_ \\| | '_ \\ / _ \\
| |_| | (_) |   <  __/| |  | | (_| | (__| | | | | | | |  __/
 \\___/ \\___/|_|\\_\\___||_|  |_|\\__,_|\\___|_| |_|_|_| |_|\\___|
"""


def print_header():
    """
    Print the JokeMachine ASCII art header and version information.

    This function displays the ASCII art logo for JokeMachine along with
    the current version number to provide a visual introduction to the program.

    Examples
    --------
    >>> print_header()  # doctest: +SKIP
    """
    print(HEADER_ART)
    print(f"JokeMachine v{__version__} - Your daily dose of humor\n")


def get_joke(category=None):
    """
    Get a random joke, optionally from a specific category.

    Parameters
    ----------
    category : str, optional
        The joke category to select from ('programming', 'dad', or 'puns').
        If None or invalid, a joke from any category will be returned.

    Returns
    -------
    str
        A randomly selected joke from the specified category or from all categories.

    Examples
    --------
    >>> import random
    >>> random.seed(42)  # For reproducible testing
    >>> joke = get_joke('programming')
    >>> joke in JOKES['programming']
    True

    >>> random.seed(42)
    >>> joke = get_joke()  # Random joke from any category
    >>> any(joke in jokes for jokes in JOKES.values())
    True
    """
    if category and category in JOKES:
        return random.choice(JOKES[category])

    # If no category specified or invalid category, choose from all jokes
    all_jokes = []
    for jokes in JOKES.values():
        all_jokes.extend(jokes)
    return random.choice(all_jokes)


def get_fun_fact():
    """
    Get a random fun fact from the collection.

    Returns
    -------
    str
        A randomly selected fun fact.

    Examples
    --------
    >>> import random
    >>> random.seed(42)
    >>> fact = get_fun_fact()
    >>> fact in FUN_FACTS
    True
    """
    return random.choice(FUN_FACTS)


def generate_dad_joke_response():
    """
    Generate a typical humorous response to a dad joke.

    Returns
    -------
    str
        A randomly selected response appropriate for reacting to a dad joke.

    Examples
    --------
    >>> import random
    >>> random.seed(42)
    >>> response = generate_dad_joke_response()
    >>> isinstance(response, str)
    True
    >>> len(response) > 0
    True
    """
    responses = [
        "*groans*",
        "*eye roll*",
        "Daaaaad! Stop it!",
        "*audible sigh*",
        "That was terrible...",
        "I can't believe you just said that.",
        "*face palm*",
        "I'm not laughing. (But I am)",
        "Please, no more!",
        "That's so bad it's good.",
    ]
    return random.choice(responses)


def tell_joke_with_delay(joke, delay=1.5):
    """
    Print a joke with a dramatic pause for better comedic effect.

    This function splits the joke at a natural break point (either after a question
    mark or after the first sentence) and adds a pause before delivering the punchline.

    Parameters
    ----------
    joke : str
        The joke text to be displayed.
    delay : float, optional
        The pause duration in seconds between setup and punchline. Default is 1.5.

    Examples
    --------
    >>> tell_joke_with_delay("Why did the chicken cross the road? To get to the other side.", 0.1)  # doctest: +SKIP
    Why did the chicken cross the road?
    To get to the other side.

    >>> tell_joke_with_delay("I'm reading a book about anti-gravity. It's impossible to put down!", 0.1)  # doctest: +SKIP
    I'm reading a book about anti-gravity.
    It's impossible to put down!
    """
    if "?" in joke:
        setup, punchline = joke.split("?", 1)
        print(f"{setup}?")
        time.sleep(delay)
        print(f"{punchline}")
    else:
        parts = joke.split(". ")
        if len(parts) > 1:
            print(f"{parts[0]}.")
            time.sleep(delay)
            print(f"{'. '.join(parts[1:])}")
        else:
            print(joke)


def save_favorite(joke):
    """
    Save a joke to the user's favorites file.

    This function saves the provided joke to a JSON file in the user's home directory
    along with a timestamp of when it was saved.

    Parameters
    ----------
    joke : str
        The joke text to save to favorites.

    Notes
    -----
    The favorites are stored in ~/.joke_machine_favorites.json

    Examples
    --------
    >>> save_favorite("Why do programmers prefer dark mode? Because light attracts bugs!")  # doctest: +SKIP
    Joke saved to favorites at ~/.joke_machine_favorites.json
    """
    favorites_file = os.path.expanduser("~/.joke_machine_favorites.json")

    # Create or load existing favorites
    if os.path.exists(favorites_file):
        with open(favorites_file) as f:
            try:
                favorites = json.load(f)
            except json.JSONDecodeError:
                favorites = []
    else:
        favorites = []

    # Add the new favorite with timestamp
    favorites.append(
        {"joke": joke, "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    )

    # Save back to file
    with open(favorites_file, "w") as f:
        json.dump(favorites, f, indent=2)

    print(f"Joke saved to favorites at {favorites_file}")


def list_favorites():
    """
    List all jokes saved in the user's favorites file.

    This function reads the favorites file from the user's home directory
    and displays all saved jokes along with their save timestamps.

    Notes
    -----
    The favorites are read from ~/.joke_machine_favorites.json

    Examples
    --------
    >>> list_favorites()
    You haven't saved any favorites yet.
    """
    favorites_file = os.path.expanduser("~/.joke_machine_favorites.json")

    if not os.path.exists(favorites_file):
        print("You haven't saved any favorites yet.")
        return

    with open(favorites_file) as f:
        try:
            favorites = json.load(f)
            if not favorites:
                print("Your favorites list is empty.")
                return

            print("\n=== Your Favorite Jokes ===\n")
            for i, fav in enumerate(favorites, 1):
                joke = fav["joke"]
                saved_at = fav["saved_at"]
                print(f"{i}. {joke}")
                print(f"   Saved on: {saved_at}")
                print()

        except json.JSONDecodeError:
            print("Error reading favorites file. It might be corrupted.")


def interactive_mode():
    """
    Run the joke machine in an interactive command-line interface mode.

    This function starts an interactive session where users can enter
    commands to get jokes, fun facts, manage favorites, and more.

    Commands
    --------
    joke [category] : Get a joke, optionally from a specific category
    fact : Get a random fun fact
    save : Save the last joke to favorites
    favorites : List saved favorite jokes
    categories : List available joke categories
    help : Show available commands
    exit/quit : Exit interactive mode

    Examples
    --------
    >>> interactive_mode()  # doctest: +SKIP
    """
    print_header()
    print("Welcome to Interactive Mode!")
    print("Type 'exit' or 'quit' to leave, 'help' for commands.\n")

    last_joke = None

    while True:
        command = input("\nWhat would you like? > ").strip().lower()

        if command in ("exit", "quit"):
            print("Thanks for laughing with JokeMachine! Goodbye!")
            break

        elif command == "help":
            print("\nAvailable commands:")
            print(
                "  joke [category] - Tell a joke (categories: programming, dad, puns)"
            )
            print("  fact            - Tell a fun fact")
            print("  save            - Save the last joke to favorites")
            print("  favorites       - List your favorite jokes")
            print("  categories      - List joke categories")
            print("  exit/quit       - Exit the program")
            print("  help            - Show this help message")

        elif command.startswith("joke"):
            parts = command.split()
            category = parts[1] if len(parts) > 1 and parts[1] in JOKES else None

            joke = get_joke(category)
            tell_joke_with_delay(joke)

            # For dad jokes, add a response
            if category == "dad" or (not category and joke in JOKES["dad"]):
                time.sleep(1)
                print(f"\n{generate_dad_joke_response()}")

            # Store the last joke for saving
            last_joke = joke

        elif command == "fact":
            print(get_fun_fact())

        elif command == "save":
            if last_joke:
                save_favorite(last_joke)
            else:
                print("No joke to save. Tell a joke first!")

        elif command == "favorites":
            list_favorites()

        elif command == "categories":
            print("\nAvailable joke categories:")
            for category in JOKES:
                print(f"  - {category} ({len(JOKES[category])} jokes)")

        else:
            print("I didn't understand that. Type 'help' for available commands.")


def main():
    """
    Main function to run the joke machine based on command-line arguments.

    This function parses command-line arguments and executes the appropriate
    functionality based on the provided options.

    Command-line Arguments
    ---------------------
    --joke, -j : Tell a random joke
    --category, -c : Specify joke category (programming, dad, puns)
    --fact, -f : Tell a random fun fact
    --save, -s : Save the joke to favorites
    --favorites : List your favorite jokes
    --interactive, -i : Run in interactive mode
    --version, -v : Show version information

    Examples
    --------
    >>> import sys
    >>> sys.argv = ['joke_machine', '--joke']
    >>> main()  # doctest: +SKIP

    >>> sys.argv = ['joke_machine', '--category', 'programming']
    >>> main()  # doctest: +SKIP

    >>> sys.argv = ['joke_machine', '--interactive']
    >>> main()  # doctest: +SKIP
    """
    parser = argparse.ArgumentParser(
        description="JokeMachine - A fun tool for jokes and humor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
        Examples:
          python -m joke_machine --joke
          python -m joke_machine --category programming
          python -m joke_machine --fact
          python -m joke_machine --interactive
        """),
    )

    parser.add_argument("--joke", "-j", action="store_true", help="Tell a random joke")
    parser.add_argument(
        "--category", "-c", choices=list(JOKES.keys()), help="Specify joke category"
    )
    parser.add_argument(
        "--fact", "-f", action="store_true", help="Tell a random fun fact"
    )
    parser.add_argument(
        "--save", "-s", action="store_true", help="Save the joke to favorites"
    )
    parser.add_argument(
        "--favorites", action="store_true", help="List your favorite jokes"
    )
    parser.add_argument(
        "--interactive", "-i", action="store_true", help="Run in interactive mode"
    )
    parser.add_argument(
        "--version", "-v", action="version", version=f"JokeMachine v{__version__}"
    )

    args = parser.parse_args()

    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return

    # If interactive mode requested
    if args.interactive:
        interactive_mode()
        return

    # Print header for non-interactive mode
    print_header()

    # Handle command-line arguments
    if args.favorites:
        list_favorites()
        return

    if args.joke or args.category:
        joke = get_joke(args.category)
        tell_joke_with_delay(joke)

        # For dad jokes, add a response
        if args.category == "dad" or (not args.category and joke in JOKES["dad"]):
            time.sleep(1)
            print(f"\n{generate_dad_joke_response()}")

        if args.save:
            save_favorite(joke)

    elif args.fact:
        print(get_fun_fact())

__name__ = "joke_machine"