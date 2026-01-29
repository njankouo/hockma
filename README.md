# 🇨🇦 Hockma Prep - Plateforme de Réussite IRCC 2026

![Status](https://img.shields.io/badge/Status-Live-emerald?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.2.0_Update_2026-red?style=for-the-badge)
![UI](https://img.shields.io/badge/Design-Tailwind_CSS_3.4-blue?style=for-the-badge)

**Hockma Prep** est une interface de vente haut de gamme conçue pour les candidats à l'immigration canadienne. Ce module de tarification (Pricing Section) est optimisé pour maximiser la conversion des programmes de préparation aux tests **TEF, TCF et EE**.

---

## ✨ Points Forts du Design

* **Psychologie des prix :** Mise en avant du "Pack Émeraude" (Best-seller) pour créer un ancrage visuel immédiat.
* **Design Moderne :** Utilisation du *Glassmorphism*, d'ombres portées diffuses et de bordures arrondies ($40px$) pour un aspect "App Mobile" premium.
* **Accessibilité & Clarté :** Hiérarchie visuelle stricte permettant de comparer les offres en moins de 3 secondes.
* **Badges de Confiance :** Mentions "Mise à jour IRCC 2026" et "Garantie Admis ou Remboursé" pour lever les freins à l'achat.

---

## 🛠️ Stack Technique

* **HTML5** : Structure sémantique.
* **Tailwind CSS** : Framework utilitaire pour un design responsive et ultra-rapide.
* **FontAwesome 6** : Iconographie professionnelle pour la liste des fonctionnalités.
* **Google Fonts** : Typographies robustes pour une lisibilité optimale.

---

## 📦 Structure du Projet

```text
├── Section #packs (Wrapper principal)
│   ├── Background Glows (Effets de lumière flous)
│   ├── Section Header (Titre + Badge de mise à jour)
│   ├── Pricing Grid (Grille adaptative 1/2/4 colonnes)
│   │   ├── Card Quartz (Entrée de gamme)
│   │   ├── Card Émeraude (Focus conversion - Élevée)
│   │   ├── Card Diamant (Haut de gamme)
│   │   └── Card Élite (Service sur-mesure / Coaching)
│   └── Secondary CTA (Bandeau "Plus de packs" dynamique)
