from shiny import App, ui, module
from modules import lead_management
from modules.navbar import navbar


app_ui = navbar()

def server(input, output, session):
    pass
app = App(app_ui,server)

if __name__ == "__main__":
    app.run()