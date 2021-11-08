# 1.__Dustin.py

  pip:
  ```
   sudo apt-get install python3-pip
  ```
  ```
   python3 -m pip install — upgrade pip
  ```
  
  virtualenv:
  ```
   sudo pip3 install virtualenv
  ```
  
1. **Requirements**

---

`Python 3.9.6 (lastest version)`


2. Install python venv
---
   windows:
   ```
   $ python -m venv .venv
   ```
   Linux: (specify the version of python)
   ```
   $ python3.9 -m venv .venv
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
   ```
   source myenv/bin/activate
   ```
   
4. Install pip-tools in venv
---
   ```
    python -m pip install pip-tools
   ```
   
5. Compile Developement dependencies
---
   ```
    pip-compile dev-requirements.in
   ```
   ```
    pip-compile requirements.in
   ```
   
6. Install dependencies
---
   ```
    pip-sync dev-requirements.txt requirements.txt
   ```
