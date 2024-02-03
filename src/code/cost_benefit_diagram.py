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

    cost_benefit_config = yaml.load(yaml_path)

    return cost_benefit_config

def get_data(cost_benefit_config):
    cost_benefit_data = dict()
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