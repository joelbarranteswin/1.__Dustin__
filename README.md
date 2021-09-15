# 1.__Dustin.py

* my practice, my work and my studies

1. **Requirements**

---

`Python 3.9.6 (lastest version)`


2. Install python venv
---
   ```
   $ python -m venv .venv
   ```
3. Activate python env
---
   windows:

   ```
   $ .\.venv\Scripts\activate
   ```
   linux/macos/unix:

   ```bash
   $ ./.venv/bin/activate
   ```
4. Install pip-tools in venv
   ```
    python -m pip install pip-tools
   ```
5. Compile Developement dependencies
   ```
    pip-compile dev-requirements.in
   ```
   ```
    pip-compile requirements.in
   ```
6. Install dependencies
   ```
    pip-sync dev-requirements.txt requirements.txt
   ```