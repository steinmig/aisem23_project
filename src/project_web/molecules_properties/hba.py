import numpy as np

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    """Implement the function that extracts number of H-bonds acceptors per molecule from raw ChEMBL data
       Computes mean, median and standard deviation, max/min values, quartiles and interquartile range
       
    Hints:
       - Number of H-bond acceptors is located in attribute `hba` of `molecule_properties`
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
    hbacceptor_values = [int(d["molecule_properties"]["hba"]) for d in raw_data if d["molecule_properties"]["hba"]]
    return dict(component = "Number of Hydrogen Bond Acceptors",
                data = hbacceptor_values,
                mean = np.mean(hbacceptor_values),
                std = np.std(hbacceptor_values),
                min_value= np.min(hbacceptor_values),
                max_value = np.max(hbacceptor_values))
    
def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing a histogram for number of H-bond acceptors.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. Bars or PieChart.
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of ints

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#6bc40c",
                                 "line": {"width": 3,
                                          "color": "#4b8a08"}},
                         xbins=dict(start=min(data_array)-1,
                                    end=max(data_array)+1,
                                    size=1),
                         ),
            ]
    layout = go.Layout(xaxis={"title": "H-bond acceptors",
                              "dtick": 1},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)
    
    return dcc.Graph(figure=fig)
    