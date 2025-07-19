# 📝 Unit Converter

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-unit-converter?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-unit-converter?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-unit-converter?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-unit-converter?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-unit-converter?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created for learning purposes only.
> It is not intended for production use.

## ℹ️ About

This project is a command-line application built in Python that allows users to convert between various units of temperature, mass, and distance. It's designed to demonstrate clean code structure, encapsulation, and testing with `pytest`.

## 🚀 Features

*   **Temperature Conversion**: Convert between Celsius, Fahrenheit, and Kelvin.
*   **Mass Conversion**: Convert between kilograms, pounds, and grams.
*   **Distance Conversion**: Convert between meters, kilometers, miles, and feet.
*   **Command-Line Interface (CLI)**: Simple interactive interface for user interaction.
*   **Error Handling**: Handles invalid input types and unsupported unit conversions gracefully.
*   **Unit Testing**: Comprehensive tests included using `pytest` to ensure accuracy and reliability.
*   **Clean Project Structure**: Modular organization for clarity, maintainability, and scalability.

## 🛠️ Technologies Used

*   **Python 3.x**
*   **`pytest`**: Framework used to create and run unit tests.

## ⚙️ How to Run the Project

### Prerequisites

Ensure that Python 3.x is installed on your machine.

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/alexandrekatsuura/python-unit-converter
    cd python-unit-converter
    ```

2.  (Optional but recommended) Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate      # On Linux/macOS
    # .venv\Scripts\activate       # On Windows
    ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the program, use the following command:

```bash
python src/main.py
```

You will be prompted to select a conversion type (Temperature, Mass, or Distance) and then enter the value, source unit, and target unit. The program will display the converted result.

## ✅ Running the Tests

To run the unit tests, from the project root directory:

```bash
pytest -v
```

This will execute all test cases located in the `tests/` directory, ensuring the conversion logic is working correctly.

## 📁 Project Structure

```bash
python-unit-converter/
├── src/
│   ├── main.py             # Main application entry point and CLI logic
│   └── converter.py        # Core conversion logic for temperature, mass, and distance
├── tests/
│   └── test_converter.py   # Unit tests for the Converter class
├── .gitignore              # Specifies intentionally untracked files to ignore by Git
├── README.md               # Project documentation and setup instructions
└── requirements.txt        # Lists project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).


