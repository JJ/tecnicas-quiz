import json
import sys

# Read JSON from file or stdin
def read_json(input_file):
    if input_file:
        with open(input_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return json.load(sys.stdin)

def convert_to_markdown(quiz_data):
    markdown = []
    markdown.append("# Preguntas y respuestas Técnicas Artísticas")

    for question in quiz_data:
        # Add question as h1 header
        markdown.append(f"## {question['pregunta']}\n\n")

        # Add answers with their correctness and justification
        for i, answer in enumerate(question['respuesta']):
            prefix = "✓" if answer['correcto'] else "✗"
            markdown.append(f"* {prefix} {answer['texto']}\n")
            markdown.append(f"  * {answer['justificacion']}\n")

        # Add a blank line between questions
        markdown.append("\n")

    return ''.join(markdown)

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Convert JSON quiz data to markdown format')
    parser.add_argument('input_file', nargs='?', help='Input JSON file (optional)')
    parser.add_argument('output_file', nargs='?', help='Output markdown file (optional)')
    args = parser.parse_args()

    # Read JSON data
    quiz_data = read_json(args.input_file)

    # Convert to markdown
    markdown_content = convert_to_markdown(quiz_data)

    # Write to output file or stdout
    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
    else:
        print(markdown_content)

if __name__ == '__main__':
    main()
