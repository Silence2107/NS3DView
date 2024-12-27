import numpy as np
import plotly.graph_objects as go

# Parameters
R = 1  # Radius of the sphere
grid_size = 50  # Resolution of the 3D grid

# Create a 3D grid

x = np.linspace(0, R, grid_size)
y = np.linspace(-R, R, grid_size)
z = np.linspace(-R, R, grid_size)
X, Y, Z = np.meshgrid(x, y, z)

# Compute the sphere volume
distance_from_center = np.sqrt(X**2 + Y**2 + Z**2)
sphere = distance_from_center <= R  # Boolean mask for the sphere

# Map a property (e.g., radius) to the volume
property_values = distance_from_center

# Create a volume plot
fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=property_values.flatten(),  # Property to color the volume
    isomin=0,
    isomax=R,
    opacity=0.7,  # Transparency
    surface_count=25,  # Number of layers
    colorscale='plasma' ))

fig.update_layout(title='3D Sphere Volume with Plotly')
fig.show()
