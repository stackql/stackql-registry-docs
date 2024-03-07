---
title: load_balancer
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer
  - lightsail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>load_balancer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>load_balancer</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lightsail.load_balancer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>load_balancer_name</code></td><td><code>string</code></td><td>The name of your load balancer.</td></tr>
<tr><td><code>load_balancer_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_port</code></td><td><code>integer</code></td><td>The instance port where you're creating your load balancer.</td></tr>
<tr><td><code>ip_address_type</code></td><td><code>string</code></td><td>The IP address type for the load balancer. The possible values are ipv4 for IPv4 only, and dualstack for IPv4 and IPv6. The default value is dualstack.</td></tr>
<tr><td><code>attached_instances</code></td><td><code>array</code></td><td>The names of the instances attached to the load balancer.</td></tr>
<tr><td><code>health_check_path</code></td><td><code>string</code></td><td>The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., "&#x2F;").</td></tr>
<tr><td><code>session_stickiness_enabled</code></td><td><code>boolean</code></td><td>Configuration option to enable session stickiness.</td></tr>
<tr><td><code>session_stickiness_lb_cookie_duration_seconds</code></td><td><code>string</code></td><td>Configuration option to adjust session stickiness cookie duration parameter.</td></tr>
<tr><td><code>tls_policy_name</code></td><td><code>string</code></td><td>The name of the TLS policy to apply to the load balancer.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
load_balancer_name,
load_balancer_arn,
instance_port,
ip_address_type,
attached_instances,
health_check_path,
session_stickiness_enabled,
session_stickiness_lb_cookie_duration_seconds,
tls_policy_name,
tags
FROM awscc.lightsail.load_balancer
WHERE region = 'us-east-1'
AND data__Identifier = '{LoadBalancerName}';
```

## Permissions

To operate on the <code>load_balancer</code> resource, the following permissions are required:

### Read
```json
lightsail:GetLoadBalancer,
lightsail:GetLoadBalancers
```

### Update
```json
lightsail:GetLoadBalancer,
lightsail:GetLoadBalancers,
lightsail:GetInstance,
lightsail:AttachInstancesToLoadBalancer,
lightsail:DetachInstancesFromLoadBalancer,
lightsail:UpdateLoadBalancerAttribute,
lightsail:TagResource,
lightsail:UntagResource
```

### Delete
```json
lightsail:DeleteLoadBalancer,
lightsail:GetLoadBalancer,
lightsail:GetLoadBalancers
```

