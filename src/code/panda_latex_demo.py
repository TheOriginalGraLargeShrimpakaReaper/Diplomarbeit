import os
import pandas as pd
import yaml


# Get the Configuration
def load_configuration(plt_conf_filename):
    panda_latex_tables_config = dict()
    plt_conf_dir = os.path.join(os.path.dirname(os.getcwd()), 'source', 'configuration')
    yaml_path = os.path.join(plt_conf_dir, plt_conf_filename)

    with open(yaml_path, "r") as file:
        panda_latex_tables_config = yaml.load(file, Loader=yaml.FullLoader)

    return panda_latex_tables_config

def get_data(startpath, destination, tablefilename, datafile_path, datafile):
    # Config Variables
    if startpath == 'homedir':
        directory = os.path.join(os.getcwd(), datafile_path)
    else:   # parentdir
        directory = os.path.join(os.path.dirname(os.getcwd()), datafile_path)

    # get the Datas as dirct
    data_path = os.path.join(directory, datafile)

    # load datas from csv into dict
    panda_table_data = pd.read_csv(data_path, sep=",", decimal=".", encoding = "latin1")

    # return data
    return panda_table_data

def create_latex_tables(panda_latex_tables_config):
    plt_tables = panda_latex_tables_config.get('tables_inventory')
    for table_item in plt_tables:
        # id and filesystem informations
        table_id = panda_latex_tables_config.get('tables').get(table_item).get('id')
        startpath = panda_latex_tables_config.get('tables').get(table_item).get('startpath')
        destination = panda_latex_tables_config.get('tables').get(table_item).get('destination_path')
        tablefilename = panda_latex_tables_config.get('tables').get(table_item).get('tablefilename')
        datafile_path = panda_latex_tables_config.get('tables').get(table_item).get('datafile_path')
        datafile = panda_latex_tables_config.get('tables').get(table_item).get('datafile')
        if startpath == 'homedir':
            directory = os.path.join(os.getcwd(), destination)
        else:  # parentdir
            directory = os.path.join(os.path.dirname(os.getcwd()), destination)
        tablefile = os.path.join(directory, tablefilename)

        # group by / aggregation
        groupby_values = panda_latex_tables_config.get('tables').get(table_item).get('group_by')
        group_by_function = panda_latex_tables_config.get('tables').get(table_item).get('group_by_function')
        #selected_rows = panda_latex_tables_config.get('tables').get(table_item).get('selected_rows')
        agg_funtion = panda_latex_tables_config.get('tables').get(table_item).get('agg_funtion')
        agg_colums = panda_latex_tables_config.get('tables').get(table_item).get('agg_colums')
        # dropping and renaming columns
        drop_columns = panda_latex_tables_config.get('tables').get(table_item).get('drop_columns')
        rename_columns = panda_latex_tables_config.get('tables').get(table_item).get('rename_columns')

        # table filtering and sorting
        where_clausel = panda_latex_tables_config.get('tables').get(table_item).get('where_clausel')
        order_by = panda_latex_tables_config.get('tables').get(table_item).get('sorting').get('order_by')
        sort_acending = panda_latex_tables_config.get('tables').get(table_item).get('sorting').get('sort_acending')
        sort_inplace = panda_latex_tables_config.get('tables').get(table_item).get('sorting').get('sort_inplace')

        # pivot settings
        pivot = panda_latex_tables_config.get('tables').get(table_item).get('pivot')
        pivot_column = panda_latex_tables_config.get('tables').get(table_item).get('pivot_columns')
        pivot_value = panda_latex_tables_config.get('tables').get(table_item).get('pivot_values')

        # pivot_table settings
        pivot_table = panda_latex_tables_config.get('tables').get(table_item).get('pivot_table')
        pivot_table_column = panda_latex_tables_config.get('tables').get(table_item).get('pivot_table').get('pivot_columns')
        pivot_table_value = panda_latex_tables_config.get('tables').get(table_item).get('pivot_table').get('pivot_values')
        pivot_table_agg_function = panda_latex_tables_config.get('tables').get(table_item).get('pivot_table').get('pivot_agg_func')
        pivot_table_indizes = panda_latex_tables_config.get('tables').get(table_item).get('pivot_table').get('pivot_index').get('pivot_indizes')
        pivot_table_indizes_visible = panda_latex_tables_config.get('tables').get(table_item).get('pivot_table').get('pivot_index').get('pivot_indizes_visible')
        pivot_table_rename_indizes = panda_latex_tables_config.get('tables').get(table_item).get('pivot_table').get('pivot_index').get('pivot_rename_indizes')

        # margins (subtotals)
        margin = panda_latex_tables_config.get('tables').get(table_item).get('margins').get('margin')
        margin_name = panda_latex_tables_config.get('tables').get(table_item).get('margins').get('margin_name')

        # table settings
        table_caption = panda_latex_tables_config.get('tables').get(table_item).get('caption')
        table_label = panda_latex_tables_config.get('tables').get(table_item).get('label')
        table_style = panda_latex_tables_config.get('tables').get(table_item).get('table_styles')
        sparse_columns = panda_latex_tables_config.get('tables').get(table_item).get('table_styles').get('sparse_columns')
        table_caption_position = panda_latex_tables_config.get('tables').get(table_item).get('table_styles').get('props').get('caption-side')
        table_position = panda_latex_tables_config.get('tables').get(table_item).get('table_styles').get('props').get('position')
        longtable = panda_latex_tables_config.get('tables').get(table_item).get('table_styles').get('props').get('longtable')

        # get the pandas (panda data)
        panda_table_data = get_data(startpath, destination, tablefilename, datafile_path, datafile)

        # Drop unused columns
        if drop_columns:
            panda_table_data = panda_table_data.drop(columns=drop_columns)

        # filter by where clausel
        if where_clausel:
            panda_table_data = panda_table_data.query(where_clausel)

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
                panda_table_data = pd.pivot_table(panda_table_data, index=pivot_table_indizes, columns=pivot_table_column, values=pivot_table_value, aggfunc=agg_tuple, margins=margin, margins_name=margin_name)
            elif type(pivot_table_agg_function) is dict:
                panda_table_data = pd.pivot_table(panda_table_data, index=pivot_table_indizes, columns=pivot_table_column,
                                                  values=pivot_table_value, aggfunc=pivot_table_agg_function, margins=margin, margins_name=margin_name)
            else:
                panda_table_data = pd.pivot_table(panda_table_data, index=pivot_table_indizes, columns=pivot_table_column, values=pivot_table_value, aggfunc=pivot_table_agg_function, margins=margin, margins_name=margin_name)

        # order by
        if order_by:
            panda_table_data.sort_values(by=order_by, inplace=sort_inplace, ascending=sort_acending)

        # rename columns
        if rename_columns:
            panda_table_data = panda_table_data.rename(columns=rename_columns)

        # rename indices
        if pivot_table_rename_indizes:
            panda_table_data = panda_table_data.rename_axis(index=pivot_table_rename_indizes)

        # convert python panda to latex table
        latex_table = panda_table_data.to_latex(header=True, bold_rows=False, longtable=longtable, sparsify=sparse_columns, label=table_label, caption=table_caption, position=table_position, na_rep='', index=pivot_table_indizes_visible)

        # caption below is not supported yet (pandas 2.2)
        # replace caption and replace table end with the caption line and table end
        if table_caption_position == 'below':
            caption_label = "\\caption{" + table_caption + "} \\label{" + table_label + "} \\\\"
            caption_label_nbr = "\\caption{" + table_caption + "} \\label{" + table_label + "}"
            caption_only = "\\caption{" + table_caption + "} \\\\"
            caption_only_nbr = "\\caption{" + table_caption + "}"
            label_only = "\\label{" + table_label + "} \\\\"
            label_only_nbr = "\\label{" + table_label + "}"
            latex_table = latex_table.replace(caption_label, '')
            latex_table = latex_table.replace(caption_only, '')
            latex_table = latex_table.replace(label_only, '')
            latex_table = latex_table.replace(caption_label_nbr, '')
            latex_table = latex_table.replace(caption_only_nbr, '')
            latex_table = latex_table.replace(label_only_nbr, '')

            if longtable:
                table_string = '\\end{longtable}'
                new_caption = caption_label_nbr + "\n" + table_string
                latex_table = latex_table.replace(table_string, new_caption)
            else:
                table_string = '\\end{table}'
                new_caption = caption_label_nbr + "\n" + table_string
                latex_table = latex_table.replace(table_string, new_caption)


        # write latex table to filesystem
        with open(tablefile, 'w') as wrlt:
            wrlt.write(latex_table)

# run the methods / functions
panda_latex_tables_config = load_configuration('panda_latex_demo.yaml')
create_latex_tables(panda_latex_tables_config)