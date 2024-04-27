import os
from pathlib import Path
import chardet
import pandas as pd
import yaml


def load_configuration(panda_diagram_plotter_conf_filename):
    panda_diagram_plotter_config = dict()

    riskmatrix_conf_dir = os.path.join(os.path.dirname(os.getcwd()), 'source', 'configuration')
    yaml_path = os.path.join(riskmatrix_conf_dir, panda_diagram_plotter_conf_filename)

    with open(yaml_path, "r") as file:
        panda_diagram_plotter_config = yaml.load(file, Loader=yaml.FullLoader)

    return panda_diagram_plotter_config

def get_data(startpath, destination, tablefilename, datafile_path, datafile, separator, decimal):
    # Config Variables
    if startpath == 'homedir':
        directory = os.path.join(os.getcwd(), datafile_path)
    else:  # parentdir
        directory = os.path.join(os.path.dirname(os.getcwd()), datafile_path)

    # get the Datas as dirct
    data_path = os.path.join(directory, datafile)

    # load datas from csv into dict
    detected = chardet.detect(Path(data_path).read_bytes())
    encoding = detected.get("encoding")

    print(datafile, ':', encoding)
    panda_table_data = pd.read_csv(data_path, sep=separator, decimal=decimal, encoding=encoding)
    # return data
    return panda_table_data
def create_panda_diagram_plotter(panda_diagram_plotter_config):
    pd.options.mode.copy_on_write = True

    pdp_tables = panda_diagram_plotter_config.get('diagram_inventory')
    for table_item in pdp_tables:
        print(table_item)
        startpath = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('startpath')
        destination = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('destination_path')
        imagename = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('imagename')
        datafile_path = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('datafile_path')
        datafile = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('datafile')
        if startpath == 'homedir':
            directory = os.path.join(os.getcwd(), destination)
        else:  # parentdir
            directory = os.path.join(os.path.dirname(os.getcwd()), destination)
        image_path = os.path.join(directory, imagename)
        separator = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('separator')
        decimal = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('decimal')

        # column operations
        column_operations = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('column_operations').get('datas')

        # group by / aggregation
        groupby_values = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('group_by')
        group_by_function = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('group_by_function')

        agg_funtion = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('agg_funtion')
        agg_colums = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('agg_colums')
        # dropping and renaming columns
        drop_columns = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('drop_columns')
        drop_columns_after_operations = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('drop_columns_after_operations')
        rename_columns = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('rename_columns')

        # table filtering and sorting
        where_clausel = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('where_clausel')
        order_by = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('sorting').get('order_by')
        sort_acending = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('sorting').get('sort_acending')
        sort_inplace = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('sorting').get('sort_inplace')

        # pivot settings
        pivot = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot')
        pivot_column = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_columns')
        pivot_value = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_values')

        # pivot_table settings
        pivot_table = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_table')
        pivot_table_column = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_table').get(
            'pivot_columns')
        pivot_table_value = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_table').get(
            'pivot_values')
        pivot_table_agg_function = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_table').get(
            'pivot_agg_func')
        pivot_table_indizes = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_table').get(
            'pivot_index').get('pivot_indizes')
        pivot_table_indizes_visible = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_table').get(
            'pivot_index').get('pivot_indizes_visible')
        pivot_table_rename_indizes = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('pivot_table').get(
            'pivot_index').get('pivot_rename_indizes')

        # margins (subtotals)
        margin = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('margins').get('margin')
        margin_name = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('margins').get('margin_name')
        margin_column = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('margins').get('margin_column')
        non_pivot_margin_column = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('margins').get('non_pivot_margin_column')
        non_pivot_margin_function = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('margins').get('non_pivot_margin_function')

        # chart settings
        chart = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-kind')
        title = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('title')
        x_axis_title = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('x-axis-title')
        y_axis_title = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('y-axis-title')
        x_axis_columns = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('x-axis-columns')
        y_axis_columns = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('y-axis-columns')
        index = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-index')

        # chart styles
        grid = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('grid')
        legend = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('legend')
        rot = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('rot')
        fontsize = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('fontsize')
        figsize = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('figsize')
        stacked = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('stacked')
        secondary_y = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('secondary_y')
        stylelist = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('stylelist')
        subplots = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('subplots')
        autopct = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('autopct')
        loc = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('loc')
        bbox_to_anchor = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('chart-designs').get('bbox_to_anchor')

        # get the pandas (panda data)
        panda_table_data = get_data(startpath, destination, imagename, datafile_path, datafile, separator, decimal)

        # filter by where clausel
        if where_clausel:
            panda_table_data = panda_table_data.query(where_clausel)

        # Drop unused columns
        if drop_columns and not drop_columns_after_operations:
            panda_table_data = panda_table_data.drop(columns=drop_columns)

        # set aggregation functions
        # if groupby_values and not agg_funtion and not pivot_column and not pivot_table_column:
        if groupby_values and not (pivot_column or (pivot_table_column or pivot_table_value or pivot_table_indizes)):
            match group_by_function:
                case 'max':
                    panda_table_data = panda_table_data.groupby(groupby_values, as_index=False).max()
                case 'min':
                    panda_table_data = panda_table_data.groupby(groupby_values, as_index=False).min()
                case 'head':
                    panda_table_data = panda_table_data.groupby(groupby_values, as_index=False).head()
                case 'sum':
                    panda_table_data = panda_table_data.groupby(groupby_values, as_index=False).sum()
                case 'mean':
                    panda_table_data = panda_table_data.groupby(groupby_values, as_index=False).mean()
        else:
            panda_table_data = panda_table_data

        # pivot if pivot is selected
        if pivot_table_column or pivot_table_value or pivot_table_indizes:
            if type(pivot_table_agg_function) is list:
                agg_tuple = tuple(pivot_table_agg_function)
                panda_table_data = pd.pivot_table(panda_table_data, index=pivot_table_indizes,
                                                  columns=pivot_table_column, values=pivot_table_value,
                                                  aggfunc=agg_tuple, margins=margin, margins_name=margin_name)
            elif type(pivot_table_agg_function) is dict:
                panda_table_data = pd.pivot_table(panda_table_data, index=pivot_table_indizes,
                                                  columns=pivot_table_column,
                                                  values=pivot_table_value, aggfunc=pivot_table_agg_function,
                                                  margins=margin, margins_name=margin_name)
            else:
                panda_table_data = pd.pivot_table(panda_table_data, index=pivot_table_indizes,
                                                  columns=pivot_table_column, values=pivot_table_value,
                                                  aggfunc=pivot_table_agg_function, margins=margin,
                                                  margins_name=margin_name)

        # set column operations
        if column_operations:
            for column_ops in column_operations:
                operation_function = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('column_operations').get('operations').get(column_ops).get('operation_function')
                operation_columns = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('column_operations').get('operations').get(column_ops).get('columns')
                operation_axis = panda_diagram_plotter_config.get('panda_diagram_plotter').get(table_item).get('column_operations').get('operations').get(column_ops).get('axis_number')
                match operation_function:
                    case 'max':
                        panda_table_data[column_ops] = panda_table_data[operation_columns].max(axis=operation_axis)
                    case 'min':
                        panda_table_data[column_ops] = panda_table_data[operation_columns].min(axis=operation_axis)
                    case 'head':
                        panda_table_data[column_ops] = panda_table_data[operation_columns].head(axis=operation_axis)
                    case 'sum':
                        panda_table_data[column_ops] = panda_table_data[operation_columns].sum(axis=operation_axis)
                    case 'mean':
                        panda_table_data[column_ops] = panda_table_data[operation_columns].mean(axis=operation_axis)
                    case 'diff':
                        panda_table_data[column_ops] = panda_table_data[operation_columns[1]] - panda_table_data[operation_columns[0]]

        if (margin and non_pivot_margin_column and non_pivot_margin_function and not (pivot_table_column or pivot_table_value or pivot_table_indizes)):
            match non_pivot_margin_function:
                case 'max':
                    panda_table_data = panda_table_data.append(panda_table_data[non_pivot_margin_column].max())
                case 'min':
                    panda_table_data = panda_table_data.append(panda_table_data[non_pivot_margin_column].min())
                case 'head':
                    panda_table_data = panda_table_data.append(panda_table_data[non_pivot_margin_column].head())
                case 'sum':
                    sum = panda_table_data[non_pivot_margin_column].sum()
                    sum.name = margin_name
                    # sum = sum.reset_index()
                    # panda_table_data = panda_table_data.append(sum.transpose())
                    # panda_table_data = pd.concat([panda_table_data, pd.DataFrame([sum])])

                    # panda_table_data = pd.concat([panda_table_data, pd.DataFrame([sum])])
                    # panda_table_data = panda_table_data.append(panda_table_data[non_pivot_margin_column].sum())
                    panda_table_data.loc[margin_name] = panda_table_data[non_pivot_margin_column].sum()
                case 'mean':
                    panda_table_data = panda_table_data.append(panda_table_data[non_pivot_margin_column].mean())

        # Drop unused columns
        if drop_columns and drop_columns_after_operations:
            panda_table_data = panda_table_data.drop(columns=drop_columns)

        # order by
        if order_by:
            panda_table_data.sort_values(by=order_by, inplace=sort_inplace, ascending=sort_acending)

        # rename columns
        if rename_columns:
            panda_table_data = panda_table_data.rename(columns=rename_columns)

        # set indices
        if index:
            index_values = panda_table_data.get(index)
            #panda_table_data.set_index(index_values)
            panda_table_data = panda_table_data.set_index(index)

        # rename indices
        if pivot_table_rename_indizes:
            panda_table_data = panda_table_data.rename_axis(index=pivot_table_rename_indizes)



        #   Plotter
        #   Plotter Process starts here!
        if autopct:
            panda_chart_plot = panda_table_data.plot(kind=chart, title=title, y=y_axis_columns, x=x_axis_columns, xlabel=x_axis_title,
                                                 ylabel=y_axis_title, grid=grid, stacked=stacked, legend=legend,
                                                 secondary_y=secondary_y, subplots=subplots, rot=rot, fontsize=fontsize,
                                                 figsize=figsize, autopct=autopct)
        else:
            panda_chart_plot = panda_table_data.plot(kind=chart, title=title, y=y_axis_columns, x=x_axis_columns, xlabel=x_axis_title,
                                                 ylabel=y_axis_title, grid=grid, stacked=stacked, legend=legend,
                                                 secondary_y=secondary_y, subplots=subplots, rot=rot, fontsize=fontsize,
                                                 figsize=figsize)

        match chart:
            case 'pie':
                panda_chart_plot[0].legend(loc=loc, bbox_to_anchor=bbox_to_anchor)
                plt = panda_chart_plot[0].get_figure()
                plt.savefig(image_path, bbox_inches='tight')
            case _:
                if bbox_to_anchor:
                    panda_chart_plot.legend(loc=loc, bbox_to_anchor=bbox_to_anchor)
                if loc:
                    panda_chart_plot.legend(loc=loc)
                plt = panda_chart_plot.get_figure()
                plt.savefig(image_path, bbox_inches='tight')

    return "blade runner"
panda_diagram_plotter_config = load_configuration('pandas_data_chart_plotter_conf.yaml')
create_panda_diagram_plotter(panda_diagram_plotter_config)