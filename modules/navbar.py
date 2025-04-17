from shiny import App, ui

def navbar():
    try:
        app_ui = ui.page_navbar(
            ui.nav_panel("Lead Management","Page one content"),
            ui.nav_panel("Property Management","Page two content"),
            ui.nav_panel("Market analysis","Market analysis"),
            title="Realty Express"
        )
        return app_ui
    except Exception as e:
        raise Exception(f"Error loading navigation content: {e}")