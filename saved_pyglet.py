import pyglet
from pyglet.window import Window
from pyglet.text import Label, FormattedDocument


# Create the window
window = Window()

# Create labels to display the maximum score and grade E inputs
max_score_label = Label(text='Enter the maximum score: ', x=10, y=window.height - 30)
grade_e_label = Label(text="Enter the value for grade 'E': ", x=10, y=window.height - 60)

# Create text input fields to allow the user to enter the maximum score and grade E
max_score_input = FormattedDocument(x=200, y=window.height - 30, width=200, multiline=False)
grade_e_input = FormattedDocument(x=200, y=window.height - 60, width=200, multiline=False)

# Create a label to display the grade boundaries
grade_boundaries_label = Label(text='', x=10, y=window.height - 90)

# Function to calculate and display the grade boundaries
def calculate_grade_boundaries():
    # Get the maximum score and grade E inputs from the text input fields
    max_score = max_score_input.text
    grade_e = grade_e_input.text

    # Validate the input values
    try:
        max_score = int(max_score)
    except:
        max_score_input.text = 'Invalid value'
        return
    try:
        grade_e = int(grade_e)
    except:
        grade_e_input.text = 'Invalid value'
        return

    # Calculate the grade boundaries
    interval = max_score - grade_e
    grade_interval = interval / 5

    # Build the string to display the grade boundaries
    grade_boundaries_str = '(F < {})'.format(grade_e)
    for i in range(0, 5):
        grade_e += grade_interval
        grade_boundaries_str += '\n{} {}'.format(grades[i], round(grade_e))

    # Display the grade boundaries
    grade_boundaries_label.text = grade_boundaries_str

# Create a button to calculate and display the grade boundaries
calculate_button = pyglet.text.Button(text='Calculate', x=10, y=10, width=80, height=30)

# Set the on_click event for the button to call the calculate_grade_boundaries function
@calculate_button.event
def on_click(button):
    calculate_grade_boundaries()

# Function to copy the grade boundaries to the clipboard
def copy_to_clipboard():
    pyglet.clipboard.set(grade_boundaries_label.text)

# Create a button to copy the grade boundaries to the clipboard
copy_button = pyglet.text.Button(text='Copy to clipboard', x=100, y=10, width=120, height=30)

# Set the on_click event for the button to
# Set the on_click event for the button to call the copy_to_clipboard function
@copy_button.event
def on_click(button):
    copy_to_clipboard()

# Function to draw the labels, text input fields, and buttons
@window.event
def on_draw():
    window.clear()
    max_score_label.draw()
    grade_e_label.draw()
    max_score_input.draw()
    grade_e_input.draw()
    grade_boundaries_label.draw()
    calculate_button.draw()
    copy_button.draw()

# Run the pyglet window
pyglet.app.run()