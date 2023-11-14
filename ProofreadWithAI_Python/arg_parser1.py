import argparse

parser = argparse.ArgumentParser(description="Example program",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source file, a Microsoft Word document")
parser.add_argument("dest", help="Destination file, a Microsoft Word document")

args = parser.parse_args()
config = vars(args)
print("Config:")
print(config)
