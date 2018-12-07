# -*- coding: utf8 -*-
"""
A minimal front end to the Docutils Publisher in one file.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import sys
from docutils.core import publish_cmdline, publish_cmdline_to_binary, default_description
from docutils.writers.odf_odt import Writer, Reader


descriptions = {
    'html': ('Generates (X)HTML documents from standalone reStructuredText'
               'sources.  ' + default_description),
    'odt': ('Generates OpenDocument/OpenOffice/ODF documents from '
               'standalone reStructuredText sources.  ' + default_description),
    'html5': (u'Generates HTML 5 documents from standalone '
               u'reStructuredText sources ' + default_description)
}

if len(sys.argv) < 2:
    print 'Not enough arguments. Use one of: ' + ", ".join(descriptions.keys())
    exit()

writer_name = sys.argv[1]
if writer_name not in descriptions:
    print 'Unknown writer: ' + writer_name + '. Use one of: ' + ", ".join(descriptions.keys())
    sys.exit()
del sys.argv[1]
description = descriptions[writer_name]


if writer_name == 'html' or writer_name == 'html5':
    publish_cmdline(writer_name=writer_name, description=description)
elif writer_name == 'odt':
    writer = Writer()
    reader = Reader()
    output = publish_cmdline_to_binary(reader=reader, writer=writer, description=description)
