# JokeMachine

A fun command-line joke generator with multiple categories, fun facts, and an interactive mode.

```ascii
     _       _         __  __            _     _            
    | | ___ | | _____ |  \/  | __ _  ___| |__ (_)_ __   ___ 
 _  | |/ _ \| |/ / _ \| |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
| |_| | (_) |   <  __/| |  | | (_| | (__| | | | | | | |  __/
 \___/ \___/|_|\_\___||_|  |_|\__,_|\\___|_| |_|_|_| |_|\___|
```

## Installation

You can install JokeMachine directly from PyPI:

```bash
pip install joke-machine
```

Or install from source:

```bash
git clone https://github.com/yourusername/joke_machine.git
cd joke_machine
pip install -e .
```

## Usage

JokeMachine can be used as a module or as a command-line tool.

### Command-line Usage

```bash
# Tell a random joke
python -m joke_machine --joke

# Tell a joke from a specific category
python -m joke_machine --category programming

# Tell a random fun fact
python -m joke_machine --fact

# Save the joke to your favorites
python -m joke_machine --joke --save

# List your favorite jokes
python -m joke_machine --favorites

# Run in interactive mode (recommended for the full experience)
python -m joke_machine --interactive
```

After installation, you can also use the shorthand command:

```bash
joke-machine --joke
```

### Available Categories

- **programming**: Jokes about programming and tech
- **dad**: Classic dad jokes that will make you groan
- **puns**: Clever wordplay to brighten your day

### Interactive Mode

The interactive mode provides a conversation-like interface to all features:

```bash
python -m joke_machine --interactive
```

In interactive mode, you can:
- Request jokes from specific categories
- Get fun facts
- Save jokes to your favorites collection
- List all your saved favorites
- View available categories

Just type `help` in the interactive prompt to see all available commands.

## Features

- Multiple joke categories (programming, dad jokes, puns)
- Random fun facts
- Interactive command-line interface
- Save your favorite jokes for later
- Dramatic pause delivery for better comedic effect
- Typical responses to dad jokes

## Configuration

JokeMachine stores your favorite jokes in a JSON file at:
```
~/.joke_machine_favorites.json
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to add more jokes, features, or improvements.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Add your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request