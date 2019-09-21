echo "Installing version monitoring dependencies ..."
pip install --yes boto3 arrow
sudo apt-get install supervisor

echo "Installing configuration files ..."
echo "BASE_DIR = '`pwd`'" >> `pwd`/pangaea_version_monitor/local_settings.py
sudo sed 's?BASE_PATH?'`pwd`'?' "`pwd`/pangaea_version_monitor/conf/pangaea_version_monitor.conf" > /etc/supervisor/conf.d/pangaea_version_monitor.conf

sudo supervisorctrl reload