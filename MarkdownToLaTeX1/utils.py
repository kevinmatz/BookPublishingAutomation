def read_file(file_path):
    """
    Function to read a file
    :param file_path: str
    :return: str
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"{file_path} not found.")
        return None


def write_file(file_path, data):
    """
    Function to write to a file
    :param file_path: str
    :param data: str
    :return: None
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print(f"Error writing to {file_path}: {str(e)}")
