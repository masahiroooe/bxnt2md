import json
from markdown import MarkdownFormatter
from html import HtmlFormatter

class BoxNoteParser:
    def parse(self, content, output_format):
        try:
            data = json.loads(content)
            formatter = None

            if output_format == 'markdown':
                formatter = MarkdownFormatter()
            elif output_format == 'html':
                formatter = HtmlFormatter()
            else:
                return content  # テキストの場合はそのまま出力

            if 'content' in data.get('doc', {}):
                parsed_output = self._process_content(data['doc']['content'], formatter)
                return parsed_output
            else:
                return "Error: No 'content' found in JSON."
        except json.JSONDecodeError as e:
            return f"Invalid JSON: {e}"

    def _process_content(self, content_list, formatter, indent_level=0):
        output = []
        for item in content_list:
            item_type = item.get("type")

            if item_type == "heading":
                level = item.get("attrs", {}).get("level", 1)
                heading_text = self._extract_text(item.get("content", []))
                output.append(formatter.format_heading(heading_text, level))

            elif item_type == "paragraph":
                paragraph_text = self._extract_text(item.get("content", []))
                output.append(formatter.format_paragraph(paragraph_text))

            elif item_type == "ordered_list":
                output.append(formatter.format_list(item, indent_level))

            elif item_type == "bullet_list":
                output.append(formatter.format_list(item, indent_level))

            elif item_type == "check_list":
                for check_item in item.get("content", []):
                    output.append(self._process_content([check_item], formatter, indent_level))

            elif item_type == "check_list_item":
                is_checked = item.get("attrs", {}).get("checked", False)
                item_text = self._extract_text(item.get("content", []))
                output.append(formatter.format_check_list_item(item_text, is_checked, indent_level))

            elif item_type == "table":
                table_output = formatter.format_table(item)
                output.append(table_output)

            elif item_type == "text":
                text = item.get("text", "")
                if "marks" in item:
                    for mark in item["marks"]:
                        if mark.get("type") == "link":
                            href = mark.get("attrs", {}).get("href", "")
                            text = formatter.format_link(text, href)
                output.append(text)

            # 再帰的にネストされた content を処理
            if "content" in item:
                nested_content = self._process_content(item["content"], formatter, indent_level + 1)
                output.append(nested_content)

        return "\n".join(output)

    def _extract_text(self, content_list):
        text_parts = []
        for content in content_list:
            if content.get("type") == "text":
                text = content.get("text", "")
                text_parts.append(text)
        return "".join(text_parts)
