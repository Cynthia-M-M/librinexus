
# ⚡ LibriNexus Enterprise

[![Frappe Version](https://img.shields.io/badge/Frappe-v15-blue?style=flat-square&logo=frappe)]( https://unodoriferous-rosario-unspeared.ngrok-free.dev)
[![Live Demo](https://img.shields.io/badge/Demo-Live%20App-success?style=flat-square&logo=google-chrome&logoColor=white)]( https://unodoriferous-rosario-unspeared.ngrok-free.dev)
[![UI](https://img.shields.io/badge/UI-Tailwind%20CSS-38bdf8?style=flat-square&logo=tailwindcss)](https://tailwindcss.com)
[![License](https://img.shields.io/badge/License-MIT-gray?style=flat-square)]()

**An advanced Library Management System & Digital Storefront.**
Built for the **Stelden Skillset Showcase**, this application merges a robust Librarian Backend with a modern, consumer-facing E-Commerce Frontend.

---

## 🟢 Live Demo
**Click here to test the application:**
### [🔗 Launch LibriNexus Live]( https://unodoriferous-rosario-unspeared.ngrok-free.dev)
*(Hosted on ngrok)*

---

## 🚀 Key Features

### 🛒 The "Storefront" Experience (Frontend)
Unlike standard library apps, LibriNexus offers a "Netflix-style" discovery experience for members.

| Feature | Tech Detail |
| :--- | :--- |
| **🛍️ Guest Cart System** | Custom JavaScript implementation using `LocalStorage` for persistent shopping sessions without login. |
| **📲 WhatsApp Checkout** | "Click-to-Order" integration that pre-fills message templates for instant mobile transactions. |
| **🔎 Real-Time Search** | Dynamic filtering by Category (Tech, Fiction) and Title with optimized SQL queries. |
| **🎨 Responsive UI** | Built with **Tailwind CSS** & **Jinja2** templating for a pixel-perfect mobile & desktop experience. |

### 🧠 The "Brain" (Backend Logic)
Automation and validation logic built strictly on the Frappe Framework.

| Feature | Tech Detail |
| :--- | :--- |
| **⛔ Debt Validation** | Python Controller hooks prevent issuing books if member debt exceeds **KES 500**. |
| **🔗 Google Books API** | (Experimental) Auto-fetch book metadata using ISBN to reduce manual entry. |
| **📊 SQL Reporting** | Custom Script Reports for "High Value Inventory" using concise SQL joins. |
| **🛡️ Role Management** | Strict permissions separating the Librarian Desk from the Public Store. |

---

## 🛠️ Installation

*(Standard Frappe Bench Installation)*

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app [https://github.com/Cynthia-M-M/librinexus](https://github.com/Cynthia-M-M/librinexus) --branch version-16
bench install-app librinexus

```

## 🤝 Contributing & Standards

This app follows strict Frappe coding standards using `pre-commit` for formatting and linting.

```bash
cd apps/librinexus
pre-commit install

```

**Tools used:**

* `Ruff` (Python Linting)
* `Prettier` (JS/HTML Formatting)
* `ESLint` (JS Quality)

## ⚙️ CI / CD

This app uses GitHub Actions for Continuous Integration:

* **CI:** Runs unit tests on every push.
* **Linters:** Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) for security.

---

### License

MIT

```

```
