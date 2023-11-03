---
title: endpoint_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_groups
  - globalaccelerator
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>endpoint_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.globalaccelerator.endpoint_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ListenerArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the listener</td></tr><tr><td><code>EndpointGroupRegion</code></td><td><code>string</code></td><td>The name of the AWS Region where the endpoint group is located</td></tr><tr><td><code>EndpointConfigurations</code></td><td><code>array</code></td><td>The list of endpoint objects.</td></tr><tr><td><code>TrafficDialPercentage</code></td><td><code>number</code></td><td>The percentage of traffic to sent to an AWS Region</td></tr><tr><td><code>HealthCheckPort</code></td><td><code>integer</code></td><td>The port that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.</td></tr><tr><td><code>HealthCheckProtocol</code></td><td><code>string</code></td><td>The protocol that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.</td></tr><tr><td><code>HealthCheckPath</code></td><td><code>string</code></td><td></td></tr><tr><td><code>HealthCheckIntervalSeconds</code></td><td><code>integer</code></td><td>The time in seconds between each health check for an endpoint. Must be a value of 10 or 30</td></tr><tr><td><code>ThresholdCount</code></td><td><code>integer</code></td><td>The number of consecutive health checks required to set the state of the endpoint to unhealthy.</td></tr><tr><td><code>EndpointGroupArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint group</td></tr><tr><td><code>PortOverrides</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.globalaccelerator.endpoint_groups
WHERE region = 'us-east-1'
</pre>
