
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

publications = pd.read_csv("markdown_generator/publications.tsv", sep="\t", header=0, keep_default_na=False)
publications


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


def get_bibtext(item):
    authors = item.authors.replace(',', ' and\n       ')
    bibtex = f"""
@{item.bibtype}{{{item.bibid},
    author = {{
        {authors}
    }},"""

    if item.bibtype == 'article':
        bibtex += f"""
    article = {{{item.venue}}},"""
    elif item.bibtype == 'inproceedings':
        bibtex += f"""
    booktitle = {{{item.venue}}},"""
    else:
        raise ValueError(f'Error. Unknown bibtype {item.bibtype}')

    bibtex += f"""
    title = {{{item.title}}},
    year = {{{item.year}}},"""

    if item.volume and len(str(item.volume)) > 1:
        bibtex += f"""
    volume = {{{item.volume}}},"""

    # print(item.number is float('nan'))
    # import ipdb; ipdb.set_trace()
    if item.number and len(str(item.number)) > 1:
        bibtex += f"""
    number = {{{item.number}}},"""

    if item.doi and len(str(item.doi)) > 3:
        bibtex += f"""
    doi = {{{item.doi}}},"""

    if item.paper_url and len(str(item.paper_url)) > 3:
        bibtex += f"""
    url = {{{item.paper_url}}},"""

    bibtex += f"""
    pages = {{{item.pages}}},
}}"""

    return bibtex
# "@INPROCEEDINGS{husain2013mapping,
#   author={
#     Ammar Husain and
#     Heather Jones and
#     Balajee Kannan and
#     Uland Wong and
#     Tiago Pimentel and
#     Sarah Tang and
#     Shreyansh Daftry and
#     Steven Huber and
#     William L. Whittaker
#   },
#   booktitle={2013 IEEE Aerospace Conference},
#   title={Mapping planetary caves with an autonomous, heterogeneous robot team},
#   year={2013},
#   volume={},
#   number={},
#   pages={1-13},
# }"

# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

import os
for row, item in publications.iterrows():
    
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += """collection: publications"""
    
    md += "\nauthors: \""   + item.authors.replace('Tiago Pimentel', '<b>Tiago Pimentel</b>') + '"'

    md += """\npermalink: /publication/""" + html_filename
    
    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"
    
    md += "\ndate: " + str(item.pub_date) 
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"
    
    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + item.paper_url + "'"
    
    md += "\ncitation: '" + html_escape(item.citation) + "'"

    if len(str(item.highlights)) > 5:
        highlights = item.highlights
        highlights = highlights.replace('outstanding paper award', '<b>outstanding paper award</b>')
        highlights = highlights.replace('best paper award', '<b>best paper award</b>')
        md += "\nhighlights: '" + html_escape(highlights) + "'"
    
    md += "\n---"
    
    ## Markdown description for individual page

    if len(str(item.paper_url)) > 5:
        md += "\n\n<a href='" + item.paper_url + "'>Find paper here</a>\n" 

    md += "\n" + html_escape(item.abstract) + "\n"

    md += "\n```" + get_bibtext(item) + "\n```"
    
    md_filename = os.path.basename(md_filename)
       
    with open("_publications/" + md_filename, 'w') as f:
        f.write(md)


