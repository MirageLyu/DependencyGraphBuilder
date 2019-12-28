# Vagant-dev-box

# Minimum Vagrant version required
Vagrant.require_version ">= 1.6.4"

Vagrant.configure("2") do |config|
  config.vm.box = "debian/jessie64"
  config.vm.box_url = "https://atlas.hashicorp.com/debian/boxes/jessie64/versions/8.7.0/providers/virtualbox.box"
  config.vm.hostname = "pg.box"
  config.vm.network :private_network, ip: "192.168.6.6"
  config.vm.network "forwarded_port", guest: 80, host: 8888, auto_correct: true
  config.vm.network "forwarded_port", guest: 22, host: 2020, auto_correct: true
  config.vm.synced_folder "~/Documents/workspace", "/var/www", type: "nfs"

  config.vm.provider :virtualbox do |v|
    v.name = "pg-debian-box"
    v.customize [
      "modifyvm", :id,
      "--name", "pg-debian-box",
      "--cpuexecutioncap", "50",
      "--memory", "512",
      "--natdnshostresolver1", "on",
      "--cpus", 1,
    ]
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "ansible/playbook.yml"
    #ansible.verbose = "vv"
  end

end
