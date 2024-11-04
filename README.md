# Django

# Introduction:
```
4 type of request. Generally. called CRUD operation. (Create, Read, Update, Database)
1. Get (For get anything. Read operation)
2. Post (For create. Create operation)
3. Update (For edit anything. Update operation)
4. Delete (For delete anything. Delete operation)
```

# Create virtual environment for python in ubuntu:

```txt
sudo apt install -y python3-venv
```
```
cd environments
```
```
python3 -m venv my_env
```
```
ls my_env
```
```
source my_env/bin/activate
```
```
Issue for ubuntu while installing PyAutoGUI package (N.B. check pyautogui after every command):
```
```txt
echo Display
```
```txt
xhost +SI:localuser:$(whoami)
```
```txt
xhost +local:$(whoami)
```
```txt
sudo apt-get install xvfb
```
```txt
xvfb-run python /home/workstation/Desktop/Test/Project/TestPython/test.py
```
```txt
pip uninstall pyautogui mouseinfo
```
```txt
pip install pyautogui
```

# Django install:

```txt
pip install django
```

`For see current version:`
```txt
django-admin --version
```
`For specific version:`
```txt
pip install django==version
```
`For all package list in pip`
```txt
pip list
```