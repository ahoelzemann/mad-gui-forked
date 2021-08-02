# MaD GUI 
***M***achine Learning 
***a***nd 
***D***ata Analytics 
***G***raphical 
***U***ser 
***I***nterface

![Test and Lint](https://github.com/mad-lab-fau/mad-gui/workflows/Test%20and%20Lint/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/mad-gui/badge/?version=latest)](https://mad-gui.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

##  What is it?
The MaD GUI is a framework for processing time series data.
Its use-cases include visualization, annotation (manual or automated), and algorithmic processing of visualized data and annotations.

## How do I get the GUI to work on my machine?
Below, we present two options how to obtain and run the GUI.
However, this will only enable you to look at our example data.
You want to load data of a specific format/system or want to use a specific algorithm? 
In this case please refer to ["Can I use it with data of my specific system or a specific algorithm?"](#can-i-use-it-with-data-of-my-specific-system-or-a-specific-algorithm).

### Option A: Standalone executable
The GUI can be packed into stand-alone executables, such that is not necessary for you to install anything on your machine.

- Windows users: download our exemplary executable here [Coming soon, including example data]
- Other operating systems: [Contact us](mailto:mad-digait@fau.de).

### Option B: Using the python package
```
pip install mad_gui
```

Then, from your command line either simply start the GUI or pass additional arguments:
```
python -m mad_gui.start_gui
python -m mad_gui.starg_gui --base_dir C:/my_data
```

Alternatively, within a python script use our [start_gui](https://github.com/mad-lab-fau/mad-gui/blob/2857ccc20766ea32f847271771b52c97e2682b79/mad_gui/start_gui.py#L26) 
function and hand it over the path where your data resides, `<data_path>` like `"C:/data"` or `"/home/data/"`: 
```
from mad_gui import start_gui
start_gui(<data_path>)
```

## How do I interact with the GUI?
<soon there will be one or more videos here, which show(s) how the GUI works>

- loading data / video / annotations
- adding annotations via an algorithm
- synchronize video and data
- export data / apply other algorithms and export results

## Can I use it with data of my specific system or a specific algorithm?
Yes, however it will need someone who is familiar with python.
You do not have experience with python but still want to load data from a specific system? [Contact us!](mailto:mad-digait@fau.de)

Developers can get basic information about the project setup in our [Developer Guidelines](https://mad-gui.readthedocs.io/en/latest/developer_guidelines.html).
If you want extend the GUI with your custom plugins, e.g. for loading data of a specific system,
or adding an algorithm, the necessary information can be found in our [API Reference](https://mad-gui.readthedocs.io/en/latest/api_reference.html).

## Can I change something at the core of the GUI?
Sure, we try to document the most important parts of the GUI to make adaption as easy as possible.
For more information, please take a look at our [Contribution Guidelines](https://mad-gui.readthedocs.io/en/latest/contribution_guidelines.html#contribution-guidelines).
