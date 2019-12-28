# -*- mode: ruby -*-
# vi: set ft=ruby :


module OS
    def OS.windows?
        (/cygwin|mswin|mingw|bccwin|wince|emx/ =~ RUBY_PLATFORM) != nil
    end

    def OS.mac?
        (/darwin/ =~ RUBY_PLATFORM) != nil
    end

    def OS.unix?
        !OS.windows?
    end

    def OS.linux?
        OS.unix? and not OS.mac?
    end
end


# All Vagrant configuration is done below. The '2' in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

    if !Vagrant.has_plugin?('vagrant-proxyconf')
        system('vagrant plugin install vagrant-proxyconf')
        raise('vagrant-proxyconf installed. Run command again.');
    end
    if !Vagrant.has_plugin?('vagrant-env')
        system('vagrant plugin install vagrant-env')
        raise('vagrant-env installed. Run command again.');
    end
    if !Vagrant.has_plugin?('vagrant-vbguest')
        system('vagrant plugin install vagrant-vbguest')
        raise('vagrant-vbguest installed. Run command again.');
    end
    if !Vagrant.has_plugin?('vagrant-hosts')
        system('vagrant plugin install vagrant-hosts')
        raise('vagrant-hosts installed. Run command again.');
    end

    #if Vagrant.has_plugin?('vagrant-proxyconf') && Vagrant.has_plugin?('vagrant-env')
    #    config.env.enable
    #    trigram = ENV['TRIGRAM']
    #    password = ENV['PASSWORD']
    #    config.proxy.http     = 'http://' + trigram + ':' + password + '@10.6.7.50:8080'
    #    config.proxy.https     = 'http://' + trigram + ':' + password + '@10.6.7.50:8080'
    #end

    config.vm.box = 'centos/7'

    # Define the machine

    config.vm.define 'developer' do |node|

        node.vm.provider 'virtualbox' do |vb|
            vb.memory = '1025'
            vb.cpus = 2
        end

        node.vm.hostname = 'localhost'
        node.vm.provision 'shell' do |s|
            s.path = './bootstrap.sh'
            s.privileged = false
            s.binary = true
        end
        if OS.windows?
            puts 'Host OS is Windows'
            node.vm.synced_folder '.', '/vagrant'
        else
            node.vm.synced_folder '.', '/vagrant', type: 'nfs'
            # node.vm.synced_folder ".", "/vagrant", type: "rsync", rsync__exclude: ".git/"
        end

        node.vm.network :private_network, :ip => '10.0.1.191'
        node.vm.network 'forwarded_port', guest: 3000, host: 2021
        node.vm.network 'forwarded_port', guest: 3001, host: 2022

    end

end
