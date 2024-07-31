import pandas as pd
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px


# Data import
df_final2 = pd.read_csv("https://raw.githubusercontent.com/matei4501/Olympics-score-adjusted-for-population/main/draft1_data.csv?token=GHSAT0AAAAAACQOJPNOEJ7756PFOLKNCZBWZVKOKWQ")


# Dash app
app = Dash()

app.layout = [
    html.H1(children='2024 Paris Olympics'),
    dcc.RadioItems(options=['Original Score', 'Per Capita Score', 'Controlling for Population Score'], value='Original Score', id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph')
]

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    map_dict = {'Original Score': 'Score', 'Per Capita Score': 'Score per Capita (adjusted)', 'Controlling for Population Score': 'Lm_Score'}

    df_graph = df_final2.sort_values(map_dict[col_chosen])
    fig = px.bar(df_graph, x='country', y=map_dict[col_chosen], color=df_graph["Region"], category_orders={"Region": ["EUROPE", "NORTHERN AMERICA", "SOUTH AMERICA", "ASIA", "AFRICA", "OCEANIA"]})

    fig.update_layout(title='Olympic Medals Score by Country', xaxis_title='Country', yaxis_title='Score')

    return fig

if __name__ == '__main__':
    app.run(debug=True)
