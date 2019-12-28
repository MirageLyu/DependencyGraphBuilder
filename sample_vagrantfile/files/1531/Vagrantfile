$PROJECT_NAME = "waterpark"

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.synced_folder ".", "/home/vagrant/" + $PROJECT_NAME
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end

  config.vm.provision "shell", inline: <<-SHELL
    cd ~
    echo Initial Provisioning......
    echo Add git-core
    sudo add-apt-repository ppa:git-core/ppa  > /dev/null
    echo update module
    sudo apt-get update  > /dev/null
    echo install module
    sudo apt-get install -y vim g++ git-core curl make > /dev/null
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    echo Install rust......
    curl https://sh.rustup.rs -sSf | sh -s -- -y
    export PATH="~/.cargo/bin:$PATH"
    export RUST_BACKTRACE="1"
  SHELL

  config.vm.provision "shell", privileged: false, run: "always", inline: <<-SHELL
    export PATH="~/.cargo/bin:$PATH"
    export RUST_BACKTRACE="1"
  SHELL
end
