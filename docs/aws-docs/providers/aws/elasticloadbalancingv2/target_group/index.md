---
title: target_group
hide_title: false
hide_table_of_contents: false
keywords:
  - target_group
  - elasticloadbalancingv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>target_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.target_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>IpAddressType</code></td><td><code>string</code></td><td>The type of IP address used for this target group. The possible values are ipv4 and ipv6. </td></tr><tr><td><code>HealthCheckIntervalSeconds</code></td><td><code>integer</code></td><td>The approximate amount of time, in seconds, between health checks of an individual target.</td></tr><tr><td><code>LoadBalancerArns</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the load balancers that route traffic to this target group.</td></tr><tr><td><code>Matcher</code></td><td><code>undefined</code></td><td>[HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target.</td></tr><tr><td><code>HealthCheckPath</code></td><td><code>string</code></td><td>[HTTP/HTTPS health checks] The destination for health checks on the targets. [HTTP1 or HTTP2 protocol version] The ping path. The default is /. [GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /AWS.ALB/healthcheck.</td></tr><tr><td><code>Port</code></td><td><code>integer</code></td><td>The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply. If the protocol is GENEVE, the supported port is 6081.</td></tr><tr><td><code>Targets</code></td><td><code>array</code></td><td>The targets.</td></tr><tr><td><code>HealthCheckEnabled</code></td><td><code>boolean</code></td><td>Indicates whether health checks are enabled. If the target type is lambda, health checks are disabled by default but can be enabled. If the target type is instance, ip, or alb, health checks are always enabled and cannot be disabled.</td></tr><tr><td><code>ProtocolVersion</code></td><td><code>string</code></td><td>[HTTP/HTTPS protocol] The protocol version. The possible values are GRPC, HTTP1, and HTTP2.</td></tr><tr><td><code>UnhealthyThresholdCount</code></td><td><code>integer</code></td><td>The number of consecutive health check failures required before considering a target unhealthy.</td></tr><tr><td><code>HealthCheckTimeoutSeconds</code></td><td><code>integer</code></td><td>The amount of time, in seconds, during which no response from a target means a failed health check.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the target group.</td></tr><tr><td><code>VpcId</code></td><td><code>string</code></td><td>The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply.</td></tr><tr><td><code>TargetGroupFullName</code></td><td><code>string</code></td><td>The full name of the target group.</td></tr><tr><td><code>HealthyThresholdCount</code></td><td><code>integer</code></td><td>The number of consecutive health checks successes required before considering an unhealthy target healthy. </td></tr><tr><td><code>HealthCheckProtocol</code></td><td><code>string</code></td><td>The protocol the load balancer uses when performing health checks on targets. </td></tr><tr><td><code>TargetGroupAttributes</code></td><td><code>array</code></td><td>The attributes.</td></tr><tr><td><code>TargetType</code></td><td><code>string</code></td><td>The type of target that you must specify when registering targets with this target group. You can't specify targets for a target group using more than one target type.</td></tr><tr><td><code>HealthCheckPort</code></td><td><code>string</code></td><td>The port the load balancer uses when performing health checks on targets. </td></tr><tr><td><code>TargetGroupArn</code></td><td><code>string</code></td><td>The ARN of the Target Group</td></tr><tr><td><code>Protocol</code></td><td><code>string</code></td><td>The protocol to use for routing traffic to the targets.</td></tr><tr><td><code>TargetGroupName</code></td><td><code>string</code></td><td>The name of the target group.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.elasticloadbalancingv2.target_group
WHERE region = 'us-east-1' AND data__Identifier = '{TargetGroupArn}'
</pre>
