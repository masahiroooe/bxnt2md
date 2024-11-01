# html.py
def generate_html_header(title):
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
"""

def generate_html_footer():
    return "</body>\n</html>"

def format_list(items, ordered=False):
    tag = 'ol' if ordered else 'ul'
    list_items = "\n".join(f"<li>{item}</li>" for item in items)
    return f"<{tag}>\n{list_items}\n</{tag}>"

def format_paragraph(content):
    return f"<p>{content}</p>"

def format_table(headers, rows):
    header_html = "<tr>" + "".join(f"<th>{header}</th>" for header in headers) + "</tr>"
    rows_html = "\n".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows)
    return f"<table>\n{header_html}\n{rows_html}\n</table>"

def format_text(text):
    return text

def format_link(text, href):
    return f'<a href="{href}">{text}</a>'
