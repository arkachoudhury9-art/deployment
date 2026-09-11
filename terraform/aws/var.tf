variable "db_username" {
  type = string
  description = "The username for the database"
}

variable "db_password" {
  type = string
  description = "The password for the database"
  sensitive = true
}
