#Script to run the requirements for this project
#and to run the python code in background
pip3 install --no-cache-dir -r requirements.txt
echo Done pip
echo Starting Dice Roll Telegram Bot
python3 main.py 
echo Telegram handles are running.
