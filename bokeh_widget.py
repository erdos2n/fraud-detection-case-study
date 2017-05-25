import pandas as pd
import numpy as np


from bokeh.plotting import figure, output_file, show
from bokeh.models.widgets import Dropdown, Select, Tabs, Panel 
from bokeh.layouts import widgetbox
from bokeh.charts import Bar, Histogram
from bokeh.io import *
from bokeh.palettes import Spectral6
from bokeh import mpl

def bokeh_plot(selected_feature='event_created_to_end', bins=15):
    color_list = ['#FF8C00', '#FAFCCC', '#EA653B', '#EE993D', \
                  '#EA653B', '#ED9239', '#A4A7AA', '#676767']

    p = figure(width=500, height=500)

    p = Histogram(new_df, values=selected_feature, label='label', color='label', title=selected_feature, \
        density=True, legend='top_right', bins=bins, palette=color_list)

    p.xaxis.axis_label_text_font_style = 'normal'
    p.yaxis.axis_label_text_font_style = 'normal'
    p.xaxis.axis_label_text_font_size = '18pt'
    p.yaxis.axis_label_text_font_size = '18pt'

    p.background_fill_color = "#acaaa8"
    p.background_fill_alpha = 0.5
    p.title.text_font = 'helvetica'
    p.title.text_font_size = '18pt'
    p.legend

# output_file("select.html")
# select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
# # output_file("bokeh_widget.html")
# # menu = [("Event Created to End", "event_create_to_end"), ("Tickets Sold", "total_tickets_sold"),
# #         ("Missing Payout Type?", "payout_type_MISSING"), ("Median Ticket Cost", "median_ticket_cost")]
# # dropdown = Dropdown(label="Select Feature", button_type="warning", menu=menu)


# def function_to_call(attr, old, new):
#     bokeh_plot()
#     select.value = new 


if __name__ == '__main__':
    df = pd.read_csv('NEWER_Clean_df.csv', index_col=0)
    d = {0: 'Not Fraud', 1: 'Fraud'}
    new_df = df[df['event_created_to_end'] < 15]
    new_df.replace({'label': d}, inplace=True)
    new_df['label'].unique()
    new_df['color_set'] = ['#FF8C00' if element == 'Fraud' else '#FAFCCC' for element in np.array(new_df['label'])]
    

    # select.on_change('value', function_to_call)
    # print select
    # show(widgetbox(select))

    menu = ["event_created_to_end", "total_tickets_sold", "payout_type_MISSING", "median_ticket_cost"]
    output_file("slider.html")

    p1 = bokeh_plot(menu[0])
    p2 = bokeh_plot(menu[1])
    p3 = bokeh_plot(menu[2])
    p4 = bokeh_plot(menu[3])
    
    tab1 = Panel(child = p1, title = 'Event Create to End')
    tab2 = Panel(child = p2, title = 'Total Tickets Sold')
    tab3 = Panel(child = p3, title = 'Payout Type Missing (yes/no)')
    tab4 = Panel(child = p4, title = 'Median Ticket Cost')

    tabs = Tabs(tabs=[tab1, tab2, tab3, tab4])
    show(tabs)