Title: Ansible, lookups und Listen...
Date: 2016-04-28
Tags: asnible, lookups, lists, documentation

...oder auch, wir brauchen keine Doku, wir haben doch Code.

Es kommt vor, dass ich für ein Deployment Wissen aus externen Systemen
benötige. Ansible kennt dafür das Konzept der
[Lookups](http://docs.ansible.com/ansible/playbooks_lookups.html). So weit, so
gut. Spannend wird es immer dann, wenn ich den Editor anwerfe und feststelle,
dass es zwar irgendwelche Konzepte gibt, die Doku allerdings auf einem Stand
der Sorte: "Ja, geht, irgendwie da lang, und hier mal noch ein paar halbgare
Brocken, komm klar" ist.

Beispiel? [Klar
doch](http://docs.ansible.com/ansible/developing_plugins.html#distributing-plugins):
*"Plugins are loaded from both Python's site_packages (those that ship with
ansible) and a configured plugins directory, which defaults to
/usr/share/ansible/plugins, in a subfolder for each plugin type: [...] In
addition, plugins can be shipped in a subdirectory relative to a top-level
playbook, in folders named the same as indicated above."*

Heißt was genau? Ich hätte für mein Plugin gern ein Python-Egg, dass ich
vernünftig testen und dann releases kann, damit auch andere was davon haben.
Klingt nach Doku nicht ganz abwegig. Loaded from site_packages, subfolder for
each plugin type...

Einfach mal so bauen, einbinden, nix. Kaputt. Plugin nicht gefunden. Komisch,
wenn ich in den Ansible-Code schaue, ist die Ordnerstruktur ganz anders. Also
Debugger anwerfen und mal schauen, wie die Plugins geladen werden. Breakpoint
wird gefunden, Debugger aufgerufen ... und direkt von Ansible wieder gekillt.
Suuper, ganz tolle Idee, Ansible! Mit print() weiter, kotz.

Am Ende stellt sich raus: *"Plugins are loaded from both Python's site_packages
(those that ship with ansible)"* Ja, das soll heißen "ONLY those that ship with
ansible". Warum schreibt ihr es dann in die Doku??? Das euere eigenen Plugins
funktionieren und geladen werden, darf ich ja wohl erwarten! Thirdparty-Plugins
werden eben NICHT aus den site_packages geladen. Und damit kann auch niemand
Plugins mit Standard-Werkzeugen erstellen und veröffentlichen.

Also nach Doku einfach nen Python-File nach "./lookup_plugins" werfen. Gebaut,
Liste zurück gegeben, eingebunden, was passiert? Nein, in Ansible kommt nicht
['one', 'two', 'three'] zurück, sondern 'one, two, three'.

WHAAAT?

Ich hab dann nochmal 2 Stunden drangehangen und viel Code gelesen, bis ich [die
Stelle](https://github.com/ansible/ansible/blob/v2.0.2.0-1/lib/ansible/template/__init__.py#L410)
gefunden habe. Ja, das heißt, dass ich bei einem Lookup

    {{ lookup('MY_LOOKUP', [...], wantlist=True) }}

schreiben muss, damit Ansible nicht versucht clever zu sein und ich eine Liste
in die Hand bekomme. Und siehe da, das steht so ähnlich sogar [in der
Doku](http://docs.ansible.com/ansible/playbooks_lookups.html): *"Since 1.9 you
can pass wantlist=True to lookups to use in jinja2 template "for"* loops." Ja,
unter anderem brauche ich Listen, damit ich in jinja2 loopen kann.

Danke für die Info.
