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
<tr><td><b>Description</b></td><td>target_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticloadbalancingv2.target_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ip_address_type</code></td><td><code>string</code></td><td>The type of IP address used for this target group. The possible values are ipv4 and ipv6. </td></tr>
<tr><td><code>health_check_interval_seconds</code></td><td><code>integer</code></td><td>The approximate amount of time, in seconds, between health checks of an individual target.</td></tr>
<tr><td><code>load_balancer_arns</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the load balancers that route traffic to this target group.</td></tr>
<tr><td><code>matcher</code></td><td><code>object</code></td><td>&#91;HTTP&#x2F;HTTPS health checks&#93; The HTTP or gRPC codes to use when checking for a successful response from a target.</td></tr>
<tr><td><code>health_check_path</code></td><td><code>string</code></td><td>&#91;HTTP&#x2F;HTTPS health checks&#93; The destination for health checks on the targets. &#91;HTTP1 or HTTP2 protocol version&#93; The ping path. The default is &#x2F;. &#91;GRPC protocol version&#93; The path of a custom health check method with the format &#x2F;package.service&#x2F;method. The default is &#x2F;AWS.ALB&#x2F;healthcheck.</td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td>The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply. If the protocol is GENEVE, the supported port is 6081.</td></tr>
<tr><td><code>targets</code></td><td><code>array</code></td><td>The targets.</td></tr>
<tr><td><code>health_check_enabled</code></td><td><code>boolean</code></td><td>Indicates whether health checks are enabled. If the target type is lambda, health checks are disabled by default but can be enabled. If the target type is instance, ip, or alb, health checks are always enabled and cannot be disabled.</td></tr>
<tr><td><code>protocol_version</code></td><td><code>string</code></td><td>&#91;HTTP&#x2F;HTTPS protocol&#93; The protocol version. The possible values are GRPC, HTTP1, and HTTP2.</td></tr>
<tr><td><code>unhealthy_threshold_count</code></td><td><code>integer</code></td><td>The number of consecutive health check failures required before considering a target unhealthy.</td></tr>
<tr><td><code>health_check_timeout_seconds</code></td><td><code>integer</code></td><td>The amount of time, in seconds, during which no response from a target means a failed health check.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the target group.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply.</td></tr>
<tr><td><code>target_group_full_name</code></td><td><code>string</code></td><td>The full name of the target group.</td></tr>
<tr><td><code>healthy_threshold_count</code></td><td><code>integer</code></td><td>The number of consecutive health checks successes required before considering an unhealthy target healthy. </td></tr>
<tr><td><code>health_check_protocol</code></td><td><code>string</code></td><td>The protocol the load balancer uses when performing health checks on targets. </td></tr>
<tr><td><code>target_group_attributes</code></td><td><code>array</code></td><td>The attributes.</td></tr>
<tr><td><code>target_type</code></td><td><code>string</code></td><td>The type of target that you must specify when registering targets with this target group. You can't specify targets for a target group using more than one target type.</td></tr>
<tr><td><code>health_check_port</code></td><td><code>string</code></td><td>The port the load balancer uses when performing health checks on targets. </td></tr>
<tr><td><code>target_group_arn</code></td><td><code>string</code></td><td>The ARN of the Target Group</td></tr>
<tr><td><code>protocol</code></td><td><code>string</code></td><td>The protocol to use for routing traffic to the targets.</td></tr>
<tr><td><code>target_group_name</code></td><td><code>string</code></td><td>The name of the target group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ip_address_type,
health_check_interval_seconds,
load_balancer_arns,
matcher,
health_check_path,
port,
targets,
health_check_enabled,
protocol_version,
unhealthy_threshold_count,
health_check_timeout_seconds,
name,
vpc_id,
target_group_full_name,
healthy_threshold_count,
health_check_protocol,
target_group_attributes,
target_type,
health_check_port,
target_group_arn,
protocol,
target_group_name,
tags
FROM awscc.elasticloadbalancingv2.target_group
WHERE region = 'us-east-1'
AND data__Identifier = '{TargetGroupArn}';
```

## Permissions

To operate on the <code>target_group</code> resource, the following permissions are required:

### Delete
```json
elasticloadbalancing:DeleteTargetGroup,
elasticloadbalancing:DescribeTargetGroups
```

### Read
```json
elasticloadbalancing:DescribeTargetGroups,
elasticloadbalancing:DescribeTargetGroupAttributes,
elasticloadbalancing:DescribeTargetHealth,
elasticloadbalancing:DescribeTags
```

### Update
```json
elasticloadbalancing:DescribeTargetGroups,
elasticloadbalancing:ModifyTargetGroup,
elasticloadbalancing:ModifyTargetGroupAttributes,
elasticloadbalancing:RegisterTargets,
elasticloadbalancing:DescribeTargetHealth,
elasticloadbalancing:DeregisterTargets,
elasticloadbalancing:AddTags,
elasticloadbalancing:RemoveTags
```

