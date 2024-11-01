# markdown.py
class MarkdownFormatter:
    def format_heading(self, text, level):
        return f"{'#' * level} {text}"

    def format_paragraph(self, text):
        return text

    def format_list(self, item, indent_level):
        items = item.get("content", [])
        formatted_items = []
        for i, list_item in enumerate(items, 1):
            prefix = f"{'  ' * indent_level}- " if item["type"] == "bullet_list" else f"{'  ' * indent_level}{i}. "
            formatted_items.append(f"{prefix}{list_item.get('text', '')}")
        return "\n".join(formatted_items)

    def format_check_list_item(self, text, checked, indent_level):
        checkbox = "[x]" if checked else "[ ]"
        return f"{'  ' * indent_level}{checkbox} {text}"

    def format_link(self, text, href):
        return f"[{text}]({href})"

    def format_table(self, item):
        # Implement a markdown-compatible table format
        return "Table format not yet implemented."
