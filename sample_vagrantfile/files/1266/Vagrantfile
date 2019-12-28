# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.insert_key = false

  config.vm.define "debian7" do |debian7|
    debian7.vm.box = "chef/debian-7.7"
    debian7.vm.network "forwarded_port", guest: 80, host: 8080
  end

  config.vm.define "centos6" do |centos6|
    centos6.vm.box = "chef/centos-6.6"
    centos6.vm.network "forwarded_port", guest: 80, host: 8180
  end

  config.vm.define "centos7" do |centos7|
    centos7.vm.box = "chef/centos-7.0"
    centos7.vm.network "forwarded_port", guest: 80, host: 8280
  end

  config.vm.define "ubuntu_trusty" do |ubuntu_trusty|
    ubuntu_trusty.vm.box = "ubuntu/trusty64"
    ubuntu_trusty.vm.network "forwarded_port", guest: 80, host: 8380
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "role.yml"
    # The following definitions are used for the auto generated
    # inventory:
    # http://docs.vagrantup.com/v2/provisioning/ansible.html
    ansible.verbose = "vvvv"
    ansible.groups = {
      "debian" => ["debian7"],
      "centos" => ["centos6", "centos7"],
      "ubuntu" => ["ubuntu_trusty"],
      "all_groups:children" => ["debian", "ubuntu", "centos"]
    }
  end
end

