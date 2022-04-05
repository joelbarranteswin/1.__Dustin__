# import pip
# pip.main(["install", 'panel'])

import panel as pn

slider = pn.widgets.IntSlider(start=0, end=10)

def slideshow(index):
    url = f"https://picsum.photos/800/300?image={index}"
    return pn.pane.JPG(url)

output = pn.bind(slideshow, slider)

app = pn.Column(slider, output)
app