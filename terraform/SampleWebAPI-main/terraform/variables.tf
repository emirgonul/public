variable "prefix" {
  description = "project prefix"
  default     = "sample-web-api"
}

variable "resource_group_name" {"
  default     = "sample-web-api"
}

variable "location" {
  description = "The region where the virtual network is created."
  default     = "eastus"
}

variable "virtual_network_name" {
  description = "The name for your virtual network."
  default     = "sample-vnet"
}

variable "address_space" {
  description = "The address space that is used by the virtual network."
  default     = ["10.0.0.0/16"]
}

variable "subnet_prefix" {
  description = "The address prefix to use for the subnet."
  default     = ["10.0.2.0/24"]
}

variable "hostname" {
  description = "vmname"
  default     = "sample-vm"
}

variable "vm_size" {
  description = "Specifies the size of the virtual machine."
  default     = "Standard_DS1_v2"
}

variable "image_publisher" {
  description = "vm image"
  default     = "MicrosoftWindowsServer"
}

variable "image_offer" {
  description = "Name of the offer"
  default     = "WindowsServer"
}

variable "image_sku" {
  description = "Image SKU"
  default     = "2019-datacenter-gensecond"
}

variable "image_version" {
  default     = "latest"
}

variable "admin_username" {
  description = "admin username"
  default     = "admin"
}

variable "admin_password" {
  description = "Admin pw"
  default     = "@NeedtoHideThis@"
}