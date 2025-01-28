variable "region" {
  default = "us-east-1"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  default = ["10.0.0.0/27", "10.0.0.32/27"]
}

variable "private_subnet_cidrs" {
  default = ["10.0.1.0/27", "10.0.1.32/27"]
}
