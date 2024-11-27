# CSS Extractor for HTML Projects

This tool helps you extract only the relevant CSS rules from one or more CSS files based on your HTML files. It
categorizes the rules into:

1. **Definitely Styling Rules**: These are rules directly affecting your HTML elements (e.g., classes like `.btn`).
2. **Possibly Styling Rules**: These are rules that might affect the elements, such as generic tag selectors (e.g.,
   `div`, `button`).

## Problem:

When working with large CSS files, especially those from third-party libraries (like Bootstrap), it's easy to end up
with a lot of unused CSS rules. This leads to a bloated file, slower page loads, and potential conflicts between
multiple CSS sources.

For example, if you only use a button with the class `.btn`, you don’t need the entire Bootstrap CSS file with 10,000+
lines of unused styles. Instead, you only need the rules relevant to that button.

## Solution:

This tool parses your HTML files, extracts the used tags and classes, and then checks your CSS files to find only the
styles that affect those elements. It creates a new, minimal CSS file that only includes the necessary styles.

---

## Features:

- **Extracts relevant CSS**: Only the styles affecting the HTML tags and classes present in your HTML files.
- **Categories styles**: Divides the CSS rules into:
    - **Definitely Styling Rules**: e.g., `.btn`, `.modal-header`
    - **Possibly Styling Rules**: e.g., `div`, `button`
- **Supports multiple HTML and CSS files**: You can pass multiple files for extraction.

---

## Requirements:

- Python 3.6+
- `beautifulsoup4` library for HTML parsing
- `re` module for regular expressions

Install the required library with:

```bash
pip install beautifulsoup4
