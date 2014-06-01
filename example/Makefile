
A2X=a2x

PDF_OPTS=\
	--asciidoc-opts='--conf-file=local-docbook45.conf' \
	-a tabsize=4 \
	-a source-highlighter=pygments \
	-a pygments-style=default

all: example.pdf

example.pdf: example.adoc
	$(A2X) -L --xsl-file=fo.xsl --fop $(PDF_OPTS) example.adoc

clean:
	rm -f example.pdf
