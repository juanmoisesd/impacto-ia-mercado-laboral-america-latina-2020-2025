"""Impacto de la Inteligencia Artificial en el Mercado Laboral de América Latina (2020-2025)
DOI: 10.5281/zenodo.19211331 | GitHub: https://github.com/juanmoisesd/impacto-ia-mercado-laboral-america-latina-2020-2025"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="10.5281/zenodo.19211331".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). Impacto de la Inteligencia Artificial en el Mercado Laboral de América Latina (2. Zenodo. https://doi.org/10.5281/zenodo.19211331'
def info(): print(f"Dataset: Impacto de la Inteligencia Artificial en el Mercado Laboral de América Latina (2\nDOI: 10.5281/zenodo.19211331\nGitHub: https://github.com/juanmoisesd/impacto-ia-mercado-laboral-america-latina-2020-2025")