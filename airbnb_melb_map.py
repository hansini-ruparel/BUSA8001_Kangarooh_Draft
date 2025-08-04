import pandas as pd
import plotly.express as px
custom_orange_scale = [
    [0.0, "#7f2704"],   # Dark burnt orange
    [0.2, "#d94801"],   # Deep orange
    [0.5, "#fd8d3c"],   # Medium orange
    [0.8, "#fdae6b"],   # Lighter orange
    [1.0, "#fdd0a2"]    # Very light orange
]

df  = pd.read_csv('train.csv')
# print(df.head(10))

df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)


fig = px.scatter_mapbox(df, lon = df['longitude'], lat = df['latitude'], 
                       zoom = 9.5, color_continuous_scale=custom_orange_scale,
                       color = df['price'], width = 1200, height = 900, title = 'Price of Airbnb in Melbourne')

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0, "t":50, "l":0, "b":10})
fig.show()
