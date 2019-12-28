# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = 'chef/debian-7.4'

    config.vm.network :forwarded_port, guest: 80, host: 8080

    config.ssh.forward_agent = true

    config.vm.provider :virtualbox do |vb|
      # Use VBoxManage to customize the VM. For example to change memory:
      vb.customize ['modifyvm', :id, '--memory', '1024']
    end

    config.omnibus.chef_version = :latest
    config.vm.provision :chef_solo do |chef|
        chef.cookbooks_path = ['chef-repo/cookbooks', 'chef-repo/site-cookbooks']
        chef.run_list = %w(
            recipe[apt]
            recipe[build-essential]
            recipe[debian]
            recipe[vim]
            recipe[tmux]
            recipe[zsh]
            recipe[docker]
            recipe[custom]
        )

        chef.json = {
            debian: {
                mirror: 'http://cdn.debian.net/debian',
            },
            zsh: {
                install_method: 'source',
            },
            vim: {
                install_method: 'source',
            },
            tmux: {
                install_method: 'source',
            },
        }
    end
end
