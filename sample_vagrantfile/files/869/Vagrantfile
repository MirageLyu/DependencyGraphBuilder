Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "mezu"
  config.vm.network "private_network", ip: "192.168.27.14"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "_vagrant/playbook.yml"
  end

  config.ssh.forward_agent = true
  config.ssh.insert_key = false

end
