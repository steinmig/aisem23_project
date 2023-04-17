import numpy as np

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    """Implement the function that extracts number of H-bond donors per molecule from raw ChEMBL data
       Computes mean, median and standard deviation 
       
    Hints:
       - Number of H-bond donors is located in attribute `hbd` of `molecule_properties`
       - Make sure to exclude None values
       - When input is empty, the method should return an empty dictionary

    Args:
        raw_data (list): ChEMBL output: see callbacks/data_schema.py for description
                         
    Returns:
        dict: the following attributes have to be included in the output
                - data: array of integers, actual values
                - mean: average value of the data
                - std: standard deviation of the data
                - min_value (float): minimum value
                - max_value (float): maximum value
    """
    hb_donor_values = [int(d["molecule_properties"]["hbd"]) for d in raw_data if d["molecule_properties"]["hbd"]]
    return dict(component="Hydrogen Bond Donors",
                data=hb_donor_values,
                mean=np.mean(hb_donor_values),
                std=np.std(hb_donor_values),
                min_value=np.min(hb_donor_values),
                max_value=np.max(hb_donor_values)
                )


def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing a histogram for number of H-bond donors.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. Bars or PieChart.
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of ints

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#0070C0",
                                 "line": {"width": 3,
                                          "color": "#015895"}},
                         xbins=dict(start=min(data_array) - 1,
                                    end=max(data_array) + 1,
                                    size=1),
                         ),
            ]
    layout = go.Layout(xaxis={"title": "H-bond donors",
                              "dtick": 1},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)

    return dcc.Graph(figure=fig)
