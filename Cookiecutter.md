# Cookiecutter Quick‑Start Guide

> **Use this file as the canonical instructions for generating a new project from the `python-package-template`.**
>
> It lives in the root of the template so users see it immediately after cloning or opening the repo on GitHub.

---

## 1  Prerequisites

| Requirement  | Version | Notes                                                                 |
| ------------ | ------- | --------------------------------------------------------------------- |
| Python       | ≥ 3.9   | Needed only on the machine running Cookiecutter, not on your template |
| pip          | latest  | `python -m pip install --upgrade pip`                                 |
| Cookiecutter | latest  | Install once: `python -m pip install --upgrade cookiecutter`          |

---

## 2  Generate a New Package

### Option A Use the GitHub URL (recommended)

```bash
cookiecutter gh:{{ cookiecutter.github_user }}/python-package-template
```

*If the repo is private, ensure you have a PAT with **`repo`** scope or set* `GITHUB_TOKEN` *env var.*

### Option B From a Local Clone

```bash
cookiecutter /path/to/python-package-template
```

Cookiecutter will prompt you for values defined in `cookiecutter.json`:

```
project_name [Awesome Package]:
package_slug [awesome_package]:
distribution_slug [awesome-package]:
github_user [your-github]:
author_name [Your Name]:
author_email [you@example.com]:
license:
  1 - MIT
  2 - Apache-2.0
  3 - BSD-3-Clause
Choose license [1]:
python_min_version [3.9]:
description [A short description of the project.]:
```

After answering, a **new folder** matching `distribution_slug` is created with fully customized code, tests, and CI.

---

## 3  Next Steps in Your New Project

```bash
cd <distribution_slug>
python -m pip install -e ".[dev]"   # install optional dev deps (pytest, ruff, etc.)
pytest                               # run starter tests

# Initialize version control
git init
git add .
git commit -m "Bootstrap from python-package-template"

# Push to GitHub (replace remote URL)
git remote add origin git@github.com:<github_user>/<distribution_slug>.git
git push -u origin main

# First release -> triggers GitHub Actions to build & publish
git tag v0.1.0
git push --tags
```

*The provided `publish.yml` workflow uploads the package to GitHub Packages automatically.*

---

## 4  Updating the Template in an Existing Project

Once a project is generated, it is **decoupled** from future template changes. To pull in updates you can:

1. Manually cherry‑pick commits from the template repo, **or**
2. Use tools like [`cruft`](https://github.com/cruft/cruft) to track and re‑apply template changes.

---

## 5  Common Customizations

| Task                                       | Where to change                                                                         |
| ------------------------------------------ | --------------------------------------------------------------------------------------- |
| Add runtime dependencies                   | `pyproject.toml` → `[project].dependencies`                                             |
| Change license                             | Regenerate OR replace `LICENSE` file                                                    |
| Add CLI entry‑points                       | `pyproject.toml` → `[project.scripts]`                                                  |
| Enable `setuptools-scm` versioning         | Remove `_version.py` and set `[project.version] = "0.0.0"` plus `[tool.setuptools_scm]` |
| Publish to PyPI in addition to GH Packages | Extend `.github/workflows/publish.yml` with a PyPI twine step                           |

---

## 6  FAQ

<details>
<summary>❓ Why can’t I just <code>pip install</code> the template?</summary>

Templates are blueprints intended to be **rendered** into a fresh copy that you modify. Installing the template itself would give you its code, not your customized package.

</details>

<details>
<summary>❓ Can I skip some prompts?</summary>

Supply defaults via command‑line flags, e.g.:

```bash
cookiecutter gh:{{ cookiecutter.github_user }}/python-package-template \
  --no-input \
  project_name="MyLib" package_slug="mylib" distribution_slug="my-lib" \
  github_user="me" author_name="Me" author_email="me@example.com"
```

</details>

---

### Happy templating! 🚀
