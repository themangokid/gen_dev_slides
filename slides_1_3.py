import re
import os
import pyglet


def split_sentences(text):
    # split the text into sentences using regular expression
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences


def create_slides(sentences, header_level=1):
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


class TextInputWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_input = pyglet.text.Label('Enter text:', font_size=12, x=10, y=self.height - 20)
        self.text = ''

    def on_text(self, text):
        self.text += text

    def on_text_motion(self, motion):
        if motion == pyglet.window.key.MOTION_RETURN:
            sentences = split_sentences(self.text)
            lists = create_lists(sentences)
            images = add_images("images")
            slides = create_slides(sentences, header_level=1)
            write_to_markdown(slides, lists, images)
            pyglet.app.exit()

    
    def on_draw(self):
        self.clear()
        self.text_input.draw()


if __name__ == '__main__':
    window = TextInputWindow(width=400, height=300, resizable=True)
    pyglet.app.run()
