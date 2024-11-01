# html.py
class HtmlFormatter:
    def format_heading(self, text, level):
        return f"<h{level}>{text}</h{level}>"

    def format_paragraph(self, text):
        return f"<p>{text}</p>"

    def format_list(self, item, indent_level):
        tag = "ul" if item["type"] == "bullet_list" else "ol"
        items = item.get("content", [])
        formatted_items = [f"<li>{list_item.get('text', '')}</li>" for list_item in items]
        return f"{'  ' * indent_level}<{tag}>\n" + "\n".join(formatted_items) + f"\n{'  ' * indent_level}</{tag}>"

    def format_check_list_item(self, text, checked, indent_level):
        checkbox = '<input type="checkbox" checked>' if checked else '<input type="checkbox">'
        return f"{'  ' * indent_level}<li>{checkbox} {text}</li>"

    def format_link(self, text, href):
        return f'<a href="{href}">{text}</a>'

    def format_table(self, item):
        # Implement an HTML-compatible table format
        return "Table format not yet implemented."
