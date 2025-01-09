from dash import Dash, html
import dash_bootstrap_components as dbc

dash_app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Simple HTML

# dash_app.layout = [html.H1(children='Hello World')]
# dash_app.layout.append(html.Textarea(children='Input text'))

# DDK
dash_app.layout = [
    dbc.Container([
        html.Header([
            html.Title(children='My App')
        ]),
        html.H1(children="Test"),
        html.Div([
            dbc.Input(type="email", id="example-email", placeholder="Enter email"),
            dbc.Input(type='password', placeholder='password'),
            dbc.Textarea(placeholder='Input text')
        ])
    ])
]

if __name__ == '__main__':
    dash_app.run(debug=True)