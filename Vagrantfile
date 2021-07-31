Vagrant.configure(2) do |config|

  config.vm.provision "shell", path: "bootstrap.sh"

  # Load Balancer Node
  config.vm.define "my-consul" do |lb|
    lb.vm.box = "ubuntu/xenial64"
    lb.vm.hostname = "consul.exersize.com"
    lb.vm.network "private_network", ip: "172.16.16.20"
    lb.vm.provider "virtualbox" do |v|
      v.name = "my-consul"
      v.memory = 1024
      v.cpus = 1
    end
  end
end