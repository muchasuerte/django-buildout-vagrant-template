# Template for django + zc.buildout + vagrant

## Start:

- install vagrant [link](http://www.vagrantup.com/)  
- add a vagrantbox:  

		vagrant box add precise64 precise-server-cloudimg-amd64-vagrant-disk1.box  

- install that plugin for virtualbox guest plugin auto update:  

		vagrant plugin install vagrant-vbguest  

- get a copy of that project [download](archive/master.zip)  
- customize the buildout files into the buildout dir
- run  

		vagrant up  

## Info:
Vagrant provision will run:

	 ./manager.sh vagrant-init  

Vagrant is configured to forward that ports:

- nginx: 8080  
- supervisor: 9080  

Tested on kubuntu 12.04.4 LTS


## Commands from the guest
	vagrant ssh
	cd /vagrant/

##### Reload buildout configuration
	./manager.sh update 

##### start/stop supervisord
	./manager.sh supervisor start|stop|restart
