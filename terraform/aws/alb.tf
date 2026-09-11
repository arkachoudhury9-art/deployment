resource "aws_alb" "main" {
    name = "main"
    internal = false
    load_balancer_type = "application"
    security_groups = [aws_security_group.alb.id]
    subnets = [aws_subnet.public_a.id, aws_subnet.public_b.id]
}

resource "aws_alb_target_group" "app" {
    name = "app"
    port = 8000
    protocol = "HTTP"
    target_type = "ip"
    vpc_id = aws_vpc.main.id
    health_check {
        path = "/health"
        healthy_threshold = 2
        unhealthy_threshold = 5
        interval = 15
        timeout = 5
        matcher = "200"
    }
}

resource "aws_alb_listener" "app" {
    load_balancer_arn = aws_alb.main.arn
    port = 80
    protocol = "HTTP"
    default_action {
        type = "forward"
        target_group_arn = aws_alb_target_group.app.arn
    }
}

output "alb_dns_name" {
  value = aws_alb.main.dns_name
}