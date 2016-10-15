Title: Server-Panik
Date: 2016-02-08
Tags: server, panik, fsck

Mein Server ist heute abgeschmiert. RAM alle. Kommt vor. Dabei ist irgendwie
das Dateisystem nach read-only gekippt. Kommt auch vor. Neustarten hilft, denke
ich mir. SSH auf die Kiste, reboot.

5 Minuten später bekomme ich eine E-Mail von meinem Provider:

>Details zu dieser Operation:
>
>Filesystem manual check
>Date 2016-02-08 18:19:35, **** made Filesystem manual check:
> Here are the details of the performed operation:
> The server has completed a file system check  (fsck)
> The server was blocked when checking files with the message:
> (Ctrl-D to continue...)
>
> Actions:
> "ctrl+d" done
>
> Result:
> Login to server. Ping OK, services started.

Ich so: Äh, whoooooooot?

Antwort an den Provider per Mail: Spannende Reaktion, nen FS-Check zu killen.
Ja, der Server ist online, aber...

```
[8.020835] EXT4-fs (sda1): warning: mounting fs with errors, running e2fsck is recommended
```

Echt jetzt? Ist das euer Ernst, den erwarteten FS-Check nach nem Reboot zu
killen und damit ggf. den Server wirklich zu grillen?

Gerade kommt die Antwort rein:

> Can you give me result of:
> smartctl -a -d ata /dev/sda
> in order to check the disk?

Ist das die berühmte Kernel-Panic, von der immer alle reden? Alle rasten aus
und rennen wild im Kreis? Hab die Kiste jetzt nochmal durchgestartet. Mal
sehen, ob am Ende des Tages die Festplatte noch drin ist...
