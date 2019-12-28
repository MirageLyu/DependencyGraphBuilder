#!/usr/bin/env ruby

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hellocode/ruby-devenv64"
  config.vm.network :forwarded_port, host: 3030, guest: 3000

  # removing system version of ruby
  config.vm.provision :shell,
    :inline => "sudo apt-get remove ruby -y && sudo apt-get autoremove -y"

 # install ruby and perform initial project setup
  config.vm.provision :shell do |sh|
    sh.privileged = false
    sh.path = "bootstrap.sh"
  end
end
