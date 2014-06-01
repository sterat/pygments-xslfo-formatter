
DEST=..
FILES=$(DEST)/README.md $(DEST)/README

all: $(FILES)


../README.md: README.mw
	mwtext -t md -o $(DEST)/README.md README.mw

../README: README.mw
	mwtext -t text -o $(DEST)/README README.mw
