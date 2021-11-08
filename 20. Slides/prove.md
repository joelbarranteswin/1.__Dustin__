# Darkslide

---

# Overview

Generate HTML5 slideshows from markdown, ReST, or textile.

![python](http://i.imgur.com/bc2xk.png)

Darkslide is primarily written in Python, but it's themes use:

- HTML5
- Javascript
- CSS

---

# Code Sample

Darkslide supports code snippets

    !python
    def log(self, message, level='notice'):
        if self.logger and not callable(self.logger):
            raise ValueError(u"Invalid logger set, must be a callable")

        if self.verbose and self.logger:
            self.logger(message, level)

---

# Code Sample
    !python
    import pandas as pd
    a = 3
    b = 6
    c = a + b
    print(este es el numero,c)