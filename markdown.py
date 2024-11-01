# markdown.py
def format_list(items, ordered=False):
    return "\n".join(f"{idx + 1}. {item}" if ordered else f"- {item}" for idx, item in enumerate(items))

def format_paragraph(content):
    return content

def format_table(headers, rows):
    header_row = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join("---" for _ in headers) + " |"
    rows_data = "\n".join("| " + " | ".join(row) + " |" for row in rows)
    return f"{header_row}\n{separator}\n{rows_data}"

def format_text(text):
    return text

def format_link(text, href):
    return f'[{text}]({href})'
