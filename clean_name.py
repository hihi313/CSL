import argparse
import bibtexparser
import bibtexparser.middlewares as m
import re

# Create a regex pattern to match years from 1600 to 2099
year_ptrn = re.compile(r"\s*\b(1[6-9]\d{2}|20[0-9]{2})\b\s*")
# Create a regex pattern to match abbreviations (3 or more uppercase letters)
abbr_ptrn = re.compile(r"\s*\(\s*\b([A-Z]{3,})\b\s*\)\s*")

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def process_bib_file(filename):
    # Define a middleware for decoding LaTeX
    layers = [
        # m.LatexDecodingMiddleware(),
    ]
    # Parse the .bib file with the middleware
    library = bibtexparser.parse_file(filename, append_middleware=layers)

    # Iterate over each entry in the library
    for entry in library.entries:
        # Check if "volume" is not a number then delete the field
        if "volume" in entry and not is_int(entry["volume"]):
            del entry["volume"]
        # Check for "journaltitle" and "booktitle" keys in the entry
        for k in ("journaltitle", "booktitle", "journal"):
            if k in entry:
                v = entry[k]
                # Search for year and abbreviation in the value
                match = re.search(year_ptrn, v)
                year = match.group(1) if match else None
                match = re.search(abbr_ptrn, v)
                abbr = match.group(1) if match else None

                # Remove the year and abbreviation from the value
                v2 = year_ptrn.sub("", v)
                entry[k] = abbr_ptrn.sub("", v2)
                # print(f"date:  {entry["date"]}")
    return library

if __name__ == "__main__":
    # Define command line arguments
    parser = argparse.ArgumentParser(description="Process a .bib file.")
    parser.add_argument(
        "input_file", type=str, help="The path to the .bib file to process."
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="output.bib",
        help="The name of the output file (default: output.bib).",
    )
    args = parser.parse_args()

    # Process the .bib file and write the output to a new file
    lib = process_bib_file(args.input_file)
    print(f"Entry count: {len(lib.entries)}")
    layers = [
        # m.LatexEncodingMiddleware(),
    ]
    bibtexparser.write_file("output.bib", lib, append_middleware=layers)