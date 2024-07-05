---
title: target_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - target_groups_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>target_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/target_groups/"><code>target_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticLoadBalancingV2::TargetGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.target_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td>The type of IP address used for this target group. The possible values are ipv4 and ipv6.</td></tr>
<tr><td><CopyableCode code="health_check_interval_seconds" /></td><td><code>integer</code></td><td>The approximate amount of time, in seconds, between health checks of an individual target.</td></tr>
<tr><td><CopyableCode code="load_balancer_arns" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the load balancers that route traffic to this target group.</td></tr>
<tr><td><CopyableCode code="matcher" /></td><td><code>object</code></td><td>&#91;HTTP/HTTPS health checks&#93; The HTTP or gRPC codes to use when checking for a successful response from a target.</td></tr>
<tr><td><CopyableCode code="health_check_path" /></td><td><code>string</code></td><td>&#91;HTTP/HTTPS health checks&#93; The destination for health checks on the targets. &#91;HTTP1 or HTTP2 protocol version&#93; The ping path. The default is /. &#91;GRPC protocol version&#93; The path of a custom health check method with the format /package.service/method. The default is /AWS.ALB/healthcheck.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply. If the protocol is GENEVE, the supported port is 6081.</td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>array</code></td><td>The targets.</td></tr>
<tr><td><CopyableCode code="health_check_enabled" /></td><td><code>boolean</code></td><td>Indicates whether health checks are enabled. If the target type is lambda, health checks are disabled by default but can be enabled. If the target type is instance, ip, or alb, health checks are always enabled and cannot be disabled.</td></tr>
<tr><td><CopyableCode code="protocol_version" /></td><td><code>string</code></td><td>&#91;HTTP/HTTPS protocol&#93; The protocol version. The possible values are GRPC, HTTP1, and HTTP2.</td></tr>
<tr><td><CopyableCode code="unhealthy_threshold_count" /></td><td><code>integer</code></td><td>The number of consecutive health check failures required before considering a target unhealthy.</td></tr>
<tr><td><CopyableCode code="health_check_timeout_seconds" /></td><td><code>integer</code></td><td>The amount of time, in seconds, during which no response from a target means a failed health check.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the target group.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply.</td></tr>
<tr><td><CopyableCode code="target_group_full_name" /></td><td><code>string</code></td><td>The full name of the target group.</td></tr>
<tr><td><CopyableCode code="healthy_threshold_count" /></td><td><code>integer</code></td><td>The number of consecutive health checks successes required before considering an unhealthy target healthy.</td></tr>
<tr><td><CopyableCode code="health_check_protocol" /></td><td><code>string</code></td><td>The protocol the load balancer uses when performing health checks on targets.</td></tr>
<tr><td><CopyableCode code="target_group_attributes" /></td><td><code>array</code></td><td>The attributes.</td></tr>
<tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>The type of target that you must specify when registering targets with this target group. You can't specify targets for a target group using more than one target type.</td></tr>
<tr><td><CopyableCode code="health_check_port" /></td><td><code>string</code></td><td>The port the load balancer uses when performing health checks on targets.</td></tr>
<tr><td><CopyableCode code="target_group_arn" /></td><td><code>string</code></td><td>The ARN of the Target Group</td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>string</code></td><td>The protocol to use for routing traffic to the targets.</td></tr>
<tr><td><CopyableCode code="target_group_name" /></td><td><code>string</code></td><td>The name of the target group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>target_groups</code> in a region.
```sql
SELECT
region,
target_group_arn
FROM aws.elasticloadbalancingv2.target_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>target_groups_list_only</code> resource, see <a href="/providers/aws/elasticloadbalancingv2/target_groups/#permissions"><code>target_groups</code></a>


