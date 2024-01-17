import flet as ft

class MainApp():
    def main(self, page: ft.Page):
        self.server_url = ft.TextField(helper_text="Server URL")
        page.add(self.server_url)

        

app = MainApp()
ft.app(target=app.main)