Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "setup-django.yml"
  end
end
