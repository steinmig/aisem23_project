import numpy as np

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    """Implement function that extracs similarity value per molecule from raw ChEMBL data
       Computes mean, median and standard deviation 
       
    Hints:
       - Similarity is located in attribute `similarity` of molecule data
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
    similarities = [float(d["similarity"]) for d in raw_data if d["similarity"]]
    return {"component": "Similarity",
            "data": similarities,
            "mean": np.mean(similarities),
            "std": np.std(similarities),
            "min_value": np.min(similarities),
            "max_value": np.max(similarities),
            }
    
def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing histogram of similarities.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. Boxplot.
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of floats

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#C00000",
                                 "line": {"width": 3,
                                          "color": "#9F0202"}}),
            ]
    layout = go.Layout(xaxis={"title": "Similarity, %"},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)
    
    return dcc.Graph(figure=fig)
    