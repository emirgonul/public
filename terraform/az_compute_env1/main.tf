# Define the provider and set the Azure subscription details
provider "azurerm" {
  features {}
}

# Define the resource group
resource "azurerm_resource_group" "compute-env1" {
  name     = "az-compute-env1"
  location = "us-east-2"
}

# Define the virtual network
resource "azurerm_virtual_network" "network-env1" {
  name                = "az-virtual-network1"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  address_space       = ["10.0.0.0/16"]
}

# Define the subnet
resource "azurerm_subnet" "subnet1" {
  name                 = "az-subnet1"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.0.0/24"]
}

# Define the public IP address
resource "azurerm_public_ip" "public-ip" {
  name                = "az-public-ip1"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  allocation_method   = "Static"
}

# Define the network interface
resource "azurerm_network_interface" "network-int1" {
  name                = "az-network-int1"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location

  ip_configuration {
    name                          = "az-ip-configuration1"
    subnet_id                     = azurerm_subnet.example.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.example.id
  }
}

# Define the virtual machine
resource "azurerm_virtual_machine" "example" {
  name                  = "az-vm01"
  resource_group_name   = azurerm_resource_group.example.name
  location              = azurerm_resource_group.example.location
  size                  = "Standard_DS2_v2"
  admin_username        = "adminuser"
  admin_password        = "Password123!"
  network_interface_ids = [azurerm_network_interface.example.id]

  storage_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  os_disk {
    name              = "disk0"
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
}
