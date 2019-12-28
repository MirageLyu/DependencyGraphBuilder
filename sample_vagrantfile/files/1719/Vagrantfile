#e -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"
VAGRANTFILE_LOCAL = 'Vagrantfile.local'

$script = <<SCRIPT
sudo apt-get update && sudo apt-get install -y python2.7 python-pip python-dev git libffi-dev libssl-dev
sudo pip install 'setuptools>=18.5' 'ansible>=2.1'
cd /vagrant
export CSIRTG_TOKEN=$1
export CSIRTG_FEED=$2
export CSIRTG_USER=$3
export ZYRE_GROUP=$4
export ZSYS_INTERFACE=$5
bash bootstrap.sh
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provision "shell" do |s|
    s.inline = $script
    s.args = [
        ENV['CSIRTG_TOKEN'],
        ENV['CSIRTG_FEED'],
        ENV['CSIRTG_USER']
    ]
  end
  config.vm.box = 'ubuntu/xenial64'

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--cpus", "2", "--ioapic", "on", "--memory", "1024" ]
  end

  config.vm.network 'public_network'

  if File.file?(VAGRANTFILE_LOCAL)
    external = File.read VAGRANTFILE_LOCAL
    eval external
  end
end
