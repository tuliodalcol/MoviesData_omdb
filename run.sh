echo 'Creating environment...'
python3 -m venv env
echo 'Activating Environment...'
. env/bin/activate
echo 'Installing packages...'
pip3 install --upgrade pip
pip3 -q install -r requirements.txt
echo 'Pachages Installed!!!'
echo 'Run unittest'
python3 -m unittest tests/test_extract.py
