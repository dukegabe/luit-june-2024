provider "aws" {
  region = "us-east-1" 
}

terraform {
  backend "remote" {
    organization = "Terraform-Project-3-Duke"

    workspaces {
      name = "luit-june-2024"
    }
  }
}
