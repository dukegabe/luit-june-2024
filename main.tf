provider "aws" {
  region = "us-east-1"  # Replace with your desired region
}

data "aws_vpc" "default" {
  default = true
}

resource "aws_security_group" "terraform-sg1" {
  name = "terraform-sg1"
  description = "Allow inbound traffic for Jenkins"
  vpc_id = data.aws_vpc.default.id

  ingress {
    description = "Allow port 22"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow public access
  }

  ingress {
    description = "Allow port 8080"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow public access
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Jenkins Security Group"
    Purpose = "Terraform project number 1"
  }
}

resource "aws_s3_bucket" "terraform-project-bucket-1" {
  bucket = "terraform-project-bucket-7388-duke"
  
  tags = {
    Name = "terraform-project-bucket-1"
    Purpose = "Terraform Project number 1"
  }
}

resource "aws_instance" "TerraformProject1" {
  ami           = "ami-01816d07b1128cd2d"  # Amazon Linux 2 AMI (update based on region)
  instance_type = "t2.micro"               # Free tier eligible
  key_name      = "DockerKP"          # Replace with your key pair name
  vpc_security_group_ids     = [aws_security_group.terraform-sg1.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo
              sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io-2023.key
              sudo dnf upgrade -y
              sudo dnf install -y java-21-amazon-corretto
              sudo dnf install -y jenkins
              sudo systemctl enable jenkins
              sudo systemctl start jenkins
            EOF

  tags = {
    Name = "TerraformProject1"
  }
}