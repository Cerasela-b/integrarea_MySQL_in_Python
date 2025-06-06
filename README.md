# integrarea_MySQL_in_Python

Task 6 - Raport analiză date


1. Descrierea datelor

Datele analizate provin dintr-o bază de date MySQL și includ informații despre filme, genurile acestora și bugetele alocate. Relația dintre filme și genuri este de tip many-to-many, gestionată prin tabela intermediară 'genremovie'.

Tabele implicate:
- movie(id_movie, title, budget, etc.)
- genre(genre_id, name_genre)
- genremovie(movie_id, genre_id)

2. Scopul analizei

Scopul principal a fost să determinăm bugetul mediu al filmelor pe gen și să reprezentăm grafic aceste informații pentru a identifica eventuale diferențe semnificative între genuri.

3. Etape parcurse

- Conectarea la baza de date și extragerea datelor relevante (gen și buget)
- Gruparea datelor după gen și calcularea bugetului mediu
- Afișarea statisticilor descriptive generale pentru buget
- Crearea unui bar chart cu bugetul mediu al filmelor pe gen

4. Concluzii cheie

- Genurile de filme au bugete medii semnificativ diferite.
- Cele mai ridicate bugete medii apar la genurile de tip acțiune și SF, ceea ce indică o producție mai costisitoare.
- Genurile precum comedie sau dramă au în general bugete mai modeste.
- Nu au fost detectate erori majore în date, dar unele filme aveau buget nul sau lipsă, care au fost eliminate din analiză.

5. Recomandări

- Pentru analize viitoare, se recomandă includerea și a încasărilor (box_office) pentru o comparație între buget și profit.
- Se poate adăuga o analiză temporală pentru a observa cum au evoluat bugetele în timp pe fiecare gen.
