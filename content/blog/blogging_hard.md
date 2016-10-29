Title: Blogging the hard way
Date: 2016-10-29
Tags: blog, pelican, github, travis, deployment, ci

Ich hab mal eben die Blog-Engine gewechselt für die hier auftauchenden Inhalte.
Ich mag PHP nicht, in erster Linie weil ich das hier alles auf meinem eigenen
Server laufen habe und ich wenig Bock habe, jede Woche drei
[Sicherheitsupdates](https://wordpress.org/news/category/security/)
einzuspielen. Ohne PHP bleibt allerdings nicht wirklich viel übrig. Das
Arbeitspferd in vielen Jahren war bisher [Movable
Type](https://movabletype.com/). Die Software fährt einen spannenden Ansatz und
generiert statische HTML-Seiten, die dann ganz direkt und ohne viel Magie vom
Webserver ausgeliefert wurden. Aber, Movable Type ist eine Perl-Software. Ich
hatte in den letzten Jahren immer mehr das Gefühl ein antikes Museum zu
betreiben. Es findet zwar nach wie vor Entwicklung statt, aber die Firma hinter
dem Projekt hält es für eine clevere Idee, die aktuelle Version nicht länger
unter einer OpenSource-Lizenz zu veröffentlichen. Ich melde daher seit einiger
Zeit eine grundlegende Meinungsverschiedenheit an.

Da ich nicht vor habe viel mehr zu veranstalten als ein wenig rumgeblogge von
Zeit zu Zeit, sehe ich keinen großen Sinn darin, jetzt irgend eines meiner für
gut befundenen CMS / Frameworks auszupacken und an
[Kotti](http://kotti.pylonsproject.org/) oder
[Django](https://www.djangoproject.com/) ein Blog-Plugin zu stricken. Für ein
anderes Projekt hatte ich im letzten Jahr
[Pelican](http://blog.getpelican.com/) in der Hand.

Pelican ist witzig: Der Schwimmvogel läuft überhaupt nicht auf dem Server,
sondern generiert lokal aus einem Haufen Markdown-Files eine Sammlung
statisches HTML (also ähnlich wie Movable Type, nur lokal und ohne GUI). Für
mich war an dieser Stelle die spannendste Frage, wie ich einen flüssigen
Prozess auf die Füße gestellt bekomme, um fix Inhalte zu pushen, ohne jedes mal
auf allen Geräten Pelican zu installieren, die Seite zu rendern und dann via
SSH den ganzen Krempel zu pushen. Und das geht so:

## Schreiben

Einfach vim aufmachen und eine [Markdown-formatierte
Textdatei](https://raw.githubusercontent.com/stefan-walluhn/website.pelican/63dad4325cc9b3cf216912cb084d267b642f5861/content/blog/blogging_hard.md)
schreiben. Meta-Daten in die Kopfzeile dumpen, speichern, fertig.

## Speichern

Der ganze Kram liegt in einem
[Git-Repository](https://github.com/stefan-walluhn/website.pelican). Ich kann
meine Änderungen daher einfach zu Github pushen, komme so von überall an den
Content und habe sogar eine schicke Historie, wann ich was geschrieben oder
geändert habe.

## Rendern

Sobald bei Github eine Änderung eingeht, legt [Travis](https://travis-ci.org/)
los, zieht sich das Repository und Pelican und rendert die Seite. Danke Travis!

## Upload

Ich hab lange überlegt, was hier sinnvoll ist. Vor längerer Zeit hatte ich
einen Ansatz mit [Gitlab](https://about.gitlab.com/gitlab-ci/) ausprobiert, bei
dem ein Runner auf dem Zielsystem die Seite noch einmal rendert. Aber das ist
ja eigentlich Blödsinn, die Seite ist ja bereits fertig. Wie kommt also der
Content aus der Travis CI auf den Server?

Die Antwort: WebDAV. Auf dem Server läuft ein eigener nginx vhost für Travis,
schick verschlüsselt dank [Let's Encrypt](https://letsencrypt.org/) und
zugangsbeschränkt per Basic Auth. Travis bekommt von mir die Zugangsdaten und
ein
[curl-Einzeiler](https://github.com/stefan-walluhn/website.pelican/blob/d3a3161d1be11698b9d369c73af7ed6877c38101/.travis.yml#L14)
pusht die gerenderte Seite. Fertig.

Das ist als Workflow natürlich weniger für Wordpress-Klicker:innen geeignet,
aber für Menschen, die eh den ganzen Tag an Github hängen halte ich dieses
Setup für einen ganz schicken Ansatz inklusive einem enormen Sicherheitsgewinn
auf dem Zielsystem (vorausgesetzt ihr vertraut Travis CI).
