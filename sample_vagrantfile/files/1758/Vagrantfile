# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    vb.customize ["modifyvm", :id, "--cpus", 4]
  end

  config.vm.provision :shell, :inline => "apt-get install curl build-essential bzip2 -y"
  #config.vm.provision :shell, :path => "build-rstudio", :args => "0.97.336"
end
