def plt_bar(lst, test_point_hr = None, kde = True, title = None, grid = True, figsize = (10, 10),             xlabel = None, ylabel = 'percentage', extra_colors = [], labels = None):
    
    
    """Takes a list of arrays and 
    plots their histograms on the same graph

    Inputs:
        lst:             list of arrays, each array will have a histogram
        test_point_hr:   shades in bar of predicted hour datapoint, default = None
        kde:             will graph the kde or not graph the kde, default = True
        title:           main title of the plot, default 'None'
        grid:            grid appears if True, no grid if False, default True
        figsize:         size of the plot, default = (10, 10)
        xlabel:          label of x-axis, default = 'None'
        ylabel:          label of y-axis, default = 'percentage'
        extra_colors:    list of other colors to add to the color_list, default = []
        labels:          list of labels for each histogram, default = []

    -------------------
    Returns: a histogram of each array in the list
        """
    color_list = ['#FF8C00', '#FAFCCC', '#EA653B', '#EE993D',                   '#EA653B','#ED9239', '#A4A7AA', '#676767']
    
    if extra_colors != []: 
        for c in extra_colors:
            color_list.append(c)
    
    
    if len(lst) > len(color_list):
        print 'Not enough colors for each histogram'
        print 'we will automatically assign them to black'
        print 'Assign {} more colors to fix this problem'.format(len(lst) - len(color_list))
        
    
    fig = plt.figure(figsize=figsize)
    
    if grid:
        plt.grid(zorder = 0, linestyle = 'dashed', color = '#acaaa8')
    
    
    for index, array in enumerate(lst):
        cnt = Counter()
        for hr in array:
            cnt[hr] += 1
        
        xvalues = cnt.keys()
        yvalues = cnt.values()
        bar_list = plt.bar(xvalues, 
                           [yvalue * .001 for yvalue in yvalues],
                           ec = 'k', 
                           color=color_list[index], 
                           zorder = 3,
                           alpha = 0.8)
        if labels:
            bar_list.set_label(labels[index])
        
        if test_point_hr and index == 0:
            bar_list[test_point_hr].set_color('r')
            bar_list[test_point_hr].set_label('Tested Point')
        
        elif test_point_hr and index == 1:
            bar_list[test_point_hr].set_color('r')
        
        
        if kde:
            sns.kdeplot(array,
                        color = '#EA653B',
                        linewidth = 3,
                        zorder = 4, 
                        alpha = 0.8,
                        label = '')
        
        plt.legend()
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    
    
        
    plt.show()


# In[ ]:

def total_tickets_sold(x):
    """
    Input: dataframe x with column 'quantity sold'
    ------------
    Returns: Total Number of Tickets sold
    """
    sold = []
    for i in x:
        sold.append(i['quantity_sold'])
    return sum(sold)

def median_ticket_cost(x):
    """
    Input: dataframe x with column called 'cost'
    ----------------
    Returns: median cost
    """
    costs = []

    for i in x:

        costs.append(i['cost'])

    return np.median(costs) 

if __init__ == '__main__':
    df = pd.read_csv('NEWER_Clean_df.csv')
    fcreate = new_df[new_df['label'] == 'Fraud']['event_created_to_end']
    tcreate = new_df[new_df['label'] == 'Not Fraud']['event_created_to_end']
    fcreate = np.array(fcreate)
    tcreate = np.array(tcreate)


    plt_bar([fcreate, tcreate], test_point_hr = 11, title = 'Created Date minus End Date', xlabel = 'Duration',\
        labels = ['Fraud', 'Not Fraud'])