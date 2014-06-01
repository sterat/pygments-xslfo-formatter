# -*- coding: utf-8 -*-
"""
	pygments.formatters.html
	~~~~~~~~~~~~~~~~~~~~~~~~

	Formatter for XSL-FO output.

	:copyright: Copyright 2014, Steve Ratcliffe
	:license: BSD, see LICENSE for details.
"""

from pygments.formatter import Formatter
from pygments.util import bytes

__all__ = ['XslfoFormatter']


_escape_html_table = {
	ord('&'): u'&amp;',
	ord('<'): u'&lt;',
	ord('>'): u'&gt;',
	ord('"'): u'&quot;',
	ord("'"): u'&#39;',
	}


def escape_html(text, table=_escape_html_table):
	"""Escape &, <, > as well as single and double quotes for HTML."""
	return text.translate(table)


class XslfoFormatter(Formatter):
	r"""
	Format tokens as XSL-FO ``<fo:inline>`` tags.
	"""

	name = 'XSL-FO formatter'
	aliases = ['xslfo', 'xsl-fo']
	filenames = []

	def __init__(self, **options):
		Formatter.__init__(self, **options)
		self.title = self._decodeifneeded(self.title)

		# Holds fo attributes that correspond to each style type.
		self.styles = {}
		self.background_colour = self.style.background_color or '#ffffff'

		# Iterate over the style and create a list of fo attributes that describe it.
		for token, style in self.style:
			atts = []
			if style['color']:
				atts.append('color="#%s"' % style['color'])
			if style['bold']:
				atts.append('font-weight="bold"')
			if style['italic']:
				atts.append('font-style="italic"')
			if style['underline']:
				atts.append('text-decoration="underline"')

			# Save the attributes for this style
			self.styles[token] = ' '.join(atts)

	def _decodeifneeded(self, value):
		if isinstance(value, bytes):
			if self.encoding:
				return value.decode(self.encoding)
			return value.decode()
		return value

	def format_unencoded(self, tokensource, outfile):
		"""
		Read the token source and write it marked up with fo:inline styles.

		We join together tokens with the same token type and then surround the
		text with a fo:inline tag with appropriate attributes for the style
		element.

		The whole thing is wrapped in a fo:block tag.
		"""

		def write_value(t, val):
			atts = self.styles[t]
			outfile.write('<fo:inline %s>%s</fo:inline>' % (atts, escape_html(val)))

		outfile.write(
			'<fo:block background-color="%s" xmlns:fo="http://www.w3.org/1999/XSL/Format">'
				% self.background_colour)

		lastval = ''
		lasttype = None
		for ttype, value in tokensource:
			while ttype not in self.styles:
				ttype = ttype.parent

			if ttype == lasttype:
				lastval += value
			else:
				if lastval:
					write_value(lasttype, lastval)
				lastval = value
				lasttype = ttype

		if lastval:
			write_value(lasttype, lastval)

		outfile.write('</fo:block>')
