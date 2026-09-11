resource "aws_ecs_service" "app" {
    name = "app"
    cluster = aws_ecs_cluster.main.id
    task_definition = aws_ecs_task_definition.app.arn
    desired_count = 2
    launch_type = "FARGATE"
    health_check_grace_period_seconds = 60
    network_configuration {
        security_groups = [aws_security_group.web.id]
        subnets = [aws_subnet.public_a.id, aws_subnet.public_b.id]
        assign_public_ip = true
    }
    load_balancer {
        target_group_arn = aws_alb_target_group.app.arn
        container_name = "ews"
        container_port = 8000
    }
    depends_on = [aws_alb_listener.app]
}

output "name" {
    value = aws_ecs_service.app.name
}