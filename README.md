# Homefun Python Skeleton

Python aid for completing the Gamescrafters Homefun series. Knowingly incomplete functions are marked `# TODO`, but know that completing these functions will not be enough for the later homefuns.

## Requirements

You will need:
* Python 3.5 or higher
* A unix-like environment (Windows users, see Git Bash or WSL)

## Usage 

The program is a barebones CLI application that lets you specify which game you want to solve and to pass inputs to your game initializers. For example, once you complete Homefun 1, the following command:

```
make run ARGS="zero_by 25 1 3 4"
```

...should result in a solution to 25-to-0-by-1-3-or-4; the `zero_by` string let the program know which game we wanted to solve, and the arguments `25 1 3 4` allowed us to specify arguments for the game's parameters. This is part of what you will implement.

## Testing

There are no tests included, but you are encouraged to write your own in the provided `src/tests.py` file. As a suggestion, a useful test is comparing the solver output to the expected output. You can run them with `make test`.
