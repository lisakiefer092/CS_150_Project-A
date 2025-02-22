import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("annual_aqi_by_county_2024.csv")
df_1 = df[df["State"] == ('California')]
df_2= df_1[["State","County", "Good Days", "Moderate Days","Unhealthy for Sensitive Groups Days","Unhealthy Days","Very Unhealthy Days","Hazardous Days"]]
print (df_2)
colors = {"Good Days": 'green', "Moderate Days":"gold","Unhealthy for Sensitive Groups Days":"orange","Unhealthy Days":"red","Very Unhealthy Days":"darkred","Hazardous Days": "black"}
y_axis_columns = ["Good Days", "Moderate Days","Unhealthy for Sensitive Groups Days","Unhealthy Days","Very Unhealthy Days","Hazardous Days"]


stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    [
        html.Div(
            html.H1(
                "Air Quality Index of the Californian Counties in 2024", style={"textAlign": "center"}
            ),
            className="row",
        ),
        html.Div(dcc.Graph(id="bar-chart", figure={}), className="row"),
        html.Div(
            [
                html.Div(
                    dcc.Dropdown(
                        id="y-axis-dropdown",
                        multi=True,
                        options=[{'label': col, 'value': col} for col in y_axis_columns],
                        value=['Good Days'],
                    ),
                    className="six columns",
                ),
                html.Div(
                    html.A(
                        id="my-link",
                        children="Learn more about the Air Quality Index",
                        href="https://www.airnow.gov/aqi/aqi-basics/",
                        target="_blank",
                    ),
                    className="three columns",
                ),
            ],
            className="row",
        ),
    ]
)
@app.callback(
    Output(component_id="bar-chart", component_property="figure"),
    [Input(component_id="y-axis-dropdown", component_property="value")],
)
def update_chart(selected_y_axis_dropdown):
    fig = px.bar(df_2, x='County', y=selected_y_axis_dropdown,
                     title=f'Bar Plot of Californian Counties vs {selected_y_axis_dropdown}', color_discrete_map=colors)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)

