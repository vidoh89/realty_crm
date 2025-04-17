from shiny import ui, module, render
import pandas as pd

@module.ui

def lead_management_ui(id:str):
    ns= ui.NS(id)
    return ui.panel_fluid(
        ui.h2("Lead Management"),
        ui.output_text(ns("placeholder"))
    )

@module.server
def lead_management_server(id:str):
    @render.text
    def placeholder():
        return "Lead management module is running"