# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
echo I am provisioning...
PROVISIONED="/vagrant/.PROVISIONED";

if [[ -f $PROVISIONED ]]; then
  echo "Skipping provisioning";
  exit;
else
  echo "Provisioning";
fi

# neo4j install&config procedure
sudo wget -O - http://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
sudo echo 'deb http://debian.neo4j.org/repo stable/' | sudo tee --append /etc/apt/sources.list.d/neo4j.list
sudo apt-get update -y
sudo apt-get install -y  neo4j
sudo cp /vagrant/config-files/neo4j-server.properties /etc/neo4j/
sudo chown neo4j:adm /etc/neo4j/neo4j-server.properties
touch $PROVISIONED;
SCRIPT

Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/trusty64'
  config.vm.box_check_update = true
  config.vm.hostname = "neo4j"

  config.vm.network "forwarded_port", guest: 7480, host: 7480
  config.vm.network "forwarded_port", guest: 7443, host: 7443

  config.vm.provision 'shell', inline: $script

  # virtualbox definitions
  config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", 1024]
  end
end

