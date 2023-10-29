from markdown_parser import parse_markdown, markdown_to_latex
import utils

def generate_latex_from_markdown(markdown_file_path, latex_file_path):
    """
    Function to generate a LaTeX file from a Markdown file
    :param markdown_file_path: str
    :param latex_file_path: str
    :return: None
    """
    # Parse the markdown file
    parsed_data = parse_markdown(markdown_file_path)
    if parsed_data is None:
        print(f"Error parsing {markdown_file_path}")
        return

    # Convert the parsed data to LaTeX format
    latex_data = markdown_to_latex(parsed_data)

    # Write the LaTeX data to a file
    utils.write_file(latex_file_path, latex_data)
