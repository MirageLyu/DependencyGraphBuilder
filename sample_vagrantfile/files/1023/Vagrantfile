# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise32"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "mailpile.yml"
  end
  config.vm.network :forwarded_port, guest: 33411, host: 33411
end
