sudo systemctl stop mysistem_check_container.service
sudo systemctl disable mysistem_check_container.service

sudo mkdir -p /usr/share/mysistem
sudo cp -rf environment /usr/share/mysistem
sudo cp -rf logs /usr/share/mysistem
sudo cp -rf scripts /usr/share/mysistem
sudo cp -rf services/* /etc/systemd/system

sudo systemctl daemon-reload
sudo systemctl enable mysistem_check_container.service
sudo systemctl start mysistem_check_container.service
