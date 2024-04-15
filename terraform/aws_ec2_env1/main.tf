# Configure the AWS Provider
provider "aws" {
  region  = "us-east-1"
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
}

#STEPS
#1/2. create EC2 master-key
#1. create vpc: a custom pc for the environment
#2. create internet gateway: to send traffic outside with public ip
#3. create custom route table:
#4. create a subnet: where webserver will live
#5. associate subnet with route table: anytime subnet gets created it's assigned a route table
#6. create security group: to allow port 22,80,443
#7. create a network interface: with an ip in the subnet that was created in step 4
#8. assign an elastic IP to the network interface created in step 7 (public routeable)
#9. create Ubuntu server and install/enable apache2


#1/2. create EC2 master-key 
#1. create vpc | need a custom vpc
#vpc resource
resource "aws_vpc" "prod-vpc" {
  cidr_block = "10.0.0.0/16"
    tags = {
    Name = "production"
  }
}

#2. create internet gateway | to send traffic to outside with public ip, so anyone can reach it
resource "aws_internet_gateway" "gw" {
  #reference prod-vpc's id
  vpc_id = aws_vpc.prod-vpc.id

  tags = {
    Name = "main"
  }
}

#3. create custom route table
resource "aws_route_table" "prod-route-table" {
  vpc_id = aws_vpc.prod-vpc.id

  route {
    cidr_block = "0.0.0.0/0" #default route, send all traffic to the internet gateway
    gateway_id = aws_internet_gateway.gw.id
  }

  route {
    ipv6_cidr_block        = "::/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "prod route table "
  }
}

#4. create a subnet | subnet where webserver will live
resource "aws_subnet" "subnet-1" {
    vpc_id = aws_vpc.prod-vpc.id
    #cidr_block is equal to the custom subnet_prefix variable
    #cidr_block = "10.0.1.0/24"
    cidr_block = var.subnet_prefix[0] #reference first value in terraform.tfvariable
    availability_zone = "us-east-1a"

    tags = {
    Name = "prod-subnet "
  }
}

##dev subnet
resource "aws_subnet" "subnet-2" {
    vpc_id = aws_vpc.prod-vpc.id
    cidr_block = var.subnet_prefix[1]
    availability_zone = "us-east-1a"

    tags = {
    Name = "dev-subnet "
  }
}

#5. associate subnet with route table | anytime subnet gets created it's best to assign a route table
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.prod-route-table.id
}

#6. create security group to allow port 22,80,443 | setup what type of traffic is allowed 
resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow Web inbound traffic"
  vpc_id      = aws_vpc.prod-vpc.id

  ingress {
    description      = "HTTPS from VPC"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"] #any ip adress can access it
  }

    ingress {
    description      = "HTTP from VPC"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"] #any ip adress can access it
  }

    ingress {
    description      = "SSH from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"] #any ip adress can access it
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

#7. create a network interface with an ip in the subnet that was created in step 4
resource "aws_network_interface" "web-server-nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow_web.id]
}

#8. assign an elastic IP to the network interface created in step 7 | elastic ip/public ip routeable outside
resource "aws_eip" "one" {
  vpc                       = true
  network_interface         = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [aws_internet_gateway.gw]
}

#output entry to record assigned public ip of elastic ip
output "server_public_ip" {
  value = aws_eip.one.public_ip
}

#9. create Ubuntu serber and install/enable apache2
#compute resource type
resource "aws_instance" "my_web_server" {
  ami           = "ami-0b0dcb5067f052a63"
  instance_type = "t2.micro"
  availability_zone = "us-east-1a"
  key_name = "master_key"

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.web-server-nic.id
  }
  #bash script to install apache & run it
  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install apache2 -y
              sudo systemctl start apache2
              sudo bash -c 'echo verification message > /var/www/html/index.html'
              EOF

  tags = {
    Name = "web_server"
  }
}