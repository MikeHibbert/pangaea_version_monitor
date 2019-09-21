echo "Installing version monitoring dependencies ..."
sudo apt-get install supervisor python-pip
pip install --yes boto3 arrow

echo "Installing configuration files ..."
mkdir `pwd`/logs
echo "from settings import *\n">> `pwd`/pangaea_version_monitor/local_settings.py
echo "BASE_DIR = '`pwd`'" >> `pwd`/pangaea_version_monitor/local_settings.py
sudo sed 's?BASE_PATH?'`pwd`'?' "`pwd`/pangaea_version_monitor/conf/pangaea_version_monitor.conf" > /etc/supervisor/conf.d/pangaea_version_monitor.conf
sudo sed 's?BASE_PATH?'`pwd`'?' "`pwd`/pangaea_version_monitor/conf/pangaea_node.conf" > /etc/supervisor/conf.d/pangaea_node.conf

sudo supervisorctl reload