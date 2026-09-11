resource "aws_ecs_cluster" "main" {
  name = "ews"
}

resource "aws_ecs_task_definition" "app" {
  family = "ews"
  network_mode = "awsvpc"
  cpu = "256"
  memory = "512"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn
  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "ARM64"
  }
 
  container_definitions = jsonencode([
    {
      name = "ews"
      image = "372684706039.dkr.ecr.ap-south-1.amazonaws.com/user-platform:latest"
      essential = true
      portMappings = [
        {
          containerPort = 8000
          hostPort = 8000
          protocol = "tcp"
        }
      ]
      environment = [
        {
          name = "APP_ENV"
          value = "production"
        },
        {
            name = "APP_HOST",
            value = "0.0.0.0"
        },
        {
            name = "APP_PORT",
            value = "8000"
        },
        {
          name = "SQLALCHEMY_DATABASE_URL",
          value = "postgresql://${var.db_username}:${urlencode(var.db_password)}@${aws_db_instance.main.address}:${aws_db_instance.main.port}/${aws_db_instance.main.db_name}"
        }
      ]
    }
  ])
}