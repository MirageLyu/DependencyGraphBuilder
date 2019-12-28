# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos-7.0"
  config.vm.hostname = "dev-centos7.0"
  config.vm.network "private_network", ip: "192.168.33.30"
  config.ssh.forward_agent = true
  config.vm.synced_folder "../", "/vagrant"
  # config.vbguest.auto_update = false
  # config.vbguest.iso_path = "#{ENV['HOME']}/Downloads/VBoxGuestAdditions_4.3.16.iso"
  # config.vbguest.no_remote = true
  # config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/id_rsa.pub"
  # config.vm.provision "file", source: "~/.ssh/id_rsa", destination: "~/.ssh/id_rsa"

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.auto_detect = true
    config.cache.scope = :box
  end

  if Vagrant.has_plugin?("vagrant-omnibus")
    config.omnibus.cache_packages = true
    config.omnibus.chef_version = :latest
  end
  
  config.berkshelf.berksfile_path = "Berksfile"
  config.berkshelf.enabled = true

  config.vm.provision "chef_zero" do |chef|
    # Specify the local paths where Chef data is stored
    chef.cookbooks_path = "./cookbooks/"
    chef.roles_path = "./roles/"
    chef.data_bags_path = "./data_bags/"
    chef.environments_path = "./data_bags/"

    # Specify roles
    chef.add_role "base"
    chef.add_role "webserver"
    chef.add_role "build"
  end
end
