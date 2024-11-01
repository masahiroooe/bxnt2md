# main.py
import os
from boxnote import BoxNoteParser
from html import generate_html_header, generate_html_footer

def main(directory, output_format):
    for filename in os.listdir(directory):
        if filename.endswith(".boxnote"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()

            parser = BoxNoteParser(output_format)
            parsed_data = parser.parse_json(content)

            output_filename = filename.replace(".boxnote", f".{output_format}")
            output_path = os.path.join(directory, output_filename)

            with open(output_path, 'w', encoding='utf-8') as output_file:
                if output_format == "html":
                    output_file.write(generate_html_header(filename))
                output_file.write("\n".join(parsed_data))
                if output_format == "html":
                    output_file.write(generate_html_footer())

            print(f"Processed {filename} and saved as {output_filename}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python main.py <directory> <output_format>")
        print("output_format: html, markdown, text")
        sys.exit(1)

    directory = sys.argv[1]
    output_format = sys.argv[2]
    main(directory, output_format)
