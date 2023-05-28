# Configure the DigitalOcean provider
provider "digitalocean" {
  token = "YOUR_DIGITALOCEAN_API_TOKEN"
}

# Create a new droplet
resource "digitalocean_droplet" "example" {
  image    = "ubuntu-20-04-x64"
  name     = "example-droplet"
  region   = "nyc1"
  size     = "s-1vcpu-1gb"
}
