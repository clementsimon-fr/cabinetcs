# cabinetcs.fr

Site du Cabinet CS (Clément Simon, coach professionnel), publié avec GitHub Pages.

## Structure

- `/` accueil
- `/accompagnements/` vue d'ensemble, puis `individuel/`, `equipe/`, `dirigeants/`
- `/a-propos/`, `/contact/`, `/mentions-legales/`
- `assets/` : `site.css`, `site.js`, police Inter (hébergée localement), logo, portrait, illustrations
- `entreprises/…` et `mentions-legales.html` : redirections des anciennes adresses

## Modifier le site

Les pages HTML sont générées par `_build/pages.py` (contenu) et `_build/sitelib.py`
(en-tête, menu, pied de page, composants). Après modification :

    cd _build && python3 pages.py

Le dossier `_build` commence par « _ », il n'est donc pas publié par GitHub Pages.
