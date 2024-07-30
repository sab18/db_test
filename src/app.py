import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import sqlite3


app = dash.Dash(__name__)

server = app.server #in src/app.py

app.layout=html.Div([
    
    dbc.Button('click here',id='db-button'),
    html.P(id='text'),

])



# @app.callback(
#     Output('text','children'),
#     Input('db-button','n_clicks')
# )
# def click(n_clicks):
#     if n_clicks is not None and n_clicks > 0:
        

#         conn = sqlite3.connect('db_test.db')
#         cursor = conn.cursor()
          
#         insert_query = "INSERT INTO table_test (col1, col2) VALUES (?, ?)"
#         cursor.execute(insert_query, ('val1', 'val2')) #entry_time instead?
#         conn.commit()
#         cursor.close()
#         conn.close()

#         return "button was clicked"
#     else:
#         return 'not clicked'

print('ran')

if __name__ == "__main__":
    app.run_server(debug=True)
    
