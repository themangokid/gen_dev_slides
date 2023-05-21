import pyglet

window = pyglet.window.Window()

# Create a document to hold the input text
document = pyglet.text.document.FormattedDocument()

# Set the color of the text and the background
document.set_style(0, len(document.text), dict(color=(255, 0, 0, 255), background_color=(0, 255, 0, 255)))

# Create a layout to display the document
layout = pyglet.text.layout.TextLayout(document, width=200, height=200, multiline=False)

@window.event
def on_draw():
    window.clear()
    layout.draw()

# Update the document when the input field is updated
@window.event
def on_text(text):
    document.text = text
    # Set the color of the text and the background
    document.set_style(0, len(document.text), dict(color=(255, 0, 0, 255), background_color=(0, 255, 0, 255)))

# Set the focus to the input field
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        layout.caret.on_mouse_press(x, y, button, modifiers)

pyglet.app.run()
