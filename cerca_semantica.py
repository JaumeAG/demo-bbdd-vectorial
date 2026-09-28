"""
cerca_semantica.py
Camps Industrials 2 — Bloc 2: Infraestructura Cloud i Vector DBs
W3Barcelona

Petit script per demostrar EN DIRECTE com funciona una base de dades
vectorial: guarda un conjunt de frases, les converteix en embeddings,
i cerca en temps real les frases més semblants (per significat, no
per paraules exactes) a la pregunta que escriguis.

Fet servir ChromaDB: una base de dades vectorial real, gratuïta i
sense servidor — perfecta per a una demo a classe.
"""

import chromadb

FRASES = [
    "El gat dorm a la finestra tota la tarda.",
    "Els gossos necessiten sortir a passejar cada dia.",
    "La recepta porta tomàquet, all i oli d'oliva.",
    "Cal coure la pasta deu minuts en aigua bullint.",
    "El sensor de temperatura envia dades cada minut.",
    "El servidor MQTT rep les lectures del magatzem.",
    "Avui plourà a la tarda segons la previsió.",
    "El vent bufarà fort a partir de dimecres.",
    "Cal xifrar les dades sensibles abans de guardar-les.",
    "Mai posis una contrasenya directament al codi font.",
    "El cotxe elèctric es carrega en menys de mitja hora.",
    "La moto necessita una revisió cada 10.000 km.",
]


def crea_coleccio():
    """Crea (o reinicia) la col·lecció de la base de dades vectorial."""
    client = chromadb.Client()
    # hnsw:space "cosine" perquè la mètrica coincideixi amb la vista a classe
    coleccio = client.create_collection(
        name="frases_demo",
        metadata={"hnsw:space": "cosine"},
    )
    coleccio.add(
        documents=FRASES,
        ids=[f"frase_{i}" for i in range(len(FRASES))],
    )
    return coleccio


def cerca(coleccio, pregunta, n=3):
    """Cerca les n frases més semblants a la pregunta."""
    resultats = coleccio.query(query_texts=[pregunta], n_results=n)
    docs = resultats["documents"][0]
    distancies = resultats["distances"][0]
    return list(zip(docs, distancies))


def main():
    print("=" * 60)
    print(" Camps Industrials 2 — Cerca semàntica en directe")
    print(" W3Barcelona")
    print("=" * 60)

    print("\nIndexant frases (generant embeddings)...")
    coleccio = crea_coleccio()
    print(f"Fet. S'han indexat {len(FRASES)} frases.\n")

    print("Escriu una pregunta i veuràs les frases més properes per")
    print("SIGNIFICAT, no per paraules exactes. Escriu 'sortir' per acabar.\n")

    while True:
        pregunta = input("Pregunta: ").strip()
        if pregunta.lower() in ("sortir", "exit", "quit", ""):
            print("\nFins aviat!")
            break

        resultats = cerca(coleccio, pregunta)

        print(f"\nResultats per a: \"{pregunta}\"")
        print("-" * 60)
        for i, (doc, dist) in enumerate(resultats, start=1):
            similitud = 1 - dist
            print(f"  {i}. [similitud {similitud:.2f}]  {doc}")
        print()


if __name__ == "__main__":
    main()
