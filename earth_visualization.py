import plotly.graph_objects as go
import numpy as np

def plot_earth_with_satellites(positions):

    R = 6371

    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = R * np.outer(np.cos(u), np.sin(v))
    y = R * np.outer(np.sin(u), np.sin(v))
    z = R * np.outer(np.ones(np.size(u)), np.cos(v))

    earth = go.Surface(x=x, y=y, z=z, opacity=0.6)

    sat_x = positions[:,0]
    sat_y = positions[:,1]
    sat_z = positions[:,2]

    sats = go.Scatter3d(
        x=sat_x,
        y=sat_y,
        z=sat_z,
        mode="markers",
        marker=dict(size=2, color="red")
    )

    fig = go.Figure(data=[earth, sats])
    fig.show()