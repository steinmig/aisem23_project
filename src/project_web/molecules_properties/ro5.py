import numpy as np

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    """Implement the function that extracts number of `rule of five` violations per molecule from raw ChEMBL data
       Computes mean, median and standard deviation 
       
    Hints:
       - Number of `rule of five` violations is located in attribute `num_ro5_violations` of `molecule_properties`
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
    num_ro5_violations_values = [int(d["molecule_properties"]["num_ro5_violations"]) for d in raw_data if d["molecule_properties"]["num_ro5_violations"]]
    return dict(component="Number of ro5 violations",
                data=num_ro5_violations_values,
                mean=np.mean(num_ro5_violations_values),
                std=np.std(num_ro5_violations_values),
                max_value=np.max(num_ro5_violations_values),
                min_value=np.min(num_ro5_violations_values)
                )
    
def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing a histogram for number of `rule of five` violations.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. Bars or PieChart.
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of ints

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#002060",
                                 "line": {"width": 3,
                                          "color": "#011745"}},
                         xbins=dict(start=min(data_array)-1,
                                    end=max(data_array)+1,
                                    size=1),
                         ),
            ]
    layout = go.Layout(xaxis={"title": "Number of `rule of five` violations",
                              "dtick": 1},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)
    
    return dcc.Graph(figure=fig)
    