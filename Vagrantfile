# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "chef/ubuntu-14.04"
  config.vm.hostname = "web2docker"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provision "shell", inline: <<-SHELL
    wget -qO- https://get.docker.com/ | sudo sh
    echo 'DOCKER_OPTS="-H unix:///var/run/docker.sock -H tcp://0.0.0.0:2376"' | sudo tee -a /etc/default/docker > /dev/null
    sudo service docker restart
    sudo usermod -aG docker vagrant
  SHELL
end
