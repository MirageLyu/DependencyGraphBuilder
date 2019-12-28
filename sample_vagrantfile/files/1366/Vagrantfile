# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"

    config.vm.network :forwarded_port, guest: 80,   host: 8080
    #config.vm.network :forwarded_port, guest: 22,   host: 2222
    #config.vm.network :forwarded_port, guest: 10000,   host: 10000
    #config.vm.network :forwarded_port, guest: 5000, host: 5000
    config.vm.network :forwarded_port, guest: 8000, host: 8000
    config.vm.network :forwarded_port, guest: 8080, host: 8888
    #config.vm.network :forwarded_port, guest: 8082, host: 8082
    #config.vm.network :forwarded_port, guest: 8773, host: 8773
    #config.vm.network :forwarded_port, guest: 8983, host: 8983
    config.vm.network :forwarded_port, guest: 9000, host: 9000
    #config.vm.network :forwarded_port, guest: 3000, host: 3000
    #config.vm.network :forwarded_port, guest: 9999, host: 9999
    config.vm.network :forwarded_port, guest: 27017, host: 27777
    #config.vm.network :forwarded_port, guest: 3301, host: 3331

    # Share an additional folder to the guest VM. The first argument is
    # an identifier, the second is the path on the guest to mount the
    # folder, and the third is the path on the host to the actual folder.
    config.vm.synced_folder "../vdata", "/vagrant_data"
    #config.vm.synced_folder "../vlinks/MEDIAREPO", "/mnt/MEDIAREPO"

    # # Add to /etc/hosts: 33.33.33.24 dev.example.com
    # config.vm.network :hostonly, "33.33.33.24"

    # provision with simple shell script
    config.vm.provision "shell", path: "install_requirements.sh"
end
