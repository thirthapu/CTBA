#import my dash library
from dash import Dash,html

#create my dash app
app = Dash(__name__)
app.title = "My First Dash App"

#define the layout
app.layout = html.Div([ #Div is a container that holds text
    html.H1 ("Hello Dash", style = {"color": "#381D5C",
                                    "fontSize": "20px",
                                    "backgroundColor": "#E89AAA"}),
    html.P("This is a simple dashboard", style = {"border": "1px solid black",
                                                  "padding": "20px",
                                                  "margin": "50px"}),
    html.Br(), #this is a line break
    html.A("Click Here", href = "https://example.com") #this makes a clickable link
    ])

#run the app
if __name__ == "__main__":
    app.run(debug = True, use_reloader = False) #by default reloader is true, it just means you don't have to reload everytime to see changes when it is True
    