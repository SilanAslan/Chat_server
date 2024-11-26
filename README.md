# Chatt med Sockets - Individuell Uppgift Programmering 2

## Beskrivning
Detta projekt är den individuella examinationsuppgiften för kursen Programmering 2. Uppgiften går ut på att skapa ett chattprogram som använder Python-modulen socket för att implementera en klient-server-modell för kommunikation mellan flera användare.

## Uppgiftskrav
### Krav för Godkänt (G)
- Upprättar en fungerande UDP- eller TCP-kommunikation mellan minst två parter.
- Alla parter kan skicka och ta emot data i textformat.
- Programmet är väl dokumenterat och kommenterat.
- Korrekt felhantering är implementerad.

### Krav för Väl Godkänt (VG)
- Implementerar en chatt-server som klienter kan ansluta till (client-server model).
- Chat-servern hanterar meddelanden från alla klienter och skickar ut meddelanden till alla anslutna klienter.

## Implementerade funktioner
- TCP-baserad kommunikation mellan server och flera klienter.
- Möjlighet för användare att välja egna användarnamn.
- Realtids-meddelandehantering och distribution till alla anslutna klienter.
- Välkomstmeddelande med ASCII-konst för nya användare.
- Felhantering för oväntade frånkopplingar och andra fel.

## Tekniska detaljer
- Använder Python 3.x
- Utnyttjar inbyggda moduler: socket och threading
- Implementerar en broadcast-funktion för meddelandedistribution
- Hanterar samtidiga klientanslutningar med hjälp av trådar

## Projektstruktur
- `server.py`: Serverlogik för hantering av klientanslutningar och meddelandedistribution.
- `client.py`: Klientlogik för anslutning till servern, samt sändning och mottagning av meddelanden.

## Användning
1. Starta servern:
python server.py
2. Starta en eller flera klienter i separata terminalfönster:
python client.py
3. Följ instruktionerna i klientprogrammet för att välja användarnamn och börja chatta.

## Utvecklare
Silan Aslan

## Noteringar
Detta projekt är utvecklat som en individuell examinationsuppgift för kursen Programmering 2 och demonstrerar förståelse för nätverksprogrammering och socketkommunikation i Python.
