import re
import os
import random
import subprocess


def marp(file_path):
    command = "marp {}".format(file_path)
    subprocess.run(command, shell=True)


def add_random_theme(file_name):
    themes = ["default", "gaia", "invert", "sky", "ocean", "forest", "sunset", "night", "purple", "red", "yellow",
              "green", "blue"]
    theme = random.choice(themes)
    with open(file_name, "r+") as file:
        content = file.read()
        file.seek(0, 0)
        file.write("---\nmarp: true\ntheme: {}\n---\n{}".format(theme, content))


def split_sentences(text):
    # Split the text into sentences using regular expressions
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences


def create_slides(sentences, header_level=2):
    # Create a slide for each sentence
    slides = []
    slide = ""
    count = 0
    for sentence in sentences:
        if count % 5 == 0 and count != 0:
            slide += "\n"
        header = "#" * header_level + " " + sentence + "\n"
        slide += header
        count += 1
        if count % 5 == 0 or count == len(sentences):
            slides.append(slide)
            slide = ""
    return slides


def create_lists(sentences):
    # Create a list for each set of 5 sentences
    lists = []
    list_items = []
    count = 0
    for sentence in sentences:
        list_items.append("- " + sentence)
        count += 1
        if count % 5 == 0 or count == len(sentences):
            lists.append("\n".join(list_items))
            list_items = []
    return lists


def add_images(directory):
    # Add images to the slides if they exist in the specified directory
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            image = "![{}]({})".format(filename, os.path.join(directory, filename))
            images.append(image)
    return images


def write_to_markdown(slides, lists, images):
    # Write the slides, lists, and images to a markdown file
    output_file_path = "output.md"
    with open(output_file_path, "w") as f:
        for slide, list_, image in zip(slides, lists, images):
            f.write(slide + "\n")
            f.write(list_ + "\n")
            f.write(image + "\n")
    print("Markdown file created successfully!")


# Example text
text = "This is the first sentence. This is the second one. And the third one."

sentences = split_sentences(text)
slides = create_slides(sentences, header_level=2)
lists = create_lists(sentences)
images = add_images("images")
write_to_markdown(slides, lists, images)
add_random_theme("output.md")
marp('output.md')
