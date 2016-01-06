#!/usr/bin/python

from _string import formatter_parser as parse
from hashlib import sha1

def idof(s):
    if s:
        return sha1(s.encode()).hexdigest()[:8]
    return idof('None')

HTML = \
'''
<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
    body {{
        max-width: 960px;
        margin: 1em auto;
    }}
    main {{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }}
    .inputs, .outputs {{
        max-width: 45%;
        min-width: 12em;
        display: inline-block;
        max-height: 23em;
        overflow: auto;
    }}
    .inputs > ul {{
        display: flex;
        flex-direction: column;
    }}
    .inentry {{
        float: right;
        max-width: 100%;
    }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <main>
    <div class="inputs">
    <ul>
    {inputs}
    </ul>
    </div>
    <button onclick="generate()">Generate</button>
    <div class="outputs">
    {outputs}
    </div>
    </main>
    <script>
    var generate = function() {{
        var inputs = document.getElementsByClassName('inentry');
        var dict = {{}};
        for (var i = 0; i < inputs.length; i++) {{
            var item = inputs[i];
            dict[item.name] = item.value;
        }}
        console.log(dict)
        var results = document.getElementsByClassName('outentry');
        for (var i = 0; i < results.length; i++) {{
            var item = results[i];
            console.log(item);
            item.value = dict['i' + item.name.substr(1)] || item.value;
        }}
    }};
    </script>
</body>
</html>
'''

def generate(template, title='UNTITLED', lang='en'):
    inputs = []
    outputs = []
    for item in parse(template):
        pretext, text, hint, *_ = item

        have_input = True
        if not text:
            have_input = False
        if text and text.startswith('='):
            text = text[1:]
            have_input = False

        have_output = True
        if not text:
            have_output = False

        outputs.append(pretext)
        if have_output:
            outputs.append('<output name="o{name}" class="outentry">{value}</output>'.format(
                name=idof(text),
                value=text
                ))

        if have_input:
            inputs.append('<li><label for="i{name}">{context}</label> <input name="i{name}" placeholder="{default}" id="i{name}" class="inentry"></li>'.format(
                name=idof(text),
                default=text,
                context=hint or pretext
                ))

    return HTML.format(title=title,
            lang=lang,
            inputs=''.join(inputs),
            outputs=''.join(outputs)
        )

if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='generate an article generator'
            )
    parser.add_argument('template',
            help='template filename',
            metavar='TEMPLATE',
            nargs='?',
            type=argparse.FileType('r'),
            default=sys.stdin)
    parser.add_argument('-T', '--title', help='title', default='Untitled')
    parser.add_argument('-L', '--lang', help='language', default='en')
    args = parser.parse_args()
    template = args.template.read()
    print(generate(template, args.title, args.lang))
