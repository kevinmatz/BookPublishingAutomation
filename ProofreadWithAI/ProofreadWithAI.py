import os
# import openai
# import pandoc  -- the code is currently using a os.system() call that uses the "pandoc" command instead
import mammoth
import textwrap
import argparse
import requests

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

# Break the markdown text into paragraphs
paragraphs = md_text.split('\n\n')

# Proofread each paragraph
segments_count = 0
proofread_segments = []
prompt_format = "Please perform copy editing on this Markdown text to correct spelling, grammar, usage, and punctuation mistakes, and to ensure consistent usage:\n {}"

for paragraph in paragraphs:
    # Break the paragraph into segments
    segments = textwrap.wrap(paragraph, 2048)
    for segment in segments:
        segments_count = segments_count + 1

        print("Segment {x}:".format(x=segments_count))
        print("-----")
        print(segment)
        print("-----")

        # prompt = prompt_format.format(segment)

        """
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=2100
        )
        """

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }

        """
        data = {
            # "engine": "text-davinci-003",
            "model": "gpt-3.5-turbo",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 2100
        }
        """

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful proofreader who performs copy editing on text to correct spelling, grammar, usage, and punctuation mistakes, and to ensure consistent usage. Please never respond with instructions or comments on how to fix the problems in the text, but rather, please always respond with the corrected text itself, and if you cannot proofread the text for any reason, please return the input text unchanged. Text will be provided with Markdown formatting; please retain the formatting."},
                # {"role": "user", "content": "Who won the world series in 2020?"},
                # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                # {"role": "user", "content": "Where was it played?"}
                {"role": "user", "content" : f'Please proofread this text: "{segment}"'}
            ]
        }

        print("----- headers:")
        print(headers)
        print("----- data:")
        print(data)
        print("-----")
        
        try:
            # response = requests.post('https://api.openai.com/v1/engines/davinci/completions', headers=headers, json=data)
            response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
            response.raise_for_status()  # This will raise a HTTPError if the response was unsuccessful
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")
            print(f"Response content: {response.content}")
            exit(1)
        else:
            print("HTTP POST request submitted successfully; no error response")

        x = {'id': 'chatcmpl-8KLUIWvHe7eJIgJ1Ywc3H8k7HnQtj', 'object': 'chat.completion', 'created': 1699859850, 'model': 'gpt-3.5-turbo-0613', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': '"Organizational Culture as a Strategic Competitive Advantage for New Enterprises"\n\nTitle formatting: The title should be capitalized using title case.\n\n'}, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 76, 'completion_tokens': 25, 'total_tokens': 101}}


        print("Response:")
        print("-----")
        print(response)
        print("----- JSON: -----")
        print(response.json())
        print("-----")
        
        # Save the corrected text
        chat_response = response.json()['choices'][0]['message']['content'].strip();
        proofread_segments.append(chat_response)

        print("Proofread results:")
        print("-----")
        print(proofread_segments[-1])
        print("-----")

        # Save the corrected text
        # proofread_segments.append(response.choices[0].text.strip())

        # For now, until we can get openai package working, just keep the segment unchanged
        # proofread_segments.append(segment)
    
    # proofread_segments.append("\n\n")

# Reassemble the proofread markdown
proofread_md = '\n\n'.join(proofread_segments)

# print("segments_count: ", segments_count)

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
