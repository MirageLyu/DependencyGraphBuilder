# -*- mode: ruby -*-
# vi: set ft=ruby :

# Make sure to be using the vagrant-vbguest plugin

Vagrant.configure("2") do |config|

  config.vm.define "centos7" do |centos7|
    centos7.vbguest.auto_update = false
    centos7.vm.box       = "centos/7"
    centos7.vm.host_name = "centos7.sovrin.lab"
    centos7.vm.network "public_network"
    centos7.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
    centos7.ssh.insert_key       = false
    centos7.vm.provider "virtualbox" do |vb|
      vb.name   = "centos7"
      vb.gui    = false
      vb.memory = "1024"
      vb.cpus   = "1"
    end
    centos7.vm.provision "packages", type: "shell", path: "scripts/centos7_packages.sh"
    centos7.vm.provision "sovrin",   type: "shell", path: "scripts/centos7_sovrin.sh"
  end

  config.vm.define "precise" do |precise|
    precise.vm.box       = "hashicorp/precise64"
    precise.vm.host_name = "precise.sovrin.lab"
    precise.vm.network "public_network"
    precise.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
    precise.ssh.insert_key       = false
    precise.vm.provider "virtualbox" do |vb|
      vb.name   = "precise"
      vb.gui    = false
      vb.memory = "1024"
      vb.cpus   = "1"
      vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
    end
    precise.vm.provision "packages", type: "shell", path: "scripts/precise_packages.sh"
    precise.vm.provision "sovrin",   type: "shell", path: "scripts/precise_sovrin.sh"
  end

  config.vm.define "trusty" do |trusty|
    trusty.vm.box       = "ubuntu/trusty64"
    trusty.vm.host_name = "trusty.sovrin.lab"
    trusty.vm.network "public_network"
    trusty.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
    trusty.ssh.insert_key       = false
    trusty.vm.provider "virtualbox" do |vb|
      vb.name   = "trusty"
      vb.gui    = false
      vb.memory = "1024"
      vb.cpus   = "1"
      vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
    end
    trusty.vm.provision "packages", type: "shell", path: "scripts/trusty_packages.sh"
    trusty.vm.provision "sovrin",   type: "shell", path: "scripts/trusty_sovrin.sh"
  end

  config.vm.define "xenial" do |xenial|
    xenial.vm.box       = "boxcutter/ubuntu1604"
    xenial.vm.host_name = "xenial.sovrin.lab"
    xenial.vm.network "private_network", ip: "10.42.111.101"
    xenial.vm.network "public_network"
    xenial.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
    xenial.ssh.insert_key       = false
    xenial.vm.provider "virtualbox" do |vb|
      vb.name   = "xenial"
      vb.gui    = false
      vb.memory = "1024"
      vb.cpus   = "1"
      vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
    end
    xenial.vm.provision "packages", type: "shell", path: "scripts/xenial_packages.sh"
    xenial.vm.provision "sovrin",   type: "shell", path: "scripts/xenial_sovrin.sh"
  end

end
