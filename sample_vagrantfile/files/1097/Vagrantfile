# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "base-ubuntu-trusty-server"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.provider :virtualbox do |vb|
    vb.gui = false
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
    ansible.host_key_checking = false
  end

  config.vm.define :elastic_0_90_13 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.109"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_0_90_13"
      end
  end

  config.vm.define :elastic_1_0_2 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.102"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_0_2"
      end
  end

  config.vm.define :elastic_1_0_3 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.103"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_0_3"
      end
  end

  config.vm.define :elastic_1_1_0 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.110"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_1_0"
      end
  end

  config.vm.define :elastic_1_1_1 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.111"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_1_1"
      end
  end

  config.vm.define :elastic_1_2_1 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.121"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_2_1"
      end
  end

  config.vm.define :elastic_1_2_2 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.122"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_2_2"
      end
  end

  config.vm.define :elastic_1_2_3 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.123"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_2_3"
      end
  end

  config.vm.define :elastic_1_3_0 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.130"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_0"
      end
  end

  config.vm.define :elastic_1_3_1 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.131"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_1"
      end
  end

  config.vm.define :elastic_1_3_2 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.132"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_2"
      end
  end

  config.vm.define :elastic_1_3_3 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.133"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_3"
      end
  end

  config.vm.define :elastic_1_3_4 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.134"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_4"
      end
  end

  config.vm.define :elastic_1_3_5 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.135"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_5"
      end
  end

  config.vm.define :elastic_1_3_6 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.136"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_6"
      end
  end

  config.vm.define :elastic_1_3_7 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.137"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_7"
      end
  end

  config.vm.define :elastic_1_3_8 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.138"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_8"
      end
  end

  config.vm.define :elastic_1_3_9 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.139"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_3_9"
      end
  end

  config.vm.define :elastic_1_4_0 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.140"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_4_0"
      end
  end

  config.vm.define :elastic_1_4_1 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.141"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_4_1"
      end
  end

  config.vm.define :elastic_1_4_2 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.142"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_4_2"
      end
  end

  config.vm.define :elastic_1_4_3 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.143"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_4_3"
      end
  end

  config.vm.define :elastic_1_4_4 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.144"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_4_4"
      end
  end

  config.vm.define :elastic_1_4_5 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.145"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_4_5"
      end
  end

  config.vm.define :elastic_1_5_0 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.150"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_5_0"
      end
  end

  config.vm.define :elastic_1_5_1 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.151"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_5_1"
      end
  end

  config.vm.define :elastic_1_5_2 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.152"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_5_2"
      end
  end

  config.vm.define :elastic_1_6_0 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.160"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_6_0"
      end
  end

  config.vm.define :elastic_1_6_1 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.161"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_6_1"
      end
  end

  config.vm.define :elastic_1_6_2 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.162"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_6_2"
      end
  end

  config.vm.define :elastic_1_7_0 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.170"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_7_0"
      end
  end

  config.vm.define :elastic_1_7_1 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.171"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_7_1"
      end
  end

  config.vm.define :elastic_1_7_2 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.172"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_7_2"
      end
  end

  config.vm.define :elastic_1_7_3 do |cfg|
      cfg.vm.network :private_network, ip: "192.168.33.173"
      cfg.vm.provider :virtualbox do |v|
          v.name = "elastic_1_7_3"
      end
  end

end
