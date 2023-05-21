import re
import os
import random
import subprocess


def marp(file):
    command = "marp {}".format(file)
    start_page = subprocess.run(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def add_random_theme(file_name):
    themes = ["default", "gaia", "invert", "sky", "ocean", "forest", "sunset", "night", "purple", "red", "yellow",
              "green", "blue"]
    theme = random.choice(themes)
    with open(file_name, "r+") as file:
        content = file.read()
        file.seek(0, 0)
        file.write("---\nmarp: true\ntheme: " + theme + "\n---\n" + content)


# Call the function to add a random theme to the markdown file


def split_sentences(text):
    # split the text into sentences using regular expression
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences


def create_slides(sentences, header_level=2):
    # create a slide for each sentence
    slides = []
    slide = ""
    count = 0
    for sentence in sentences:
        if count % 5 == 0 and count != 0:
            slide += "\n"
        header = header_level * "#" + " " + sentence + "\n"
        slide += header
        count += 1
        if count % 5 == 0 or count == len(sentences):
            slides.append(slide)
            slide = ""
    return slides


def create_lists(sentences):
    # create a list for each set of 5 sentences
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
    # add images to the slides if they exist in the specified directory
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            image = "![{}]({})".format(filename, os.path.join(directory, filename))
            images.append(image)
    return images


def write_to_markdown(slides, lists, images):
    # write the slides, lists, and images to a markdown file
    with open("backup_output/output.md", "w") as f:
        for slide, list_, image in zip(slides, lists, images):
            f.write(slide + "\n")
            f.write(list_ + "\n")
            f.write(image + "\n")
    print("Markdown file created successfully!")


# example text
text = "This is the first sentence. This is the second one. And the third one."

sentences = split_sentences(text)
slides = create_slides(sentences, header_level=2)
lists = create_lists(sentences)
images = add_images("images")
write_to_markdown(slides, lists, images)
add_random_theme("output.md")
marp('output.md')

