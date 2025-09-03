from dash import Dash, html


app = Dash(__name__)

app.layout = html.Div([
    html.H1("World Happiness Dashboard"), #makes a header
    html.P("This dashboard visualizes world happiness scores."), #makes a paragraph
    html.Br(), #creates a line break
    html.A("World Happiness Report", href="https://worldhappiness.report/", target="_blank",
           style={"color":"#6065A3", "textDecoration":"underline"}) #this creates a hyperlink
])

if __name__ == "__main__":
    app.run(debug=True)