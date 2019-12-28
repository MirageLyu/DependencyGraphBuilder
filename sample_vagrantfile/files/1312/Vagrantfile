# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  
  config.vm.box = "bento/centos-7.1"
  config.vm.box_check_update = false
  config.ssh.insert_key = false

  config.vm.define "centos7" do |centos7|
    centos7.vm.hostname = "centos7"
    centos7.vm.network "forwarded_port", guest: 22, host: 2200, id: "ssh"
    centos7.vm.network "forwarded_port", guest: 8080, host: 8080
    centos7.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 2
    end
  end

end
