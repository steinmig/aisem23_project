import numpy as np

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    """Implement the function that extracts number of aromatic rings per molecule from raw ChEMBL data
       Computes mean, median and standard deviation 
       
    Hints:
       - Number of aromatic rings is located in attribute `aromatic_rings` of `molecule_properties`
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
    aromatic_rings = [int(d["molecule_properties"]["aromatic_rings"]) for d in raw_data if d["molecule_properties"]["aromatic_rings"]]
    return {"component": "Number of aromatic rings",
            "data": aromatic_rings,
            "mean": np.mean(aromatic_rings),
            "std": np.std(aromatic_rings),
            "min_value": np.min(aromatic_rings),
            "max_value": np.max(aromatic_rings),
            }


def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing a histogram of number of aromtic rings.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. Bars or PieChart.
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of ints

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#92d050",
                                 "line": {"width": 3,
                                          "color": "#73A340"}},
                         xbins=dict(start=min(data_array)-1,
                                    end=max(data_array)+1,
                                    size=1),
                         ),
            ]
    layout = go.Layout(xaxis={"title": "Number of aromatic rings",
                              "dtick": 1},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)
    
    return dcc.Graph(figure=fig)
    