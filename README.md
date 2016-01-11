artgen.py
==========

Generator of article generators.

## Requirements

- Python 3.x
- Browser supporting JavaScript

## Usage

    usage: artgen.py [-h] [-T TITLE] [-L LANG] [TEMPLATE]

    generate an article generator

    positional arguments:
      TEMPLATE              template filename (default: <_io.TextIOWrapper
                            name='<stdin>' mode='r' encoding='UTF-8'>)

    optional arguments:
      -h, --help            show this help message and exit
      -T TITLE, --title TITLE
                            title (default: Untitled)
      -L LANG, --lang LANG  language (default: en)

## Templates

Making a template is easy.

1.  Type the original article in a text file. If you need to type a brace, i.e.
    `{` or `}`, double it as `{{` or `}}`.
2.  Enclose words with some markups described below.
3.  Run this command to get the HTML file.
4.  Open the HTML file for local use, or upload it to your web space.

### Tags

Tags are specified in this syntax:

-   `{foobar}` renders an `<output>` tag for displaying and an `<input>` tag
    for data, using text before this directive as hint text.
-   `{foobar:hint}` renders the same as the one above, except that `hint` is
    used as hint string.
-   `{=foobar}` renders only `<output>` tag, for strings that should be
    consistent with other parts.

## Examples

- [Haha Generator](https://tagaoyan.github.io/artgen/)
