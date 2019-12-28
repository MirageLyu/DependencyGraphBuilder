# Vim
# vim: set filetype=ruby:
# vim: set ft=ruby:
#
# Emacs
# -*- mode: ruby; -*-

VAGRANTFILE_API_VERSION = "2"
MAX_MEMORY = 2048
SHOW_GUI = true

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Vagrant box to build on
#    config.vm.box = "ubuntu/trusty64"
    config.vm.box = "drmyersii/ubuntu-desktop-14.04-x64"

    # settings for VirtualBox provider
    config.vm.provider "virtualbox" do |v|
        v.memory = MAX_MEMORY
        v.gui = SHOW_GUI
        v.customize ["modifyvm", :id, "--memory", "2048"]
        v.customize ["modifyvm", :id, "--cpus", "2"]
#        v.customize ["modifyvm", :id, "--graphicscontroller", "vboxvga"]
        v.customize ["modifyvm", :id, "--accelerate3d", "on"]
        v.customize ["modifyvm", :id, "--ioapic", "on"]
        v.customize ["modifyvm", :id, "--vram", "128"]
        v.customize ["modifyvm", :id, "--hwvirtex", "on"]

    end

    # call provisioner
    config.vm.provision :shell, inline: "cd /vagrant && ./provision.sh", privileged: false
end
