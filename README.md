# PDF Generation Script

This repository contains a script that generates PDF documents using the `fpdf` library and data from a CSV file. The script reads data from a `topics.csv` file and creates a PDF document named `output.pdf` based on the provided information.

## Files

1. `script.py`: This Python script uses the `fpdf` library to generate PDF documents. It reads data from the `topics.csv` file and creates a PDF document named `output.pdf`.

2. `topics.csv`: A CSV file containing data about topics for the PDF document generation. Each row includes a topic name and the number of pages associated with that topic.

3. `output.pdf`: The generated PDF document that contains the topics, lines, and footers as specified in the script.

## Usage

1. Install the required library: `fpdf` (install using `pip install fpdf`).
2. Place the `script.py` and `topics.csv` files in the same directory.
3. Run the script using the command: `python script.py`.
4. The script will generate an `output.pdf` file with topics and lines based on the data in `topics.csv`.

## Features

- **PDF Generation**: The script uses the `fpdf` library to create PDF documents with topics and lines.
  
- **Data Input**: Topics and page counts are read from the `topics.csv` file, making it easy to customize the content.

## Dependencies

- Python 3.x
- `fpdf` library (install using `pip install fpdf`)

## Future Enhancements

- Enhance the script to allow customization of font styles, sizes, and colors.
- Add support for generating more complex PDF layouts with images and tables.

## Contribution

Feel free to contribute by suggesting improvements or enhancements through pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note:** This `README.md` file provides an overview of the PDF Generation Script. Customize the content based on your project's specifics.
