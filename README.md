# DNA Sequence Analysis

This product is an application that users can use to analyze DNA sequences. The product processes a DNA sequence entered into the web application or by uploading a file. The analysis of the DNA sequence includes GC (Guanine and Cytosine) content percentage, start codon detection, stop codons detection, as well as mutations.

## Features

- **GC Content Calculation:** Computes the percentage of guanine (G) and cytosine (C) bases in the DNA sequence.
- **Start Codon Detection:** Checks if the sequence starts with the codon `ATG`.
- **Stop Codon Count:** Counts the occurrences of the stop codons `TAA`, `TAG`, and `TGA`.
- **mutations:** counts how many mutations are found in the sequence based on a generic DNA sequence.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework.
- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **HTML/CSS:** For structuring and styling the web pages.

## Installation
1. Create a virtual environment:
    python3 -m venv venv
    source venv/bin/activate

2. Install the required dependencies:
    pip install -r requirements.txt

3. Inititalize the database:
    python
    >>> from app import db
    >>> db.create_all()
    >>> exit()

4. Run the application:
    python run.py

5. Open your browser and navigate to the web application:
    http://127.0.0.1:5000/

