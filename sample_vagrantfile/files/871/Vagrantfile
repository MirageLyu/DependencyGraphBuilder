# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
    end

    config.vm.network "forwarded_port", guest: 80, host: 58080
    config.vm.network "forwarded_port", guest: 443, host: 5443

    config.vm.network :private_network, ip: "192.168.100.10"

    config.vm.synced_folder "../src", "/home/vagrant/src"

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/playbook.yml"
        ansible.inventory_path = "ansible/inventories/dev"
        ansible.limit = 'all'
    end

end
