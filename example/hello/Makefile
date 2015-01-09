CFLAGS = -g -std=gnu99 -Wall
VERSION = 0.1
prefix = /usr
bindir = ${prefix}/bin
libdir = ${prefix}/lib64
docdir = ${prefix}/share/doc
TARGET = hello
INSTALL = /usr/bin/install
RM = rm -f
ALLFILES = hello.c README Makefile

hello: $(TARGET).c
	$(CC) $(CFLAGS) $(TARGET).c -o  $(TARGET)

	
install: hello
	$(INSTALL) -D $(TARGET) $(bindir)/$(TARGET)
	$(INSTALL) -D README $(docdir)/README

clean:
	$(RM) $(TARGET)

uninstall:
	$(RM)  $(bindir)/$(TARGET) $(docdir)/README
	
dist:
	sed -i "s/^\(Version: \).*/\1$(VERSION)/" hello.spec
	ln -s . $(TARGET)-$(VERSION)
	tar acvf $(TARGET)-$(VERSION).tar.gz $(addprefix $(TARGET)-$(VERSION)/,$(ALLFILES))
	$(RM) hello-$(VERSION)
