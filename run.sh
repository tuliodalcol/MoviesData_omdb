echo 'Creating environment...'
python3 -m venv env
echo 'Activating Environment...'
. env/bin/activate
echo 'Installing packages...'
pip3 install --upgrade pip
pip3 install -r requirements.txt
echo 'Pachages Installed!!!'
