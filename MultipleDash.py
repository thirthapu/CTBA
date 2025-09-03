from dash import Dash, html, dcc, Input, Output, callback
app = Dash(__name__)

#setting the layout
app.layout = html.Div([
    #these are the three dash core components (dcc)
    dcc.Input(id="input1", type="number", placeholder="Enter a Number"),
    dcc.Input(id="input2", type="number", placeholder="Enter Another Number"),
    dcc.Input(id="input3", type="text", placeholder="Enter text"),
    #i think then these are html components
    html.Div(id="output1"),
    html.Div(id="output2"),
    html.Div(id="output3")
])

@app.callback(
    #output always goes first
    Output("output1", "children"),
    Output("output2", "children"),
    Output("output3", "children"),
    
    Input("input1", "value"),
    Input("input2", "value"),
    Input("input3", "value")
)

def update_outputs(num1, num2, text):
    #handle the none values to avoid errors
    num1 = num1 or 0
    num2 = num2 or 0
    text = text or ""
    
    #perform some operations
    result1 = f"The Sum of the first 2 numbers is: {num1 + num2}"
    result2 = f"The Product of the first 2 numbers is: {num1 * num2}"
    result3 = f"The reversed text of the third cell is: {text[::-1]}"
    
    #return
    return result1, result2, result3

#run the app
if __name__ == "__main__":
    app.run(debug=True)