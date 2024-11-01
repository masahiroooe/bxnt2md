# boxnote.py
import json
from html import format_list as html_list, format_paragraph as html_paragraph, format_table as html_table, format_link as html_link, format_text as html_text
from markdown import format_list as md_list, format_paragraph as md_paragraph, format_table as md_table, format_link as md_link, format_text as md_text

class BoxNoteParser:
    def __init__(self, output_format):
        self.output_format = output_format

    def parse_json(self, json_string):
        data = json.loads(json_string)
        parsed_content = []

        for item in data.get("content", []):
            item_type = item.get("type")
            if item_type == "text":
                text = item.get("text", "")
                if item.get("marks"):
                    for mark in item["marks"]:
                        if mark.get("type") == "link":
                            href = mark.get("attrs", {}).get("href", "")
                            text = self._format_link(text, href)
                parsed_content.append(self._format_text(text))
            elif item_type == "paragraph":
                parsed_content.append(self._format_paragraph(item.get("content", "")))
            elif item_type in ["check_list", "list"]:
                items = [i.get("value", "") for i in item.get("items", [])]
                parsed_content.append(self._format_list(items, ordered=(item_type == "list")))
            elif item_type == "table":
                headers = item.get("headers", [])
                rows = item.get("rows", [])
                parsed_content.append(self._format_table(headers, rows))

        return parsed_content

    def _format_text(self, text):
        return html_text(text) if self.output_format == "html" else md_text(text)

    def _format_paragraph(self, content):
        return html_paragraph(content) if self.output_format == "html" else md_paragraph(content)

    def _format_list(self, items, ordered=False):
        return html_list(items, ordered) if self.output_format == "html" else md_list(items, ordered)

    def _format_table(self, headers, rows):
        return html_table(headers, rows) if self.output_format == "html" else md_table(headers, rows)

    def _format_link(self, text, href):
        return html_link(text, href) if self.output_format == "html" else md_link(text, href)
