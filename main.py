import os
import sys
from boxnote import BoxNoteParser

def main():
    # 引数をチェック
    if len(sys.argv) < 3:
        print("Usage: main.py <directory_path> <output_format (markdown/html/text)>")
        sys.exit(1)

    directory_path = sys.argv[1]
    output_format = sys.argv[2].lower()

    if output_format not in ['markdown', 'html', 'text']:
        print("Error: Output format must be 'markdown', 'html', or 'text'.")
        sys.exit(1)

    # BoxNote ファイルを探索
    for filename in os.listdir(directory_path):
        if filename.endswith(".boxnote"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # BoxNote ファイルの内容を解析して出力
            parser = BoxNoteParser()
            output_data = parser.parse(content, output_format)

            # 出力ファイル名の設定
            output_filename = os.path.splitext(filename)[0] + {
                'markdown': '.md',
                'html': '.html',
                'text': '.txt'
            }[output_format]

            output_path = os.path.join(directory_path, output_filename)
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(output_data)


if __name__ == "__main__":
    main()

print(f"終わったよ。")
