# Configure the DigitalOcean provider
provider "digitalocean" {
  token = "dop_v1_7532d90fc4dafdf34bcc2f7fdecf55eea6077ed5c74972f717bb6e714e7f37d2"
}

# Create a new droplet
resource "digitalocean_droplet" "web" {
  image  = "ubuntu-22-04-x64"
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
