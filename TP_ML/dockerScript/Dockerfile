FROM ubuntu

COPY . /

Run apt-get -y update							&& \
		apt-get -y install python3				&& \
		apt-get -y install python3-pip			&& \
		apt-get -y install vim					&& \
		apt-get -y install git					&& \
		apt-get -y install firefox				&& \
		wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -								&& \
		apt-get install apt-transport-https																				&& \
		echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list 	&& \
		apt-get install sublime-text 																					&& \
		python3 -m pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["jupyter-notebook", "--allow-root"]