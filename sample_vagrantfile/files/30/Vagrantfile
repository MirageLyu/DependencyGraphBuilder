# -*- mode: ruby -*-
# vi: set ft=ruby :

$provision=<<SHELL
wget --no-check-certificate -O - https://raw.githubusercontent.com/norcams/omnibus-drop/master/omnibus-drop.sh | \
  bash -s -- -r http://folk.uio.no/beddari/puppet puppet 3.4.3-1
SHELL

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos65"
  config.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_centos-6.5_chef-provisionerless.box"
  config.vm.provision :shell, :inline => $provision
end
