variable "aws_region" {
  description = "Região da AWS para provisionar os recursos"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Nome do projeto para prefixar os recursos"
  type        = string
  default     = "devops-mini-project"
}

variable "app_port" {
  description = "Porta da aplicação Flask"
  type        = number
  default     = 5000
}

variable "docker_image_name" {
  description = "Nome da imagem Docker da aplicação"
  type        = string
  default     = "flask-app"
}

variable "docker_image_tag" {
  description = "Tag da imagem Docker da aplicação"
  type        = string
  default     = "latest"
}

