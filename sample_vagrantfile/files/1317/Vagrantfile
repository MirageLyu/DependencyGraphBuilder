# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

Vagrant.require_version '>= 1.5.0'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

zero = 0
one = 1
two = 2

  (1..3).each do |i|
    config.vm.define "kafka#{i}" do |s|
      s.vm.hostname = "kafka#{i}"
      s.vm.network "private_network", ip: "10.40.3.#{4-i}0", netmask: "255.255.255.0"

      # Enabling the Berkshelf plugin. To enable this globally, add this configuration
      # option to your ~/.vagrant.d/Vagrantfile file
      config.berkshelf.enabled = true

      config.vm.provision :chef_solo do |chef|
        chef.json = {
          apache_kafka: {
            "broker.id" =>  "#{i}"
          },
          zookeeper: {
            config: {
              clientPort: 2181,
              dataDir: '/var/lib/zookeeper',
              tickTime: 2000,
              initLimit: 5,
              syncLimit: 2,
              maxClientCxns: 0,
              server: {
                "1" => '10.40.3.30:2888:3888',
                "2" => '10.40.3.20:2888:3888',
                "3" => '10.40.3.10:2888:3888'
              }
            }
          },
          mysql: {
            server_root_password: 'rootpass',
            server_debian_password: 'debpass',
            server_repl_password: 'replpass'
          }
        }

        chef.run_list = [
          'recipe[bitmonk_kafka::default]'
        ]
      end
    end
  end


  # Set the version of chef to install using the vagrant-omnibus plugin
  # NOTE: You will need to install the vagrant-omnibus plugin:
  #
  #   $ vagrant plugin install vagrant-omnibus
  #
  if Vagrant.has_plugin?("vagrant-omnibus")
    config.omnibus.chef_version = 'latest'
  end

  config.vm.box = 'chef/ubuntu-14.04'


  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end

end
