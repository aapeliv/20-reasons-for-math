from recommonmark.parser import CommonMarkParser

project = u'Data science book'
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
