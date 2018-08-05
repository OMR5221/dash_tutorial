# dash_core_components: library includes a Graph component
# Graph: renders interactive data visualizations using plotly.js Javascript graph library
# Craete a scatter plot from a pnadas DF

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_obj as go


app = dash.Dash()

# Create pandas DF from csv filke at url
df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')
	
	
app.layout = html.Div([
	dcc.Graph(
		id='life-exp-vs-gdp',
		figure={
			'data': [
				go.Scatter(
					# x: gdp per capita per continent
					x = df[df['continent'] == i]['gdp per capita'],
					# y: life expectancy per continent
					y = df[df['continent'] == i]['life expectancy'],
					# text: country name per continent
					text = df[df['continent'] == i]['country'],
					mode = 'markers',
					opacity = 0.7,
					marker = {
						'size': 15,
						'line': {'width': 0.5, 'color': 'white'}
					},
					# continent:
					name = i
				) 
				# loop thorough continents:
				for i in df.continent.unique()
			],
			'layout': go.Layout(
				# Define labels per axis
				xaxis = {'type': 'log', 'title': 'GDP Per Capita'},
				yaxis = {'title': 'Life Expectancy'},
				# define margin widths per side
				margin = {'l': 40, 'b': 40, 't': 10, 'r': 10},
				# define legend attributes:
				legend = {'x': 0, 'y': 1},
				# define what occurs on a hover by user?
				hovermode = 'closet'
			)
		}

])