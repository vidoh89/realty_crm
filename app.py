from shiny import App, ui, module
from modules import lead_management

app_ui = ui.page_fluid(
    ui.h1("Real Estate Management Platform"),


)

def server(input, output, session):
    pass
app = App(app_ui,server)

if __name__ == "__main__":
    app.run()