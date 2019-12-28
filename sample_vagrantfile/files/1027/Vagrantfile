# -*- mode: ruby -*-
# vi: set ft=ruby :

# configure box
Vagrant.configure("2") do |config|
  
  # set build image
  config.vm.box = "precise64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.omnibus.chef_version = :latest

  config.vm.provision "chef_solo" do |chef|
    chef.add_recipe "cassandra"
    chef.add_recipe "docker"
  end
end
