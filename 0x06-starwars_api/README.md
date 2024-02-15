# Star Wars Movie Characters Script

This script fetches and prints all characters of a specified Star Wars movie using the Star Wars API.

## Requirements

- Node.js installed on your machine
- The `request` module

## Installation

1. Clone this repository:

```
git clone https://github.com/stevejoels54/alx-interview.git
```

2. Navigate to the project directory:

```
cd 0x06-starwars_api
```

3. Install dependencies:

```
npm install request
```

## Usage

Run the script with Node.js, passing the movie ID as a command-line argument:

```
node 0-starwars_characters <movie_id>
```

Replace `<movie_id>` with the ID of the Star Wars movie you want to retrieve characters for. For example:

```
node 0-starwars_characters.js 3
```

```
./0-starwars_characters.js 3
```

## Example

Running the script with the movie ID `3` (Return of the Jedi) will print the characters from that movie, one character per line.

## Notes

- This script uses the Star Wars API to fetch movie data and character information.
- It utilizes the `request` module for making HTTP requests to the API.
- The characters are printed in the same order as they appear in the `characters` list in the `/films/` endpoint response.

## Credits

- Developed by [Your Name] ([Your GitHub Profile](https://github.com/stevejoels54))

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
