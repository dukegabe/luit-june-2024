terraform {
  backend "remote" {
    organization = "Terraform-Project-3-Duke"

    workspaces {
      name = "luit-june-2024"
    }
  }
}
