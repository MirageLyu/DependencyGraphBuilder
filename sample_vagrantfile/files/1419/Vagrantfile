# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure('2') do |config|
  config.vm.box      = 'ubuntu/trusty64'
  config.vm.hostname = 'rails-dev-box'
  config.vm.provision :shell, path: 'bootstrap.sh', keep_color: true

  config.vm.network "private_network", type: "dhcp"

  ## '~' mean it will add all your directory of current user. Feel free for modify
  config.vm.synced_folder "~", "/vagrant", :nfs => true
end