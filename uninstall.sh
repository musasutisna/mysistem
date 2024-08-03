sudo systemctl stop mysistem_check_container.service
sudo systemctl disable mysistem_check_container.service

sudo rm -rf /usr/share/mysistem
sudo rm /etc/systemd/system/mysistem_check_container.service
