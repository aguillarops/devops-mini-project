output "lb_dns_name" {
  description = "O DNS do Application Load Balancer"
  value       = aws_lb.app_lb.dns_name
}

output "ecr_repository_url" {
  description = "URL do repositório ECR"
  value       = aws_ecr_repository.app_repo.repository_url
}

