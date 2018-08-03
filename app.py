import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# Define a css styling:
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Can further customize text by definiing inline styles:
colors = {
	# Royal Blue:
	'background': '#4169E1',
	# White
	'text': '#FFFFFF',
	#White
	'main_background': '#FFFFFF',
	# Black
	'main_text': '#000000'
}

# Frontend definition:
app.layout = html.Div(style={'backgroundColor': colors['background'], 'color': colors['text']}, 
	children=[
	# children: can be omitted for cleaner code as is always first arg
	# can be str, int, list, etc...
	html.H1(children='Hello Dash',
		style={
			'textAlign': 'center',
			'color': colors['text']
		}
	),
	html.Div(children='Dash: A web application framework for Python', 
		style={
			'textAlign': 'center',
			'color': colors['text']
		}
	),
	dcc.Graph(
		id = 'example-graph',
		figure={
			'data': [
				# Dict of data for x/y vals and graph details:
				{'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name': 'SF'},
				{'x': [1,2,3], 'y': [2,4,5], 'type': 'bar', 'name': u'Montreal'},
			],
			'layout': {
				# 'title': 'Dash Data Visualization',
				'plot_bgcolor': colors['main_background'],
				'paper_bgcolor': colors['main_background'],
				'font': {
						'color': colors['main_text']
				}
			}
		}
	)
])


if __name__ == '__main__':
	app.run_server(debug=True)