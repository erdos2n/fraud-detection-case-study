import pandas as pd
import numpy as np


from bokeh.plotting import figure, output_file, show
from bokeh.models.widgets import Dropdown, Select, Tabs, Panel 
from bokeh.layouts import widgetbox
from bokeh.charts import Bar, Histogram
from bokeh.io import *
from bokeh.palettes import Spectral6
from bokeh import mpl

df = pd.read_csv('NEWER_Clean_df.csv', index_col=0)
d = {0: 'Not Fraud', 1: 'Fraud'}
new_df = df[df['event_created_to_end'] < 15]
new_df.replace({'label': d}, inplace=True)
new_df['label'].unique()
new_df['color_set'] = ['#FF8C00' if element == 'Fraud' else '#FAFCCC' for element in np.array(new_df['label'])]

color_list = ['#FF8C00', '#FAFCCC', '#EA653B', '#EE993D', \
                  '#EA653B', '#ED9239', '#A4A7AA', '#676767']

menu = ["event_created_to_end", "total_tickets_sold", "payout_type_MISSING", "median_ticket_cost"]
output_file("0_trial.html")

bins = 15
p1 = figure(width=500, height=500, x_range = (new_df['event_created_to_end'].min(), new_df['event_created_to_end'].max()))
p1 = Histogram(new_df, values='event_created_to_end', label='label', color='label', title='Duration of \n Event Created to End', \
    density=True, legend='top_right', bins=bins, palette=color_list)

p1.xaxis.axis_label = ''
p1.xaxis.axis_label_text_font_style = 'normal'
p1.yaxis.axis_label_text_font_style = 'normal'
p1.xaxis.axis_label_text_font_size = '18pt'
p1.yaxis.axis_label_text_font_size = '18pt'

p1.background_fill_color = "#acaaa8"
p1.background_fill_alpha = 0.5
p1.title.text_font = 'helvetica'
p1.title.text_font_size = '18pt'

bins = 2
p2 = figure(width=500, height=500, x_range = (new_df['total_tickets_sold'].min(), new_df['total_tickets_sold'].max()))
p2 = Histogram(new_df, values='total_tickets_sold', label='label', color='label', title='Total Tickets Sold', \
    density=True, legend='top_right', bins=bins, palette=color_list)

p2.xaxis.axis_label = ''
p2.xaxis.axis_label_text_font_style = 'normal'
p2.yaxis.axis_label_text_font_style = 'normal'
p2.xaxis.axis_label_text_font_size = '18pt'
p2.yaxis.axis_label_text_font_size = '18pt'

p2.background_fill_color = "#acaaa8"
p2.background_fill_alpha = 0.5
p2.title.text_font = 'helvetica'
p2.title.text_font_size = '18pt'


bins = 2
p3 = figure(width=500, height=500, x_range = (new_df['payout_type_MISSING'].min(), new_df['payout_type_MISSING'].max()))
p3 = Histogram(new_df, values='payout_type_MISSING', label='label', color='label', title='Payout Type Missing \n (Yes/No)', \
    density=True, legend='top_right', bins=bins, palette=color_list)

p3.xaxis.axis_label = ''
p3.xaxis.axis_label_text_font_style = 'normal'
p3.yaxis.axis_label_text_font_style = 'normal'
p3.xaxis.axis_label_text_font_size = '18pt'
p3.yaxis.axis_label_text_font_size = '18pt'

p3.background_fill_color = "#acaaa8"
p3.background_fill_alpha = 0.5
p3.title.text_font = 'helvetica'
p3.title.text_font_size = '18pt'



bins = 30
p4 = figure(width=500, height=500, x_range = (new_df['median_ticket_cost'].min(), new_df['median_ticket_cost'].max()))
p4 = Histogram(new_df, values='median_ticket_cost', label='label', color='label', title='Median Ticket Cost', \
    density=True, legend='top_right', bins=bins, palette=color_list)

p4.xaxis.axis_label = ''
p4.xaxis.axis_label_text_font_style = 'normal'
p4.yaxis.axis_label_text_font_style = 'normal'
p4.xaxis.axis_label_text_font_size = '18pt'
p4.yaxis.axis_label_text_font_size = '18pt'

p4.background_fill_color = "#acaaa8"
p4.background_fill_alpha = 0.5
p4.title.text_font = 'helvetica'
p4.title.text_font_size = '18pt'


tab1 = Panel(child = p1, title = 'Event Create to End')
tab2 = Panel(child = p2, title = 'Total Tickets Sold')
tab3 = Panel(child = p3, title = 'Payout Type Missing (yes/no)')
tab4 = Panel(child = p4, title = 'Median Ticket Cost')

tabs = Tabs(tabs=[tab1, tab2, tab3, tab4])
show(tabs)