Vagrant.configure(2) do |config|

#WEATHER1
 config.vm.define "weather1" do |weather1|
   weather1.vm.hostname = "weather1"
   weather1.vm.box = "ubuntu/xenial64"
   weather1.vm.box_check_update = false
   weather1.vm.network "private_network", ip: "192.168.99.13", dns: "8.8.8.8"
   weather1.vm.provision "file", source: "./", destination: "$HOME/challenge"
   weather1.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get install python-pip -y
     pip install pip
     pip install flask --upgrade
     pip install requests --upgrade
     pip install requests_cache --upgrade
     pip install prometheus-flask-exporter
     pip install flask_prometheus
   SHELL

   config.vm.provider "virtualbox" do |weather1|
     weather1.memory = "512"
   end
 end


#WEATHER2
 config.vm.define "weather2" do |weather2|
   weather2.vm.hostname = "weather2"
   weather2.vm.box = "ubuntu/xenial64"
   weather2.vm.box_check_update = false
   weather2.vm.network "private_network", ip: "192.168.99.14", dns: "8.8.8.8"
   weather2.vm.provision "file", source: "./", destination: "$HOME/challenge"
   weather2.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get install python-pip -y
     pip install pip
     pip install flask --upgrade
     pip install requests --upgrade
     pip install requests_cache --upgrade
     pip install prometheus-flask-exporter
     pip install flask_prometheus
   SHELL

   config.vm.provider "virtualbox" do |weather2|
     weather2.memory = "512"
   end
 end

#NGINX
 config.vm.define "nginx" do |nginx|
   nginx.vm.hostname= "nginx"
   nginx.vm.box = "ubuntu/xenial64"
   nginx.vm.box_check_update = false
   nginx.vm.network "private_network", ip: "192.168.99.12", dns: "8.8.8.8"
   nginx.vm.provision "file", source: "./", destination: "$HOME/challenge"
   nginx.vm.provision "shell", inline: <<-SHELL
     apt-add-repository ppa:ansible/ansible -y
     apt-get update
     apt-get install software-properties-common ansible -y
     apt-get install python-jmespath -y
     apt-get install nginx -y
     echo "[defaults]
host_key_checking = False
remote_user = root" > /etc/ansible/ansible.cfg
   echo "[local]
127.0.0.1" > /etc/ansible/hosts
   sudo cp /home/vagrant/challenge/monit/monitoracao.yml /etc/ansible
   sudo ansible-playbook /etc/ansible/monitoracao.yml --connection=local
   SHELL
 
   config.vm.provider "virtualbox" do |nginx|
     nginx.memory = "1024"
   end
 end



#JENKINS
 config.vm.define "jenkins" do |jenkins|
   jenkins.vm.hostname = "jenkins"
   jenkins.vm.box = "ubuntu/xenial64"
   jenkins.vm.box_check_update = false
   jenkins.vm.network "private_network", ip: "192.168.99.16", dns: "8.8.8.8"
   jenkins.vm.provision "file", source: "./", destination: "$HOME/challenge"
   jenkins.vm.provision "shell", inline: <<-SHELL
     apt-get update
   SHELL

   config.vm.provider "virtualbox" do |jenkins|
     jenkins.memory = "512"
   end
 end




end
