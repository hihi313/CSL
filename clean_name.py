import argparse
import bibtexparser
import bibtexparser.middlewares as m
import re

# Create a regex pattern to match years from 1600 to 2099
year_ptrn = re.compile(r"\s*\b(1[6-9]\d{2}|20[0-9]{2})\b\s*")
abbr_ptrn = re.compile(r"\s*\(\s*\b([A-Z]{3,})\b\s*\)\s*")


def process_bib_file(filename):
    layers = [
        m.LatexDecodingMiddleware(),
    ]
    library = bibtexparser.parse_file(filename, append_middleware=layers)

    for entry in library.entries:
        for k in ("journaltitle", "booktitle"):
            if k in entry:
                v = entry[k]
                match = re.search(year_ptrn, v)
                year = match.group(1) if match else None
                match = re.search(abbr_ptrn, v)
                abbr = match.group(1) if match else None

                v2 = year_ptrn.sub("", v)
                entry[k] = abbr_ptrn.sub("", v2)
    return library


if __name__ == "__main__":

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

    lib = process_bib_file(args.input_file)
    bibtexparser.write_file("output.bib", lib)
