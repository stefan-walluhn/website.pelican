Title: DNS, hosts und splitbrains
Date: 2016-09-27 12:43
Tags: DNS, hosts, splitbrain
Slug: dns-splitbrains

Gerade aus einer überlangen Nacht zurück. Verqueres Setup, interne
OAuth2-Provider und schlechter Code und ganz plötzlich geht auf einer
mittelgroßen Seite mit mehreren tausend Besuchern in der Stunde der
Login-Prozess nicht mehr.

Nach mehreren Stunden stellt sich raus, dass die Erbauer des Setups ganz clever
sein wollten und die öffentlichen Domains auf internen Systemen via
/etc/hosts-File auf interne IPs umgebogen haben, diese dann auf einem anderen
nginx einschlagen und dort das SSL-Setup kaputt war. Ganz großes Kino.

Ich will das hier noch einmal in aller Deutlichkeit anbringen:

**NEVER EVER OVERWRITE DNS-Records!!!** Nein! Niemals! Nicht mit einem
internen DNS-Server! Nicht durch /etc/hosts- Einträge! Nicht durch
Ansible-Akrobatik! Nie!

Wenn ihr intern ein anderes Routing braucht, dann macht das explizit! Setzt
eine interne DNS-Zone auf und bringt eurer Software bei, intern andere
Endpoints zu benutzen als extern. Alles andere ist fies-versteckter Zustand und
bricht euch das Bein, wenn ihr am wenigsten damit rechnet.

Ein oft gesehenes Problem im Zusammenhang mit DNS und externen IP-Adressen sind
auch Firewalls auf Gateways. Ihr löst von innen eine öffentliche Domain auf
(www.example.com), bekommt eure externe IP zurück und versucht nun, von einer
internen IP auf ein möglicherweise per NAT durchgeschliffenes externes
Netzwerk-Interface zuzugreifen. Viele Firewalls machen hier dicht, weil z.B.
das NAT nicht greift von innen. Gern genutzte Lösung: innen den DNS-Record
umschreiben. Nope! Nicht machen! Besser die Firewall sauber konfigurieren und
mit einer extra Regel den Zugriff auf die externe IP auch von innen
konfigurieren.
