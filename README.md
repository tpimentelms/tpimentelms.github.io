# tpimentelms.github.io

Source for my personal academic website — [tpimentelms.github.io](https://tpimentelms.github.io).
It's a [Jekyll](https://jekyllrb.com/) site hosted on GitHub Pages: **push to `master` and it rebuilds and publishes automatically** (no build step to run).

---

## Quick reference — what to edit, and where

| I want to change… | Edit this |
|---|---|
| **Bio / intro** (homepage text) | `_pages/about.md` — the paragraph under the front matter. Job title is the `role:` field in its front matter. |
| **Add / edit a publication** | `markdown_generator/publications.tsv` (one row per paper), then run the generator (below). |
| **Which papers show on the homepage** ("Selected publications") | `_data/featured.yml` — an ordered list; reorder / add / remove lines. |
| **News feed** (homepage) | `_data/news.yml` — add `- date:` / `text:` entries, newest first. |
| **CV** (the page) | `_pages/cv.md`. |
| **CV** (the downloadable PDF) | replace `files/cv.pdf`. |
| **Profile photo** | replace `images/profile2.jpeg` (keep the filename, or update `author.avatar` in `_config.yml`). |
| **Browser tab icon (favicon)** | `images/favicon.svg`. |
| **Name / email / social links** | `_config.yml`, under `author:`. |
| **Colours, fonts, spacing** | `assets/css/redesign.css` (accent colour = the `--accent` variable near the top). |
| **Page structure / nav / footer** | `_layouts/` (see below). |

---

## Editing publications

The publication list is generated from a spreadsheet, so you don't hand-write the pages.

1. Edit **`markdown_generator/publications.tsv`** (tab-separated; one row per paper). Key columns:
   - `pub_date` (`YYYY-MM-DD`, controls ordering), `title`, `authors` (comma-separated; "Tiago Pimentel" is auto-bolded), `venue`, `year`, `paper_url`, `doi`, `pages`, `abstract`.
   - `bibtype` is `inproceedings` (conferences/workshops) or `article` (journals).
   - `highlights` → shows an award **badge**. Recognised phrases: `best paper award`, `outstanding paper award`, `senior area chair highlights`, `spotlight`, `Nominated …`, `Hugging Face …`.
   - **Venue style:** keep the `Full name (ACRONYM)` convention, e.g. `Conference on Empirical Methods in Natural Language Processing (EMNLP)`, `Annual Meeting of the Association for Computational Linguistics (ACL)`, `Transactions of the Association for Computational Linguistics (TACL)`.
2. Regenerate the pages (pure Python, no dependencies — run from the repo root):
   ```bash
   python3 markdown_generator/publications.py
   ```
   This rewrites `_publications/*.md`. **Don't edit those files by hand** — they're overwritten.
3. Commit the changed `publications.tsv` **and** the regenerated `_publications/`.

To feature a paper on the homepage, add its filename stem (the `_publications/` name without `.md`, or just the slug part) to `_data/featured.yml`.

---

## Repository layout

```
_pages/            about.md (homepage), publications.md, cv.md, 404.md
_layouts/          clean.html        – shared shell: <head>, nav, footer, dark-mode toggle
                   home.html         – homepage (hero + news + selected publications)
                   publications-list.html – the full /publications/ page (grouped by year)
                   prose.html        – generic text pages (CV, 404)
                   pub-single.html   – an individual paper page
_includes/         pub-entry.html    – one publication row;  pub-badge.html – the award badge
_data/             news.yml          – homepage news;  featured.yml – selected papers
_publications/     generated pages (from the TSV) — do not edit by hand
markdown_generator/ publications.tsv + publications.py  (the generator)
                    talks.* , PubsFromBib.*             (kept for later — see below)
assets/css/        redesign.css      – all the site's styling
images/            profile2.jpeg (photo), favicon.svg
files/             cv.pdf
papers/            PDFs of selected papers
talkmap/           Leaflet map scaffolding for a future talks page
_config.yml        site config (author links, collections, defaults)
```

Not in git (local/build only): `_site/`, `vendor/`, `.bundle/`, `Gemfile.local`, `Gemfile.lock`, `claude_temp/`.

---

## Running it locally (optional — GitHub Pages builds it for you)

The committed `Gemfile` uses the `github-pages` gem, which pins old gems that **don't run on modern Ruby**. For local preview, use a current Jekyll via a local-only `Gemfile.local` (gitignored):

```ruby
# Gemfile.local
source "https://rubygems.org"
gem "jekyll", "~> 4.3"
gem "webrick", "~> 1.8"
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-gist"
  gem "jekyll-redirect-from"
  gem "jemoji"
end
```

Then (a modern Ruby helps — e.g. `brew install ruby`, then prepend `/opt/homebrew/opt/ruby/bin` to your `PATH`):

```bash
BUNDLE_GEMFILE=Gemfile.local bundle install
BUNDLE_GEMFILE=Gemfile.local bundle exec jekyll serve --livereload
# open http://127.0.0.1:4000
```

---

## Adding a talks or teaching page later

The `talks` and `teaching` collections are declared in `_config.yml` but have no content yet.
To add one, create a `_talks/` (or `_teaching/`) folder with entries plus a matching layout in `_layouts/`
(use `pub-single.html` / `publications-list.html` as a template). `talkmap/` holds a Leaflet map of talk
locations that a talks page can embed.

---

<sub>Originally based on the [academicpages](https://github.com/academicpages/academicpages.github.io) template (a fork of [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/), © Michael Rose, MIT) — since substantially rewritten with a custom layout and stylesheet.</sub>
