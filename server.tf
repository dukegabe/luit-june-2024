resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = var.public_subnet_cidrs[count.index]
  map_public_ip_on_launch = true
  availability_zone = data.aws_availability_zones.available.names[count.index]
  tags = {
    Name = "public-subnet-${count.index + 1}"
  }
}

resource "aws_subnet" "private" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = var.private_subnet_cidrs[count.index]
  availability_zone = data.aws_availability_zones.available.names[count.index]
  tags = {
    Name = "private-subnet-${count.index + 1}"
  }
}

resource "aws_instance" "DukeWebSever" {
  count = 2
  ami = "ami-01816d07b1128cd2d" 
  instance_type = "t2.micro"
  subnet_id = aws_subnet.public[count.index].id
  associate_public_ip_address = true

  tags = {
    Name = "web-server-${count.index + 1}"
  }

  user_data = <<-EOF
    #!/bin/bash
    # Use this for user data to install packages, install and start web server
    # install httpd (Linux 2 version)
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello from Duke's week three Terraform Project!</h1>" > /var/www/html/index.html
  EOF
}

resource "aws_db_instance" "rds" {
  allocated_storage = 20
  engine = "mysql"
  engine_version = "8.0.39"
  instance_class = "db.t3.micro"
  db_name = "duketerraformdatabase"
  username = "admin"
  password = "password123"
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name = aws_db_subnet_group.main.name
  skip_final_snapshot = true

  tags = {
    Name = "duketerraformdatabase"
  }
}

resource "aws_security_group" "terraform-sg3" {
  name = "terraform-sg3"
  vpc_id = aws_vpc.main.id

  ingress {
    description = "Allow port 80"
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow port 22"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "rds" {
  name = "rds-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port = 3306
    to_port = 3306
    protocol = "tcp"
    security_groups = [aws_security_group.terraform-sg3.id]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_subnet_group" "main" {
  name = "main-db-subnet-group"
  subnet_ids = aws_subnet.private[*].id

  tags = {
    Name = "main-db-subnet-group"
  }
}
