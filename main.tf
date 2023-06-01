# Configure the DigitalOcean provider
provider "digitalocean" {
  token = "dop_v1_0b61b0ea9f0837e921396a2d67c3f7cf23be3a17e5e4daf39e275ff4786ee24a"
}

# Create a new droplet
resource "digitalocean_droplet" "example" {
  image  = "Ubuntu 22.04 (LTS) x64"
  name   = "Bless"
  region = "TOR1"
  size   = "s-1vcpu-1gb"
}
terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
    }
  }
}
