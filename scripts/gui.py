from browser import window

qxapi = window.QxApi
get_global = qxapi.get_global
set_global = qxapi.set_global


class TranscriptPanel():

    def __init__(self):
        self.widget = qxapi.make_transcript_panel()


class Window():

    def __init__(self):
        self.widget = qxapi.make_window()
        self.caption = self.default_caption()
        self.width = self.default_width()
        self.height = self.default_height()
        self.set_caption(self.caption)
        self.set_width(self.width)
        self.set_height(self.height)

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

    def set_caption(self, caption):
        self.caption = caption
        self.widget.setCaption(caption)

    def set_height(self, height):
        self.height = height
        self.widget.setHeight(height)

    def set_width(self, width):
        self.width = width
        self.widget.setWidth(width)

    def show(self):
        self.widget.show()


class ChatConsole(Window):

    def __init__(self):
        super().__init__()
        self.transcript = TranscriptPanel()
        self.widget.add(self.transcript.widget, {'edge': 'center'})

    def default_caption(self):
        return 'Chat Console'
