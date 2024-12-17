# Advent of Code 2024
This is the second year in a row that I participate in the challenge [Advent of Code](https://adventofcode.com/2024). I chose to use Python again since I have get used to it and feel pretty comfortable to solve the challenges with it.

## How to run the solutions
I used Python 3.11.4 for this time and Visual Studio Code as the IDE. I used a library `common.utils` that I created myself in order to retrieve the input directly from the website. Therefore, it is necessary to set an `.env` file in the root directory of the project with the following values:
```bash
YEAR=2024
SESSION_COOKIE=SESSION_COOKIE_VALUE
```

To get the `SESSION_COOKIE_VALUE`:
1. Login on Advent of Code with your account.
Open your browser’s developer console. This is usually done by right-clicking on the page and selecting “Inspect” or "Inspect Element".
1. Navigate to the Network tab in the developer console.
2. Refresh the page or navigate to any input page, such as https://adventofcode.com/2024/day/1/input.
3. In the list of network requests, click on the request for the page you just loaded. This will open a panel with details about the request.
4. Look for the “Cookie” header in the request headers section. The value of this header is your session cookie. Once this is set, you can launch any of the scripts by clicking on `Run Python File` in Visual Studio Code.

Then, it is necessary to install the required libraries. They are all set in the `requirements.txt` file. In order to do this, run:
```bash
pip install -r requirements.txt
```

> [!NOTE]  
> [Python](https://www.python.org/downloads/) must be installed in order to run the scripts.