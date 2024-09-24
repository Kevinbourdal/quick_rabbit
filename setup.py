import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = "0.0.6"
PACKAGE_NAME = "quick_rabbit"
AUTHOR = "Kevin Lopez Bourdal"
AUTHOR_EMAIL = "kevin.bourdal@outlook.com"
URL = "https://github.com/Kevinbourdal"

LICENSE = 'MIT'  # Tipo de licencia
DESCRIPTION = "Libreria para utilizar rabbit MQ de una forma facil y rapida "
LONG_DESCRIPTION = (HERE / "README.md").read_text(
    encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

# Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
    "pika",
    "simplejson"
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
