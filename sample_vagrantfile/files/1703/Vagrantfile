# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  #config.vm.box = "debian-8.7.1-amd64_virtualbox.box"
  config.vm.box = "debian/contrib-jessie64"
  config.vm.hostname = "vagrantJenkins"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  #config.vm.network "forwarded_port", guest: 8080, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"
  # damit kann ich die vm immer unter dieser ip erreichen.  
  config.vm.network "private_network", ip: "192.168.143.11"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  #config.vm.synced_folder "/jenkins", "/var/lib/jenkins"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
    vb.memory = "8192"
    vb.cpus = 2
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # legt den in trusted.gpg, das liegt jetzt im repo 
  # den kopiert der vagrant user. also erstmal ins home 
   config.vm.provision "file", source: "trusted.gpg", destination: "/home/vagrant/trusted.gpg"
   config.vm.provision "file", source: ".bashrc", destination: "/home/vagrant/.bashrc"

  # und nun chown und move
  # add user ssh key and group docker
   
  config.vm.provision "shell", inline: <<-SHELL
    chown root.root /home/vagrant/trusted.gpg  
	mv /home/vagrant/trusted.gpg /etc/apt
	echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEA23JoT2jalthYUyn3K4xkikX6b0V+EEqauPFJVrm6nodDxkvO1WCCbFQ6HKIrVREj7AwMZODl7vrAmgAUbB7kkxNzTlXuZCBkxbuQJgd026miyG/AQXHTDi+e7zKiY6zSERGK8AGYNKbGh8MkBWvrYIHUycBHQXqAnvMcVvYhBhyNwW9dqWecsIaC+rW3F//VcGfBAfD+YGkn+23ZWJt7FMiGOz1+4Bmcd5WryBLtVEpmS65034Y6QWLGLkF0W0S2S6GkxwBrZ2cqQPGv2LbjeWbBjUbXnXFDXDqmNY7RTAptlWnedogtxo79v3lBjUaOdfq1/JGMKfi5Ek0DpQkEzw== wbrune@nicos-ag.com">>/home/vagrant/.ssh/authorized_keys
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAABAEAk/RUrFn25RMpzPH9kwoVA984gRBdFZiXQFF1B2Y0PkrXtaBnqS+ZxcPBe7+4UnTXG5/nfLuEjDlRONANGCvHMaPHXiElWzIF2c20x8PjsLLjix0MqjA1ilFeWpCyss0mGqXaH2BxR7tArQhul9bA0qS3KhfTqwZph34TOo19hdr9flDwuwj91Rm4VGlzTSu0gouM2yXcaJXdqg+HaXFoFS65sq5KsuU2jHmpOsy25iTsO4CXqbPgd4WLvo7A5P0Abp17DlNlAPlNl4HcBwV0kgDtwdWNQhauM3UKM0jvIMlub3bLlAUhvISPlZFacr2cN/sZA0zQR2NO1n5kpYzh6VmEjCvEEGtAQ2LZGzuWVVdsimjrGNi7H3SUBMBkk0ZOspKP7Ng3thMTQxM9Qm5sCgYzxnomvejmsSvgQzBglQfa8xCBcP3GnYQz9B9/etA1GDP8W2wcs1EcVfP+89WC92gN6+KzkaO9W0N09VIwqy8H+lCWnvC6uWLXvNalGaRtuXlfRQxxsIzkz/2yhvSNdHeDm17lvHRbYs/lcHrQB0uR9IJlV0lZo1BGkMWbe7Tlnv7dKBDimasUxakniqiJdR0q0VU0g8UhHH4UXRIIwqP9YCFYPz2RcziOYHYr8WPbVMAAene1JUmiz2gTxowQlRNP61DJKyIm9zD0zH0jU72kCTIhGPd4zAaCaQyXsZIPO6JZ90gw4kgCfHvexEk1kpfLyy8QL9RgRgAQeXxxICK1J3eJmWPCeNkW4Ro1GzEZAuLlBrdEGYsN3bRrtROCWHqqhyp6Y2R0A51kt4QSCjmz6j3t4VGxLxwDlCkwmmqmOnIJce/8/YyyLw+KjTeOOYlI261/1AYbiS8IqPZO4/M9j6/VBhFyU/t5Sc7GBoBM5/oD60PmhxG8mU7lSjrSfNtTFUgbqjPvDgPYI+z1kHwsA77BeP90OluJxydJvQmJa7TS4xVCe8v8w3eB5ISUffoTdC2nsCPP21xGFV8DoUBd1gzVxG3sI5myz+QGv87QL2E05bsxfQPgNSlVG+v/z/eI7I7Dx0X5TZIeFvzGlyGux8vG/kehEpdFjiCanSqcNJP5fe12C7Il4mpaWo5j/cAMJ/fioDK9ldZPJ5K7dThUhzhNvoem2DYX71ArUV+iJxkp16pXkncHjknKL9XGGGYt/Xcw8TXtpfXZDT0m6hi8exY8qJode7CudQcS6h+9duNA9IK4H96NxJdRqyFS499I1kjy3l+/u9fGb8AHvVH85ndQT2gtut0Gc3+X7ej6snAI6NL/yQEEerOCUHvtZiMpP6aAlm/jS1IpTNTVAVdYt2DYKr6keyTA7C7VVB5kPZ6FTn/DDUuqZTIOzDtydQ== hdilling@nicos-ag.com">>/home/vagrant/.ssh/authorized_keys
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDjDqBlWo8cbaoPFcyda69140wc3W/bXH6uy+Ba5ihZ5QxSCryDYDXBDqMJowYuLLGpYZk0QH8yrdSxHjh/0Hk9aec2f9+Gg0j+xRTQ8zVsz8G2DFeFroZLhbc2/REvLsIHEB3x1isICh8JBFRVKcbJ/g5D7pyAC95DuSFZ3+OJkMzHn19TiIipuXS0wahKwOG3jWUwaE2UaVgNZVxq2D/WNgKSDyX05U2gw2ea6or4UuRYCTZNtmoD5m2XoMWQamrpNhURAk96zV4PP0nL/iYBPlFoH42oVIOfJ1K1TqWxpCH8y8H7prLwV0JW02GJBVIBqDJdBGxV/7sfroMeiUsD jenkins@jenkins01">>/home/vagrant/.ssh/authorized_keys
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAABQEAjovgg43SWE1y9u0GWO3Z1A3SJtCoCiqWS2h95ewvw53T/7EAABZOdTGhLm3BxCkgYWBi0/XiMzJf/9jER9DYoGSQpLrQjt7L627P2hd0sSEYQt6puSobwi3RHhqnTOCLBLCs7DBWutHaaVhQnIHgYQXb6oNYwc3Y4MB0XbZUgm7zAX40LTi1W3vkvZSOfiYg/rZr0mStXHAaLRYpxmjruWXg/BwHxe31bnz7OAxFRSPEXRC8VdTHQUSrhJHyzSokxjRJncaXIAwLgfs+nRhuOk9ZoK7KusxpSTTRcn2Z8asr1Ez68em6j0RRChh0sC8BM1ZNeeK5jxxPK3XVDit1VTBuGFgo+Nma8jBsB33pKzijhlMFsBO+tPlLiyYKVyY/xC8cTkaZsa8h9CHVW9/eZqitTSoblkysJqjxyqCTMxyncZvm6g7NR0TcxOYqCSOhlnsdk2BqS7zWoWDC/R49YQ5ZwMnuGaCkHCqS8MDbRmiLRXyuipyOsgLhkGnoWu4Iu7a7VKgEK+NYy+iti2iA6hT/cKQlR8VwWXYjNUf/ymANaFJwDmxq83BmV5S7Dl66fAao7PYniqcF3I7ldh+0GYZhzWbSucNiem5Dz/o+gyaaV/kuWuTUwr9iSvdiok7r43d3SeGAG3oJzTnLo76F4amwggwF2BDRdRcFbREFgQA3rDIht0n0bcUjjs2jfY3UFPzHoAAaokE9GuO1aTo+1eYkgvGDBTHGvrP6JEe9BnUW/od7/Lf/A8zLGHaUotkYxYyE5n7rx8DPFRXHWPjEDYdn201Lf6q2SVMPA6oa3+YpCOWUz1VkqMpc8dhOCRHcm3+rHooBPqCMMJsBMKPKSPdw8+ZaiSKMqLrlWn+clmMwcSKv9NH6b+HpwgNJAt9wzEEZx45dTDeDqvt8nnRFELPpvWEqhZZEg+7/kgCwJQQ3xtgKbGrgaGKDueaSgE1hn4IRsR2YHbl6jH/Za6iu//29InNsfObbxQ3dgUPrJd9VuXgKH/gwjhMz428mnBXxFe07H2bWFpGON5bTNOr1Vthxobm88QxHHk4v3gES8WwZeQTStWZaqyD7nNOh8/E2KVfgczproPW2srPZfXlmpCmoyAl2NjcBMzMVB1roC+1GHJNa1t1lwGI3KxIXToPlqUM8cjolEUrleBWowa2Ip6T7wIYyHJCRLiabQKNFs58ynpAIymDTwuf0+KWkvKtXl8yBIRxoqo70P9uHLhKFyp4q+2Tm7DL3nqjppFeY1KoECODjvJygc+cJkIrIduj5+UFBcUMy/LQcLWkRyxyvO2mtvb9hxe0TVj5MiWpD/EfHiazR8tPfHtArDJ/mpTv+or9AaIwgfnkHJX7D/j1J/6NmCDXfcQG/2/F3FuM/sel5i/UBYwpIILqy0NuNKPuFY+WybmQhCfLcCgJYgPGvGW/z2NaG90M+4jByJ4C0L4gtAkA0p1XIsrahcms32BtTwJlR8jKSQ/NTsk0hmGnKIhRsatzoo32EOhUwxn0PKi/pW7pZlbF01X5AMHAHygNS4JjR0cn1xeadxEq4ybHx2IiqZhQhIJ5S5KzdNjM4uxWMeACGZJ0p4fwwgl8TEGMWHX6zVTsPh0EH2HrxvQA/2yi4Lx2fLzOpLlcXP/hr4vbz1iL/gWsV7iI+42kzpUOVFH9Ln4NlSw7zp2Oo/16njMO+9UI9j4QeDS/lB760SVc= jhelms jhelms@nicos-ag.com" >>/home/vagrant/.ssh/authorized_keys
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAFAQDQ/mQ5ENZrswlIaFI8snqKFG43SZnTSehfr0vPkt6IcWxvpF5z64EpgcG5n04BAeRNj5avicPEYxIswfmo8b9P5t7L5HumyiVrED/bM+ZES4wsran1nSXflosQUzWdHIENg1VQgAUcOQWeRPs7EAjPIJFgwv8fN4NkMUTZRKFxCmvNwIWs5s+a++R+uEHTAXP97Xn9+Mo4YY/VPRCbkCIJ9jwbOrnt/WcS4YLW3OFoVKsltTrtyOOSFiGLvQF+qihh6O2RBU4Qhi3gSELi8UoWIm5fUU9CLfYgqmQC+UKBjHdp2GQZpboBJcmjvLQcXjY6lSm+OvRXaNZ3Md/2J0mHpauDuW2tHySkvxqAK6vQygR/dG0L3WHrSJy66F+h3rU26bBknhMRvOMQTwi/gVUhvAgG9E0dsLz7fijXTf5wmSmV9Mdog9D30ThBpR5nSMBZuPNvdHIbBZRLVlSRVmXc21vT9xBITg9/lm387Q3bRAVlVYMjNLRKTMNJLsQ+g60RYBIzjtt34yzoyw5h8Cv3LlHTTxZjWB5faYPez07Dav9ft+io0vUbZpgfTNcUwVhQkEZJNyqlRsL9s9AkfELirwP1XVT4NLHkM1mVdHT9UDCqVHTdLGhBK84BuV4AvVyabXqp+7xBlNJ7ZzbSNC0sutmh6URJm5UgUCB/pujLw/IkBdD2L8ic9YQVTefYuNIapsSGYMKnBXKXftplQknrw224LEVQ7ThnBamwCRGjylfAGA22Q0I/pqtNba4cy4zkz7k3FiLmcryRg/GenSZ50YNeHhfU5J/8+BzioIFcif9gD75WeFWzub8HaWzKhBXL15nT7RXszpfGbe2hKwnPHzsX5CknwyxDwd9QGSPuGUCbDyZ6nzo4F293/+xxOTGV6dAyEFP8tA+3YPHH8EdR8EMQFT0MBDWYHW0nmhRFA6SvBwk/9J8Q9hvhnoHzOfqk33BrGcmsKD3GZjYWpJChjwTNxjPJ79suJX/q5n1nG9v9hJRUTURmAwSoMixjzaal9TTIi6AzKGQmCfwTWjLugW6CFfFuVV4KZVq/cbfx2ZEKwOrjcX94DUe6PKb6AMcgSTXg+5lUu8Qtvdxt4hkpkbTwVqMbcM5TWLCQ8IR2whuqTOrHcCkUfZQJ+KdnQYhZZalc6nE7CQ24Tiyk4DYlAM0hTNEL6g+/yleqHZh591IjetmdBxnwwidpl0h8G+QaPNcIz69+kHqnKBhIF9Er/Kt0pjvdlZtMVdtwPbuoGaBhsSh7/ANN7jgzugSlQO++mdMseTkg8RymDWYRXYa2bjOhqqu3IeS8vCnudaluR1mhIZklB7KLAqMQyEaD02miozgjKkR7pTJwycr3mZ6I2xG9WvFtmzZwBHLEqdvqzwsAcJESkRPafI2C3aZdFfARcSUEF13Pan+whjZVvQuWkZBgHFHM/gljd0AStSf1aUvVFZAoFqyZw7vJhBrnYMtqiDyeh8n8F6TS1Rgcu70vHJVFDCUAcT2C0k70JWjlWQhNeLrK8jaUT1xvh5H8iVzcY8V+RyQCfDBzPvACk6Lgg4L3Czwv/UoGRlUrSAAm2qGun/fe9YLr2oOAVlvbIwGq7zql/x9WOkwfhwTvKCaEQRWQMCXwgYkKm/dfnrFTI4+ngiJZGJfh7Q0Q4oApr8VEDWEpEwBOfwEguRnutF2cZ9OvtiLyMcqm3RvJwZKRiw== rbrinkmann@nicos-ag.com" >>/home/vagrant/.ssh/authorized_keys
    echo "ssh-dss AAAAB3NzaC1kc3MAAACBALT8ExyVc/ZhzNBI0eUvXo25EA9fSm9UQC6jsSZGN1sta990aqwH2cE6zyfuh0anDniCNwivprOzpCafY3pTMXnPsCdK0HMZARxx8LRHk2ZZYOrZSZQ3F2KI+jtVjKLQ5Q5D6Fbw4rTEqn3QYrlOJF4iyAOopdhltWyVvKMmqnWLAAAAFQDB0w5TzDLvifm8oE/ZfZNsquWABwAAAIEAiNxykGzS7PvVXigpowD+Yi6cyhNH7G6maSB/egZ2/bcDNrZcME5H062IEr3DmNgN0kCjaqT3fDz1BQPvL0o9b+T4joQP+YDkZ3D8FDcvB1NnerNIeZJwFF1lppn+qW2V9g1b+kZcUEunwRs4WXj7MgIOunheqb/Lo5JSaJX0dvcAAACARhfkYAqFMSI7GH6w+LQa2fOxsuDiBhB+KAWKwIE0FO68ec0k02akEt/ZuBU/0K/263p6KYd4fCMm8QF2XnXUm3Anu/1XKxqlaxEg7ckOswwcqW/t651LrfXMKvpkbarH6WkY7hxpx3qT/Dm0lKmE0gejHfU2uxAAjSg2g1PkdUg= tboesenberg@nicos-ag.com" >>/home/vagrant/.ssh/authorized_keys
	groupadd --gid 999 docker
	usermod -a -G docker vagrant
    apt-get update
	apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common \
    joe sudo curl 
    echo "deb [arch=amd64] https://download.docker.com/linux/debian jessie stable" > /etc/apt/sources.list.d/docker.list
  SHELL

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y docker-ce
  SHELL

  config.vm.provision "file", source: "docker.conf", destination: "/home/vagrant/docker.conf"
  config.vm.provision "file", source: "docker", destination: "/home/vagrant/docker"
  
  config.vm.provision "shell", inline: <<-SHELL
    echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
    mkdir /etc/systemd/system/docker.service.d
    chown root.root /home/vagrant/docker.conf
    mv /home/vagrant/docker.conf /etc/systemd/system/docker.service.d
    chown root.root /home/vagrant/docker
    mv /home/vagrant/docker /etc/default/
    systemctl daemon-reload
    service docker restart
    curl -L https://github.com/docker/compose/releases/download/1.14.0/docker-compose-`uname -s`-`uname -m`  -o /usr/local/bin/docker-compose &>/dev/null
    chmod a+x /usr/local/bin/docker-compose 	 
  SHELL
  
  config.ssh.insert_key = false 

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.

end
