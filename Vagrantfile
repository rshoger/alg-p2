Vagrant.configure("2") do |config|
  # select a box
  config.vm.box = "bento/ubuntu-16.04"

  # sync cwd to /vagrant on guest
  config.vm.synced_folder '.', '/vagrant', id: 'vagrant-root'

  # run some provisioning
  config.vm.provision :shell, inline: <<-SHELL
    locale-gen en_US.UTF-8
    update-locale LANG=en_US.UTF-8 \
                  LANGUAGE=en_US.UTF-8 \
                  LC_CTYPE=en_US.UTF-8 \
                  LC_ALL=en_US.UTF-8

    apt-get update

    apt-get install -y vim
    apt-get install -y python3 python3-setuptools
    easy_install3 pip
    pip install tox
  SHELL
end
