import os
# import openai
import mammoth
import textwrap
import pandoc
import argparse

parser = argparse.ArgumentParser(description="Program to proofread a Microsoft Word file using an OpenAI LLM",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source file, a Microsoft Word document")
parser.add_argument("dest", help="Destination file, a Microsoft Word document")

args = parser.parse_args()
config = vars(args)
# print("Config:")
# print(config)

source_filename = config["src"]
destination_filename = config["dest"]

# Set the OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")
api_key = os.getenv("OPENAI_API_KEY")

print("source_filename: " + source_filename)
print("destination_filename: " + destination_filename)
# print("OPENAI_API_KEY: " + api_key)

# Convert Word to Markdown
with open(source_filename, "rb") as docx_file:
    result = mammoth.convert_to_markdown(docx_file)
    md_text = result.value

# Break the markdown text into segments
segments = textwrap.wrap(md_text, 2048)

# Proofread each segment
segments_count = 0
proofread_segments = []
prompt_format = "Please perform copy editing on this Markdown text to correct spelling, grammar, usage, and punctuation mistakes, and to ensure consistent usage:\n {}"

for segment in segments:
    segments_count = segments_count + 1

    print("Segment {x}:".format(x=segments_count))
    print("-----")
    print(segment)
    print("-----")

    """
        prompt = prompt_format.format(segment)
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=2100
        )
        # Save the corrected text
        proofread_segments.append(response.choices[0].text.strip())
    """

    # For now, until we can get openai package working, just keep the segment unchanged
    proofread_segments.append(segment)

# print("segments_count: ", segments_count)

# Reassemble the proofread markdown
proofread_md = ''.join(proofread_segments)

# Write the proofread markdown to a file
# TODO: How to generate a temp filename properly in Python? And can it be auto-deleted at program termination like in Java?
with open('temp_proofread.md', 'w', encoding='utf-8') as file:
    file.write(proofread_md)

# using pandoc to convert the markdown back to word document.
os.system("pandoc -s temp_proofread.md -o {destination_filename}".
          format(destination_filename=destination_filename))

print("Proofreading is complete. The proofread document is: {destination_filename}".
          format(destination_filename=destination_filename))

# TODO: Delete the temp_proofread.md file
