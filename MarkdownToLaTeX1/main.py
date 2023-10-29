import argparse
from latex_generator import generate_latex_from_markdown

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Convert a Markdown file to a LaTeX file formatted as a book.')
    parser.add_argument('markdown_file', type=str, help='The path to the Markdown file to convert.')
    parser.add_argument('latex_file', type=str, help='The path to the LaTeX file to output.')

    # Parse the arguments
    args = parser.parse_args()

    # Generate the LaTeX file from the Markdown file
    generate_latex_from_markdown(args.markdown_file, args.latex_file)

if __name__ == '__main__':
    main()
