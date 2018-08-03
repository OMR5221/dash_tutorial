import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

agri_df = pd.read_csv(
	'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')
	
def generate_table(dataframe, max_rows=10):

	return html.Table(
		# Header using listcomprehension:
		[html.Tr([html.Th(col) for col in dataframe.columns])] +
		
		# Body: Creates list from df segments from record i and each column:
		[html.Tr([
			html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
		]) 
		# min(num rows, max_rows=10):
		for i in range(min(len(dataframe), max_rows))]
	)
	
	
app = dash.Dash()

# Define a css styling:
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
		html.H4(children='US Agriculture Exports (2011)'),
		# Run function to gen table:
		generate_table(agri_df)
])


if __name__ == '__main__':
	app.run_server(debug=True)