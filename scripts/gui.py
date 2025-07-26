from browser import window

qxapi = window.QxApi


def default_caption():
    return 'a Window'


class Window():

    def __init__(self):
        self.caption = default_caption()
        self.width = self.default_width()
        self.height = self.default_height()
        self.widget = qxapi.make_window(self.caption, self.width, self.height)

    def default_caption(self):
        return 'a Window'

    def default_height(self):
        return 275

    def default_width(self):
        return 235

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def hide(self):
        self.widget.hide()

    def set_height(self, height):
        self.height = height
        self.widget.set_height(height)

    def set_width(self, width):
        self.width = width
        self.widget.set_width(width)

    def show(self):
        self.widget.show()
