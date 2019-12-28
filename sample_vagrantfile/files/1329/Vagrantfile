# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "autodemodrew" do |autodemodrew|

    autodemodrew.vm.box = "hashicorp/precise64"

	autodemodrew.vm.network :forwarded_port, guest: 80, host: 8080

	autodemodrew.vm.provision "file", source: "files/tornado.conf", destination: "tornado.conf"
	autodemodrew.vm.provision "file", source: "files/webserver.py", destination: "webserver.py"

    autodemodrew.vm.provision :ansible do |ansible|
      ansible.playbook = "playbook.yml"
      ansible.verbose  = true
    end

  end

end
