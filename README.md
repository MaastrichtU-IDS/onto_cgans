[![Run tests](https://github.com/MaastrichtU-IDS/python-template/workflows/Run%20tests/badge.svg)](https://github.com/MaastrichtU-IDS/python-template/actions?query=workflow%3A%22Run+tests%22)

## Onto-CGANS 
This repository is still working in progress. The project aims to embed ontology (human knowledge) to GAN (Generative Adversarial Network) to generate unseen classes.

<img src="https://github.com/MaastrichtU-IDS/onto_cgans/blob/master/onto_cgans.jpg" width="600">


## Method steps
1. Find suitable and matched data and ontology. (The ontology should describe the data. For example, the data from parkinson and alzheimer patients and ontologies about these two diseases)
2. Convert ontology and data to right format/expressions
3. Embed ontology to conditional vectors
4. Add the conditional vectors (the embedded ontology) to the generator in DP-CGANS
5. ...


## Resources
Rare Disease Data:
1. EJPRD: https://resourcemap.ejprarediseases.org/#/
2. ORPHADATA: http://www.orphadata.org/cgi-bin/index.php#hoommodal

Code:
1. Deepgozero: https://github.com/bio-ontology-research-group/deepgozero
2. Ontology with Machine Learning: https://github.com/bio-ontology-research-group/machine-learning-with-ontologies
3. OntoZSL: https://github.com/genggengcss/OntoZSL
4. DP-CGANS: https://github.com/sunchang0124/dp_cgans

Study materials:
1. Knowledge Graph Embedding Tutorial: https://kge-tutorial-ecai2020.github.io/
2. Biomedical ontology embedding: https://github.com/bio-ontology-research-group/machine-learning-with-ontologies

<!-- ## How to use this template

* For the directory name, *Dockerfile*, *setup.py* and *test_application.py*, Replace all instances of **my_package** and **my-package** to the package name of your choice using [snake case](https://en.wikipedia.org/wiki/Snake_case) or dash depending on the convention.
* Leave the headers as is and update the instructions below to the specifics of your tool.
* Remove this *How to use this template section*

## My package

Write a short description of the software here.

## Prerequisites

* Python 3.9 or higher, with [pip](https://pip.pypa.io/en/stable/)
* Docker (optional)

## Installation

> Provide instructions to install the package

The package can be installed from the source code, see below to run with Docker. Using `-e` means that changes to the source code will be automatically update the package locally.

```bash
pip3 install -e .
```

## Usage

> Provide working examples on how to run the package

Run the `my-package` CLI in your terminal:

```bash
my-package hello-world "Python test"
```
Or in a Python script:

```python
from my_package.application import App

app = App()
print(app.get_hello_world('Python test'))
```

## Test and Publish

> Document how to run the tests, and if they are run automatically.

### Continuous Integration

This repository uses [GitHub Actions](/actions) to:

* Automatically run tests at each push to the `master` branch
* Publish the package to [PyPI](https://pypi.org) when a release is created (N.B.: the version of the package needs to be increased in [setup.py](/blob/master/setup.py#L6) before).

> You will need to provide your login credentials using [secrets in the repository settings](/settings/secrets) to publish to [PyPI](https://pypi.org): `PYPI_USERNAME` and `PYPI_PASSWORD`

### Test locally

Install PyTest:

```bash
pip3 install -U pytest
```

Run the tests:

```bash
pytest
```

Run a specific test in a file, and display `print` in the output:

```bash
pytest tests/test_application.py::TestApplication::test_return_value -s
```

## Docker

Build the image:

```bash
docker build -t my-package .
```

Run a container:

```bash
docker run -it --rm my-package hello-world "Python test"
``` -->

