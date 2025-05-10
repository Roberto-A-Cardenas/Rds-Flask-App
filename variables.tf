variable "project_name" {
  description = "Name for tagging"
  default     = "rds-flask-app"
}

variable "db_name" {
  description = "RDS database name"
  default     = "flaskdb"
}

variable "db_username" {
  description = "RDS master username"
  default     = "flaskadmin"
}

variable "db_password" {
  description = "RDS master password"
  sensitive   = true
}

variable "ec2_key_name" {
  description = "EC2 SSH key pair name"
}
