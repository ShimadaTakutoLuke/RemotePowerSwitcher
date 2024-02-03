cp power_switcher_server.py /usr/local/bin
cp power_switcher_server.service /etc/systemd/system

systemctl daemon-reload

systemctl enable power_switcher_server.service
systemctl start power_switcher_server.service