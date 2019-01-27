from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

project = u'20 methods of the data scientist and the mathematics behind them'
copyright = u'2019, Aapeli Vuorinen and Yoni Nazarathy'
author = u'Aapeli Vuorinen and Yoni Nazarathy'

version = u''
release = u'0.0.1'

extensions = [
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

master_doc = 'index'

language = None

exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

html_static_path = ['_static']

def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)