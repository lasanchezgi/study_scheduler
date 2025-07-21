import webbrowser

class BrowserOpener:
    def open_url(self, url: str):
        webbrowser.open(url, new=2)  # new=2 => abre en nueva pestaña del navegador predeterminado
