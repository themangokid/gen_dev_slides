import customtkinter as ctk
import re
import os
import subprocess
import shutil

import traceback
traceback.print_exc()

class SlideGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Slide Generator")
        self.geometry("800x600")

        # create widgets
        self.text_entry = ctk.CTkEntry(self, width=50)
        self.generate_button = ctk.CTkButton(self, text="Generate Slides", command=self.generate_slides)
        self.output_label = ctk.CTkLabel(self, text="", font=("Helvetica", 12))

        # create grid layout
        self.text_entry.grid(row=0, column=0, padx=20, pady=20)
        self.generate_button.grid(row=0, column=1, padx=20, pady=20)
        self.output_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    def generate_slides(self):
        text = self.text_entry.get()

        if not text.strip():
            self.output_label.configure(text="Error: No text entered")
            return

        try:
            # Check Marp installation
            if not shutil.which("marp"):
                raise EnvironmentError("Marp CLI is not installed or not in the PATH")
        except Exception as e:
            self.output_label.configure(text=f"Error: {str(e)}")
            return

        try:
            # Step 1: Split sentences
            sentences = split_sentences(text)
        except Exception as e:
            self.output_label.configure(text=f"Error in sentence splitting: {str(e)}")
            return

        try:
            # Step 2: Create slides and lists
            slides = create_slides(sentences, header_level=2)
            lists = create_lists(sentences)
        except Exception as e:
            self.output_label.configure(text=f"Error in slide/list creation: {str(e)}")
            return

        try:
            # Step 3: Add images
            images = add_images("images")
        except Exception as e:
            self.output_label.configure(text=f"Error in adding images: {str(e)}")
            return

        try:
            # Step 4: Write to markdown
            write_to_markdown(slides, lists, images)
        except Exception as e:
            self.output_label.configure(text=f"Error in writing to markdown: {str(e)}")
            return

        try:
            # Step 5: Generate slides with Marp
            marp('output.md')
            self.output_label.configure(text="Slides generated successfully!")
        except Exception as e:
            self.output_label.configure(text=f"Error in generating slides with Marp: {str(e)}")
            return


def split_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences


def create_slides(sentences, header_level=2):
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
    images = []
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist")
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            image = "![{}]({})".format(filename, os.path.join(directory, filename))
            images.append(image)
    return images


def write_to_markdown(slides, lists, images):
    output_file_path = "output.md"
    with open(output_file_path, "w") as f:
        for i in range(max(len(slides), len(lists), len(images))):
            slide = slides[i] if i < len(slides) else ""
            list_ = lists[i] if i < len(lists) else ""
            image = images[i] if i < len(images) else ""
            f.write(slide + "\n")
            f.write(list_ + "\n")
            f.write(image + "\n")


def marp(markdown_file):
    try:
        subprocess.check_call(["marp", "-o", "slides.html", markdown_file])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    app = SlideGeneratorApp()
    app.mainloop()
