# Cerca semàntica en directe — Camps Industrials 2

Petit script educatiu fet per **W3Barcelona** per al Bloc 2 (Infraestructura
Cloud i Vector DBs) del Camp Industrials 2. Fa servir **ChromaDB**, una base
de dades vectorial real, gratuïta i sense servidor, per mostrar en directe
com funciona la cerca semàntica.

## Instal·lació

```bash
pip install -r requirements.txt
```

## ⚠️ Important: executa'l un cop ABANS de la sessió

La primera vegada que s'executa, ChromaDB descarrega un model d'embeddings
petit (~80 MB, un sol cop) per poder convertir les frases en vectors.
Necessita internet per a aquesta primera descàrrega. Un cop fet, torna a
funcionar sense connexió.

**Recomanació:** executa `python cerca_semantica.py` (i tanca'l amb
`sortir`) abans de la classe, perquè la descàrrega no consumeixi temps ni
dependeixi del WiFi de l'aula en directe.

## Ús

```bash
python cerca_semantica.py
```

El script indexa 12 frases sobre temes ben diferents (mascotes, cuina,
sensors IoT, seguretat, meteorologia, vehicles) i et deixa escriure
preguntes en directe. Per cada pregunta, mostra les 3 frases més properes
**per significat**, amb la seva puntuació de similitud cosinus (de -1 a 1,
tal com vam veure al Bloc 1).

Escriu `sortir` per acabar.

## Preguntes suggerides per provar a classe

- "Com cuido una mascota?" → hauria de recuperar les frases del gat i el gos
- "Com protegeixo les meves dades?" → hauria de recuperar xifratge i contrasenyes
- "Quin temps farà demà?" → hauria de recuperar pluja i vent
- Prova alguna pregunta que NO faci servir cap paraula exacta de les frases
  originals — és el millor moment per remarcar que és cerca per significat,
  no per coincidència de paraules

## Context

Aquest script acompanya la comparativa de bases de dades vectorials
(Pinecone, pgvector, Weaviate, Qdrant) del Bloc 2, i la diapositiva de
similitud cosinus del Bloc 1 — connecta la teoria amb una demo real i
tangible.
