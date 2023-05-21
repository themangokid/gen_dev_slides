import re

def split_from_num(string, num):
    return string[num:]


def split_sentences(text):
    # split the text into sentences using regular expression
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|,)\s', text)
    sentences = [sentence.strip(',.?!') for sentence in sentences]
    return sentences

def create_slides(sentences, header_level=1):
    # create a slide for each sentence
    slides = []
    slide = ""
    count = 0
    cut_off_num = 20
    for sentence in sentences:
        if len(sentences) < cut_off_num:
            split_from_num(sentences, cut_off_num)
        if count % 5 == 0 and count != 0:
            slide += "\n---\n"
        header = header_level * "+" + " " + sentence + "\n"
        slide += header
        count += 1
        if count % 5 == 0 or count == len(sentences):
            slides.append(slide)
            slide = ""
    return slides

def write_to_markdown(slides):
    # write the slides to a markdown file
    with open("backup_output/output.md", "w") as f:
        for slide in slides:
            f.write(slide + "\n")
    print("Markdown file created successfully!")

# example text
text = "I alla programmeringsspråk så är selektioner ett centralt begrepp. Selektioner eller villkorssatser brukar vi kalla det på svenska, Control Structures heter det på engelska. Oavsett vad det kallas så handlar det om val och att tala om för programmet att göra olika saker beroende på ett specifikt villkor. I detta moment kommer vi lära oss att förstå strukturen kring villkorssatser men också lära oss att skriva de villkor som styr dem."

sentences = split_sentences(text)
slides = create_slides(sentences, header_level=1)
write_to_markdown(slides)
