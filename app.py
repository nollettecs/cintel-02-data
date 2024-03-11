import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

# Built-in function to load the penguin dataset
penguins_df = palmerpenguins.load_penguins()

# Title for chart
ui.page_opts(title="Nollettecs Penguins", fillable=True)

with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
