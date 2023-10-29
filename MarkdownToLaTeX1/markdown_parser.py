import utils

def parse_markdown(file_path):
    """
    Function to parse a markdown file and convert it to a dictionary
    :param file_path: str
    :return: dict
    """
    from utils import read_file

    data = read_file(file_path)
    if data is None:
        return None

    parsed_data = {}
    current_key = None

    for line in data.split('\n'):
        if line.startswith('#'):
            current_key = line.strip('# ')
            parsed_data[current_key] = []
        elif current_key is not None:
            parsed_data[current_key].append(line)

    return parsed_data

def markdown_to_latex(parsed_data):
    """
    Function to convert parsed markdown data to LaTeX format
    :param parsed_data: dict
    :return: str
    """
    latex_data = "\\documentclass{book}\n\\begin{document}\n"

    for key, value in parsed_data.items():
        latex_data += "\\chapter{" + key + "}\n"
        for line in value:
            latex_data += line + "\n"
        latex_data += "\n"

    latex_data += "\\end{document}"

    return latex_data
