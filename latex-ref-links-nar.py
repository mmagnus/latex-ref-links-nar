#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Marcin Magnus with ChatGPT"""

import re

def format_note(doi=None, pmid=None, pmcid=None):
    note_parts = []
    if pmid:
        note_parts.append(f"[PubMed:\\href{{https://www.ncbi.nlm.nih.gov/pubmed/{pmid}}}{{{pmid}}}]")
    if pmcid:
        note_parts.append(f"[PubMed Central:\\href{{https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}}}{{{pmcid}}}]")
    if doi:
        note_parts.append(f"[doi:\\href{{https://doi.org/{doi}}}{{{doi}}}]")
    return '\n'.join(note_parts)

def clean_doi(doi):
    return doi.replace("https://doi.org/", "").replace("http://dx.doi.org/", "").strip()

def process_bibtex_entry(entry):
    doi_match = re.search(r"\bdoi\s*=\s*[{\"]([^{}\"]+)[}\"]", entry, re.IGNORECASE)
    pmid_match = re.search(r"\bpmid\s*=\s*[{\"]?(\d+)[}\"]?", entry, re.IGNORECASE)
    pmcid_match = re.search(r"\bpmcid?\s*=\s*[{\"]?(PMC\d+)[}\"]?", entry, re.IGNORECASE)

    doi = clean_doi(doi_match.group(1)) if doi_match else None
    pmid = pmid_match.group(1) if pmid_match else None
    pmcid = pmcid_match.group(1) if pmcid_match else None

    new_note_content = format_note(doi, pmid, pmcid)
    new_note = f"  note = {{{new_note_content}}},"

    # Safely replace or insert the note field using a function as repl
    if re.search(r"\bnote\s*=", entry):
        entry = re.sub(
            r"note\s*=\s*{.*?},?",
            lambda m: new_note,
            entry,
            flags=re.DOTALL
        )
    else:
        entry = re.sub(
            r"(}\s*)$",
            lambda m: f"{new_note}\n{m.group(1)}",
            entry
        )

    return entry

def process_bibtex_file(text):
    entries = re.findall(r"@Article\s*{[^@]+}", text, re.DOTALL | re.IGNORECASE)
    processed = [process_bibtex_entry(entry) for entry in entries]
    return "\n\n".join(processed)

def get_parser():
    import argparse
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="", default="") # nargs='+')
    parser.add_argument("output", help="", default="") # nargs='+')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    # Example usage
    with open(args.input, "r", encoding="utf-8") as f:
        bibtex_text = f.read()

    updated_bibtex = process_bibtex_file(bibtex_text)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(updated_bibtex)

