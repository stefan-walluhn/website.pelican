Title: I know what I am doing
Date: 2012-05-01
Tags: build requirements, gentoo

Ich hab hier 'nen angestaubten Rechner mit 'ner frischen Gentoo-Installation.
Da wollte ich gerade eclipse drauf bügeln. Bekomme ich folgende Meldung:

```
krasnojarsk stefan# emerge eclipse-sdk

Calculating dependencies... done!

>>> Verifying ebuild manifests
>>> Running pre-merge checks for dev-util/eclipse-sdk-3.7.1-r7
 * Checking for at least 1280 mebibytes RAM ...                          [ !! ]
 * There is NOT at least 1280 mebibytes RAM
 * Checking for at least 1536 mebibytes disk space at "/var/tmp/portage/dev-util/eclipse-sdk-3.7.1-r7/temp" ...                                          [ ok ]
 *
 * Space constrains set in the ebuild were not met!
 * The build will most probably fail, you should enhance the space
 * as per failed tests.
 *
 * ERROR: dev-util/eclipse-sdk-3.7.1-r7 failed (pretend phase):
 *   Build requirements not met!
```

Es gibt ja [hier](http://www.debian.org/) und [da](http://www.ubuntu.com/)
Linux-Distributionen, die einem an der Stelle [im Regen
stehen](http://stackoverflow.com/questions/3643870/gem-update-system-is-disabled-on-debian-error)
lassen. Aber Gentoo wäre nicht Gentoo, wenn es nicht einen Weg gäbe, als User
seinen Willen durchzusetzen. Ich musste eine Weile suchen, aber die ganze
Nummer hat doch seinen Charme:

```
krasnojarsk stefan# I_KNOW_WHAT_I_AM_DOING=yes emerge eclipse-sdk
```

Jetzt läuft's durch.
