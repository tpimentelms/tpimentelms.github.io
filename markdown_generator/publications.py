#!/usr/bin/env python3
"""Generate the publication pages from the publications.tsv spreadsheet.

Usage (run from the repository root):

    python3 markdown_generator/publications.py

Reads `markdown_generator/publications.tsv` and writes one Markdown file per
row into `_publications/`. Pure standard library — no pandas / no pip installs.

Columns expected in the TSV (tab-separated, with a header row):
    pub_date title authors venue excerpt citation url_slug paper_url
    abstract bibtex bibtype bibid year pages doi volume number highlights

Edit the TSV, then re-run this script and commit the regenerated _publications/.
"""
import csv
import os

TSV = "markdown_generator/publications.tsv"
OUT = "_publications"

html_escape_table = {"&": "&amp;", '"': "&quot;", "'": "&apos;"}


def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in str(text))


def get_bibtex(item):
    authors = item["authors"].replace("*", "").replace(",", " and\n       ")
    bib = f"\n@{item['bibtype']}{{{item['bibid']},\n    author = {{\n        {authors}\n    }},"
    if item["bibtype"] == "article":
        bib += f"\n    article = {{{item['venue']}}},"
    elif item["bibtype"] == "inproceedings":
        bib += f"\n    booktitle = {{{item['venue']}}},"
    else:
        raise ValueError(f"Unknown bibtype {item['bibtype']!r} for {item['bibid']!r}")
    bib += f"\n    title = {{{item['title']}}},\n    year = {{{item['year']}}},"
    if len(str(item["volume"])) > 1:
        bib += f"\n    volume = {{{item['volume']}}},"
    if len(str(item["number"])) > 1:
        bib += f"\n    number = {{{item['number']}}},"
    if len(str(item["doi"])) > 3:
        bib += f"\n    doi = {{{item['doi']}}},"
    if len(str(item["paper_url"])) > 3:
        bib += f"\n    url = {{{item['paper_url']}}},"
    bib += f"\n    pages = {{{item['pages']}}},\n}}"
    return bib


def main():
    with open(TSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    os.makedirs(OUT, exist_ok=True)
    written = []
    for item in rows:
        slug = f"{item['pub_date']}-{item['url_slug']}"
        md = '---\ntitle: "' + item["title"] + '"\ncollection: publications'
        md += '\nauthors: "' + item["authors"].replace("Tiago Pimentel", "<b>Tiago Pimentel</b>") + '"'
        md += "\npermalink: /publication/" + slug
        if len(str(item["excerpt"])) > 5:
            md += "\nexcerpt: '" + html_escape(item["excerpt"]) + "'"
        md += "\ndate: " + str(item["pub_date"])
        md += "\nvenue: '" + html_escape(item["venue"]) + "'"
        if len(str(item["paper_url"])) > 5:
            md += "\npaperurl: '" + item["paper_url"] + "'"
        md += "\ncitation: '" + html_escape(item["citation"]) + "'"
        if len(str(item["highlights"])) > 5:
            hl = item["highlights"].replace("outstanding paper award", "<b>outstanding paper award</b>")
            hl = hl.replace("best paper award", "<b>best paper award</b>")
            md += "\nhighlights: '" + html_escape(hl) + "'"
        md += "\n---"
        if len(str(item["paper_url"])) > 5:
            md += "\n\n<a href='" + item["paper_url"] + "'>Find paper here</a>\n"
        md += "\n" + html_escape(item["abstract"]) + "\n\n```" + get_bibtex(item) + "\n```"

        with open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8") as f:
            f.write(md)
        written.append(slug)

    print(f"Wrote {len(written)} publication pages to {OUT}/")


if __name__ == "__main__":
    main()
