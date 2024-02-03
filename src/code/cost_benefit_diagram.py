import matplotlib.pyplot as plt
import os
import csv
import pandas as pd
import yaml

def load_configuration():
    cost_benefit_config = dict()
    cbd_conf_filename = 'scatter_plotter_conf.yaml'
    cbd_conf_dir = os.path.join(os.path.dirname(os.getcwd()), 'source', 'configuration')
    # cbd_conf_dir = os.path.join(os.getcwd(), 'src', 'content')
    yaml_path = os.path.join(cbd_conf_dir, cbd_conf_filename)

#    with open(yaml_path) as json_string:
#        cost_benefit_config = json.load(json_string)

    with open(yaml_path, "r") as file:
        cost_benefit_config = yaml.load(file, Loader=yaml.FullLoader)
        #pprint(data)
    #cost_benefit_config = yaml.load(yaml_path, Loader=yaml.Loader)

    return cost_benefit_config

def get_data(cost_benefit_config):
    cost_benefit_data = dict()

    risk_conf = cost_benefit_config.get(risk)
    startpath = risk_conf.get('startpath')
    destination = risk_conf.get('destinatination')
    imagename = risk_conf.get('imagename')
    datafilename = risk_conf.get('datafilename')
    itemname = risk_conf.get('itemname')
    x_axis_title = risk_conf.get('x-axis-title')
    y_axis_title = risk_conf.get('y-axis-title')
    title = risk_conf.get('title')
    bubble_standard_size = int(risk_conf.get('bubble-standard-size'))

    if startpath == 'homedir':
        directory = os.path.join(os.getcwd(), destination)
    else:   # parentdir
        directory = os.path.join(os.path.dirname(os.getcwd()), destination)

    print(directory)

    # get the Datas as dirct
    data_path = os.path.join(directory, datafilename)
    image_path = os.path.join(directory, imagename)

    # load datas from csv into dict
    with open(data_path) as f:
        csv_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]

    (_, *header), *data = csv_list
    datas = {}
    for row in data:
        key, *values = row
        datas[key] = {key: value for key, value in zip(header, values)}
    return cost_benefit_data
def cost_benefit_diagram (cost_benefit_config, cost_benefit_data):
    # Datenpunkte
    #data = {'Variante a': (88, 74), 'Variante b': (95, 91), 'Variante c': (55, 60)}

    # Daten extrahieren
    labels, values = zip(*cost_benefit_data.items())
    x, y = zip(*values)

    # Scatter-Diagramm erstellen
    plt.scatter(x, y, color='blue')

    # X-Linie bei y=80
    plt.axhline(y=80, color='red', linestyle='--', label='Kosten-Maximum')

    # Y-Linie bei x=80
    plt.axvline(x=80, color='green', linestyle='--', label='Punkte-Minimum')

    # Beschriftung hinzufügen
    plt.xlabel('Punkte')
    plt.ylabel('Kosten')
    plt.title('Kosten-Nutzen-Diagramm')

    # Datenpunkte beschriften
    for label, x_point, y_point in zip(labels, x, y):
        plt.text(x_point, y_point, label)

    # Legende anzeigen
    plt.legend()

    # Diagramm anzeigen
    plt.grid(True)
    plt.show()

    # Diagramm als PNG speichern
    plt.savefig('scatter_plot.png')

cost_benefit_config = load_configuration()
cost_benefit_data = get_data(cost_benefit_config)
cost_benefit_diagram(cost_benefit_config, cost_benefit_data)