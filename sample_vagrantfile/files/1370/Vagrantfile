# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |vconfig|
    vconfig.vm.box = "trusty32"
    vconfig.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"

    vconfig.vm.define :broadsign do |config|
        config.vm.provider :virtualbox do |v|
        #internet
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
            v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
            # set memory to > 1GB
            v.customize [ "modifyvm", :id, "--memory", "2100" ]
            # maybe this will help Windows hosts with symlinks
            v.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/vagrant", "1"]
        end
        config.vm.host_name = "broadsign.vagrant"

        # set lavish permission so that everything is executable
        #

        config.vm.synced_folder "./", "/vagrant", :mount_options => ['dmode=777', 'fmode=666'] #, :nfs=>true

        config.vm.network :private_network, ip: "192.168.16.17"

        # forward to port 8888
        config.vm.network "forwarded_port", guest: 80, host: 8888

        config.vm.provision :shell, :path => "ansible/provision.sh"
    end
end
