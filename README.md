# Pygments formatter for xsl-fo output 

This is a formatter for [pygments](http://pygments.org) that produces
output marked up with <fo:inline> tags with the appropriate
colour and other presentational attributes set according to
the pygments style in use.

To be useful this must be embeded in a complete xsl-fo document.
It was developed for use with [asciidoc](http://asciidoc.org)
to produce PDF's using [fop](http://xmlgraphics.apache.org/fop) with
minimal configuration or extra dependencies.

It is possible that it could be used in more general docbook to pdf
tool chains.

## Installation 

It is not currently available in pypi, so it must be installed from
the source distibution.
Use any of the normal installation methods from the top
directory of the distribution to install.

```console
$ python setup.py install   # Usual setup.py installation method

$ pip install .             # Using pip
```

This will install pygments if it is not already installed.
You can check that it is working by listing the formatters
and checking for the presence of one containing _xslfo_.

```console
$ pygmentize -L formatters
Formatters:
~~~~~~~~~~~
[... ommitted output ...]
* xslfo, xsl-fo:
    Format tokens as XSL-FO ``<fo:inline>`` tags.
```

## Usage 

As this just adds a new formatter type to pygments, you just use'
xslfo' where ever you might, for example, specify 'html' as a
formatter name.

```console
$ pygmentize -f xslso -l python setup.py
```

You should see lots of <fo:inline> tags

To use with asciidoc, which is the initial purpose of this extension
look at the example directory which contains a simple but complete
example.

## Example result 

You can see an example pdf file here:[[1]](https://bitbucket.org/sratcliffe/pygments-xslfo-formatter/downloads/example.pdf)
