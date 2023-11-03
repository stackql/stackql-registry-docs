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
null
<tr><td><b>Id</b></td><td><code>aws.lightsail.load_balancer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>LoadBalancerName</code></td><td><code>string</code></td><td>The name of your load balancer.</td></tr><tr><td><code>LoadBalancerArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>InstancePort</code></td><td><code>integer</code></td><td>The instance port where you're creating your load balancer.</td></tr><tr><td><code>IpAddressType</code></td><td><code>string</code></td><td>The IP address type for the load balancer. The possible values are ipv4 for IPv4 only, and dualstack for IPv4 and IPv6. The default value is dualstack.</td></tr><tr><td><code>AttachedInstances</code></td><td><code>array</code></td><td>The names of the instances attached to the load balancer.</td></tr><tr><td><code>HealthCheckPath</code></td><td><code>string</code></td><td>The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., "/").</td></tr><tr><td><code>SessionStickinessEnabled</code></td><td><code>boolean</code></td><td>Configuration option to enable session stickiness.</td></tr><tr><td><code>SessionStickinessLBCookieDurationSeconds</code></td><td><code>string</code></td><td>Configuration option to adjust session stickiness cookie duration parameter.</td></tr><tr><td><code>TlsPolicyName</code></td><td><code>string</code></td><td>The name of the TLS policy to apply to the load balancer.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lightsail.load_balancer
WHERE region = 'us-east-1' AND data__Identifier = '{LoadBalancerName}'
</pre>
