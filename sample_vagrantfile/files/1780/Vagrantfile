# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # puppetlabs has some pretty nice boxes and I needed a CentOS6 box anyway.
  config.vm.box      = 'puppetlabs/centos-6.6-64-puppet'
  config.vm.box_url  = 'https://atlas.hashicorp.com/puppetlabs/boxes/centos-6.6-64-puppet'
  
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.synced_folder "data", "/vagrant_data"

  # I want a 2 cpu, 1024MB machine
  config.vm.provider "virtualbox" do |vb|
     # Display the VirtualBox GUI when booting the machine root is root/puppet
     vb.gui = true
     vb.cpus = 2
     # Customize the amount of memory on the VM. Don't forget the WLS and SOA Suite running under this
     vb.memory = "4098"
  end
   
  #I couldn't help myself... just had to use puppet for some simple things
  #By default this will look for puppet manifests in the um, manifests folder.
  config.vm.provision "puppet"
  
  #I'm yum'ing in the desktop but better would be to start with a box that already has it installed.
  #But then to find that box... and a trusted source.
  config.vm.provision "shell", path: "data/shell/setup.sh"
    
end
