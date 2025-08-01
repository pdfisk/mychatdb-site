from browser import window

qxapi = window.QxApi
get_global = qxapi.get_global
set_global = qxapi.set_global


class SplitPanel():

    def __init__(self):
        self.widget = qxapi.make_split_panel()


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
        return 375

    def default_width(self):
        return 425

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


class SplitWindow(Window):

    def __init__(self):
        super().__init__()
        self.left_panel = TranscriptPanel()
        self.right_panel = TranscriptPanel()
        self.split_panel = SplitPanel()
        self.split_panel.widget.add(self.left_panel.widget)
        self.split_panel.widget.add(self.right_panel.widget)
        self.widget.add(self.split_panel.widget, {'edge': 'center'})


class TextWindow(Window):

    def __init__(self):
        super().__init__()
        self.text_panel = TranscriptPanel()
        self.widget.add(self.text_panel.widget, {'edge': 'center'})


class ChatConsole(SplitWindow):

    def __init__(self):
        super().__init__()
        self.send_btn = qxapi.make_button('Send')
        self.clear_in_btn = qxapi.make_button('Clear In')
        self.clear_out_btn = qxapi.make_button('Clear Out')
        qxapi.add_click_handler(self.send_btn, self.on_send)
        qxapi.add_click_handler(self.clear_in_btn, self.on_clear_in)
        qxapi.add_click_handler(self.clear_out_btn, self.on_clear_out)
        self.widget.getButtonBar().add(self.send_btn)
        self.widget.getButtonBar().add(self.clear_out_btn)
        self.widget.getButtonBar().add(self.clear_in_btn)

    def default_caption(self):
        return 'Chat Console'

    def get_left_value(self):
        return self.left_panel.widget.getValue()

    def get_right_value(self):
        return self.left_panel.widget.getValue()

    def on_clear_in(self):
        self.set_left_value('')

    def on_clear_out(self):
        self.set_right_value('')

    def on_send(self):
        code = self.get_left_value()
        self.set_right_value(code)

    def set_left_value(self, value):
        self.left_panel.widget.setValue(value)

    def set_right_value(self, value):
        self.right_panel.widget.setValue(value)
