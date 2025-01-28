output "vpc_id" {
  value = aws_vpc.main.id
}

output "web_server_ips" {
  value = aws_instance.DukeWebSever[*].public_ip
}

output "rds_endpoint" {
  value = aws_db_instance.rds.endpoint
}
