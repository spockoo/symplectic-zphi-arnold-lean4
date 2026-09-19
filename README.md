# symplectic-zphi-arnold-lean4
Official repository for the formal Lean 4 certification and 100-dps symplectic integration of sub-Landauer computing on $\mathbb{Z}[\phi]^4$. Proves Arnold's iso-non-degeneracy ($\det U = -2E$) and Liouville volume conservation ($\det A_d^2 = 1$). DOI: 10.5281/zenodo.22845514
# Invariance Symplectique Unimodulaire sur $\mathbb{Z}[\phi]$ et Exemption de Landauer

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22845514.svg)](https://doi.org/10.5281/zenodo.22845514)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Auteur :** Tomy Verreault ([ORCID: 0009-0007-1990-5271](https://orcid.org/0009-0007-1990-5271))  
**Certifié formellement avec :** Lean 4 / Mathlib4  

---

## 📌 Résumé

Ce dépôt contient le code source LaTeX, la simulation haute précision (100 dps) et la certification formelle sous **Lean 4** démontrant l'exemption de la limite d'effacement de Landauer ($\Delta S_{\text{logique}} = 0$) sur le réseau quasicristallin $\mathbb{Z}[\phi]^4$.

### Piliers Théoriques & Preuves :
1. **Condition d'Iso-Non-Dégénérescence d'Arnold :** Preuve symbolique que $\det(U) = -2E \neq 0$ sur $\Sigma_E$.
2. **Rétro-Analyse Symplectique :** Intégration Störmer-Verlet à 100 décimales ($p_{\text{order}} \approx 2$, $\Delta E \approx 0.0046$).
3. **Certification Lean 4 :** Formalisation de $\det A_d^2 = 1$ et du plongement d'anneaux $\mathbb{Z}[\phi] \hookrightarrow \mathbb{R}$.

---

## 📁 Structure du Dépôt

- `paper/` : Fichier PDF et source LaTeX de l'article officiel.
- `lean4/` : Preuve formelle intégrale certifiée sans erreur sous Lean 4.
- `python/` : Script de diagnostic et d'intégration haute précision `mpmath`.

---

## 📖 Citation

Si vous utilisez ces travaux ou ce code dans vos recherches, merci de citer le dépôt Zenodo :

```bibtex
@article{verreault2026symplectic,
  author       = {Tomy Verreault},
  title        = {Fermeture Topologique, Iso-Non-Dégénérescence d'Arnold et Certification Formelle dans Lean 4 d'un Calculateur Symplectique Sp(2k, Z[phi])},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.22845514},
  url          = {[https://doi.org/10.5281/zenodo.22845514](https://doi.org/10.5281/zenodo.22845514)}
}
