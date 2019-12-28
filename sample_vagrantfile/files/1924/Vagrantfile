# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|
    # For a complete reference, please see the online documentation at
    # https://docs.vagrantup.com.
  
    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://atlas.hashicorp.com/search.
    config.vm.box = "trusty64"
    config.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-12.04-amd64-vbox.box"
  
    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    config.vm.network "private_network", ip: "10.0.0.10"
  
    # ssh
    config.ssh.forward_agent = true
  
    # Share an additional folder to the guest VM. The first argument is
    # the path on the host to the actual folder. The second argument is
    # the path on the guest to mount the folder. And the optional third
    # argument is a set of non-required options.
    config.vm.synced_folder "../data", "/vagrant_data", type: 'nfs', create: true
  
    # Provider-specific configuration so you can fine-tune various
    # backing providers for Vagrant. These expose provider-specific options.
  
    config.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50", "--cpus", "1"]
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vb.memory = "1024"
    end
  
    #
    # Provisioner - Shell
    # 
    # config.vm.provision :shell, path: "vm_provision/shell/provision-ubuntu-12.04.sh"

    #
    # Provisioner - Salt
    #

    ## For masterless, mount your salt file root
    config.vm.synced_folder "vm_provision/saltstack/", "/srv/salt/"
    config.vm.synced_folder "vm_provision/saltstack/config/", "/etc/salt/minion.d/"

    config.vm.provision :salt do |salt|
        salt.minion_config = "vm_provision/saltstack/config/minion.conf"
        salt.run_highstate = true
        salt.install_type = "stable"
        salt.bootstrap_options = "-P"
        salt.verbose = true
    end

end
