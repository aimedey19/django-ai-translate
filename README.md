# 🌍 django-ai-translate

**AI-powered translation for Django `.po` files — effortless, fast, and customizable.**

`django-ai-translate` is a Django package that automates the translation of gettext `.po` files using AI. Ideal for multilingual web applications, it helps you manage and update translations with minimal manual effort.

---

## ✨ Features

* 🔁 **Batch Translation** with customizable batch size
* ⚡️ **Async Support** for fast and efficient translation
* 🧠 **Powered by AI** (OpenAI, Groq, etc.)
* 📁 Works with standard `.po` files
* 🛠️ CLI integration via Django management command
* 📦 Easy to install and integrate in Django projects

---

## 🚀 Installation

Using [`uv`](https://github.com/astral-sh/uv):

```bash
uv pip install django-ai-translate
```

Or with pip:

```bash
pip install django-ai-translate
```

---

## 🛠️ Usage

### Django Management Command

```bash
python manage.py translate_po -f <path-to-file.po> -l <target-language> -bs [--batch-size 100]
```

**Example:**

```bash
python manage.py translate_po -f locale/fr/LC_MESSAGES/django.po -l en -bs 100
```

This command will:

* Load the `.po` file
* Translate all untranslated entries using AI
* Save the translations in-place


---


## ⚙️ Django Configuration

In your Django `settings.py`, add the following to configure the translator:

```python
AI_TRANSLATOR =  {
    'ENGINE': '',  # e.g. 'groq', 'openai', 'anthropic', or 'together'. The package only support these four api for now.
    'API_KEY': '',  # Your API key
    'MODEL': '',  # e.g. 'gpt-4', 'llama-3-70b'
    'PROMPT_TEXT': "You are a web application translator. Don't ouput thinking. Don't add anything else than result. Translate the following text to "
}
```

---

## 📁 Project Structure

```bash
django_ai_translate/
├── __init__.py
├── translator.py
├── po_handler.py
├── settings.py
├── management/
│   └── commands/
│       └── translate_po.py
tests/
pyproject.toml
```

---

## 🙌 Contributing

Pull requests are welcome! If you’d like to contribute:

```bash
git clone https://github.com/aimedey19/django-ai-translate.git
cd django-ai-translate
uv sync
```

---

## Contributors
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## 📄 License

MIT License © Aime & Contributors

