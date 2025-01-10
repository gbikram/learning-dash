from dash import Dash, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from ioc_finder import find_iocs
import jmespath
import pandas as pd

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
            # dbc.Input(type="email", id="example-email", placeholder="Enter email"),
            # dbc.Input(type='password', placeholder='password'),
            dbc.Textarea(id='freetext_input', placeholder='Input text', value="")
        ]),
        dbc.Button('Submit', id='submit_button', n_clicks=0),
        html.Div([
            # dbc.Textarea(id='parsed_output'),
            dbc.Table(id='table-output')
        ])
    ])
]

@callback(
    Output(component_id='table-output', component_property='children'),
    Input(component_id='submit_button', component_property='n_clicks'),
    State(component_id='freetext_input', component_property='value')
)
def run_parser(n_clicks, value):
    if n_clicks > 0:
        iocs_df = extract_iocs(value)
        table = dbc.Table.from_dataframe(iocs_df, striped=True, bordered=True, hover=True)
        return table
    # if n_clicks > 0:
    #     return f'You entered {value} and clicked {n_clicks} times'


def extract_iocs(freetext):
    iocs = find_iocs(freetext)
    transform_schema = """
    {
        domains: domains,
        urls: urls
    }
    """
    iocs = jmespath.search(f"{transform_schema}", iocs)
    iocs_transformed = []
    for ioc_type in iocs:
        for ioc in iocs[ioc_type]:
            iocs_transformed.append({
                'ioc_type': ioc_type,
                'ioc_value': ioc
            })    
    ioc_df = pd.DataFrame(iocs_transformed)
    print(ioc_df)
    return ioc_df


if __name__ == '__main__':
    dash_app.run(debug=True)