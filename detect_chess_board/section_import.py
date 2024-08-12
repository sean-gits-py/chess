# section_import.py
# imports book contents as "sections"
import csv
import pprint

# Function to load puzzle information from csv file
def load_sections(section_file: str = "cm_sections.csv") -> dict:
    """Load section information from csv file into dict."""
    sections = {}
    with open(section_file, 'r') as csvfile:
        fieldnames = ["section_id", "title", "start_page", "end_page", "first_puzzle_id"]
        csvreader = csv.DictReader(csvfile, fieldnames=fieldnames)
        next(csvreader, None)  # skip header
        for row in csvreader:
            sections[int(row['section_id'])] = {
                "title": row['title'],
                "start_page": int(row['start_page']),
                "end_page": int(row['end_page']),
                "first_puzzle_id": int(row['first_puzzle_id']),
            }
    return sections

# PrettyPrinter
pp = pprint.PrettyPrinter(indent=4)

# Load and print sections
sections = load_sections()
pp.pprint(sections)
