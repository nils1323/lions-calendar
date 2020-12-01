# lions-calendar
zieht sich die Gewinnernummern des aktuellen Tages und vergleicht diese mit der eigenen Nummer.

## Installation
Nötigen Module installieren:
```pip install -r requirements.txt```

### Telegrambenachrichtigung
Beim ersten Start wird man nach den Daten für einen Bot gefragt. Dieses kann man damit machen oder man legt eine Datei user.conf in das gleiche Verzeichnis, nach folgendem Muster:
```
[Telegram]
token = "Bot_Token"
chat_id = "chat_id"
```
## Ausführung
``` python3 calendarcheck.py```
