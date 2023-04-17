import numpy as np

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    """Implement the function that extracts polar surface area per molecule from raw ChEMBL data
       Computes mean, median and standard deviation 
       
    Hints:
       - Polar surface area is located in attribute `psa` of `molecule_properties`
       - Make sure to exclude None values
       - When input is empty, the method should return an empty dictionary

    Args:
        raw_data (list): ChEMBL output: see callbacks/data_schema.py for description

    Returns:
        dict: the following attributes have to be included in the output
                - component (str): name of the component
                - data (list): array of integers, actual values
                - mean (float): average value
                - std (float): standard deviation
                - min_value (float): minimum value
                - max_value (float): maximum value
    """
    psa = [comp_obj["molecule_properties"]["psa"]
           for comp_obj in raw_data
           if comp_obj["molecule_properties"]["psa"]]
    return {"component": "Polar surface area",
            "data": psa,
            "mean": np.mean(psa),
            "std": np.std(psa),
            "min_value": np.min(psa),
            "max_value": np.max(psa)}


def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing a histogram for polar surface area.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. BoxPlot.
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of floats

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#7030A0",
                                 "line": {"width": 3,
                                          "color": "#57257D"}}
                         ),
            ]
    layout = go.Layout(xaxis={"title": "Polar surface area, &#197;<sup>2</sup>"},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)

    return dcc.Graph(figure=fig)
