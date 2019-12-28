# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.vm.box = "centos"

  config.vm.define "edeploy" do |edeploy|
    edeploy.vm.hostname = "edeploy.test.enovance.com"

    edeploy.vm.synced_folder ".", "/vagrant", type: "rsync"
    edeploy.vm.provision "shell", inline: "service iptables stop"

    edeploy.vm.provision "puppet" do |puppet|
      puppet.synced_folder_type = 'rsync'
      puppet.module_path = 'modules'
      puppet.hiera_config_path = 'hiera.yaml'
    end

    #edeploy.vm.network :public_network, :bridge => "wlp3s0", :mac => "52:54:00:f9:7f:52"
    #edeploy.vm.network :public_network, ip: "192.168.121.34" , :mac => "525400f97f52"
  end

end
