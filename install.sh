sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user

# Git
sudo yum install git -y

# no need to install python already

# install pip
sudo yum -y install python-pip
mkdir venv
cd venv

# start virtual env
# python3 -m venv db-test-venv

# source db-test-venv/bin/activate
# git clone project-name (url)
# cd project-name/
# pip install -r requirements.txt