resource "aws_db_instance" "main" {
  allocated_storage = 20
  engine = "postgres"
  engine_version = "18.3"
  instance_class = "db.t3.micro"
  db_name = "ads_platform"
  username = var.db_username
  password = var.db_password
  db_subnet_group_name = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.db.id]
  publicly_accessible = false
  tags = {
    Name = "ads_platform_db"
  }
}