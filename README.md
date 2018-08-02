# NH Business Webscraper

This project's purpose is to scrape NH public records and return the information of newly formed businesses. This project isn't fully functional yet. Right now, main.py simply scrapes the information for one single business.

## Getting Started
Simply clone the repository to your computer, and installed dependencies located in the Pipfile by using the command "Pipenv install"(no quotes). Alternitavely, if you don't have Pipenv installed, read through the Pipfile and install packages manually.

### Prerequisites

Python 3.6+ (not tested below 3.6) and the following packages (in the pipfile)

```
examples
```

### Installing

My preferred way to install virtual environments for python is using [Pipenv](https://docs.pipenv.org/). 

Change to where you cloned the repository
```
cd C:\users\YOUR_NAME\YOUR_PROJECT_DIR\NH-business-scraper
```
Initialize the directory with Pipenv and create a virtual environment
```
pipenv --python 3.6
```
Install all dependencies from the Pipfile
```
pipenv install
```

## Built With
Python 3.6, PostgreSQL (psycopg2 wrapper), requests, and BeautifulSoup

## Contributing

If you've come across this repository and would like to contribute to this program, I'm happy to collaborate. This was designed as a quick project to learn how to build a webscraper, but I'd love to see it grow. Feel free to reach out through my contact info in the Authors section below.

## Authors

* **Alex Pereira** - *Sole contributor* 
    * GitHub - [alex-a-pereira](https://github.com/alex-pereira)
    * [Alex-a-pereira@outlook.com](mailto:Alex-a-pereira@outlook.com)
    
## License

This project is licensed under the Unlicense - you are free to use it for any purpose. See the [LICENSE.md](LICENSE.md) file for details
