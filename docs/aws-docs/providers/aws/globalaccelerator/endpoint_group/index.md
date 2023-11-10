---
title: endpoint_group
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_group
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
Gets an individual <code>endpoint_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>endpoint_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.globalaccelerator.endpoint_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>listener_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the listener</td></tr>
<tr><td><code>endpoint_group_region</code></td><td><code>string</code></td><td>The name of the AWS Region where the endpoint group is located</td></tr>
<tr><td><code>endpoint_configurations</code></td><td><code>array</code></td><td>The list of endpoint objects.</td></tr>
<tr><td><code>traffic_dial_percentage</code></td><td><code>number</code></td><td>The percentage of traffic to sent to an AWS Region</td></tr>
<tr><td><code>health_check_port</code></td><td><code>integer</code></td><td>The port that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.</td></tr>
<tr><td><code>health_check_protocol</code></td><td><code>string</code></td><td>The protocol that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.</td></tr>
<tr><td><code>health_check_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>health_check_interval_seconds</code></td><td><code>integer</code></td><td>The time in seconds between each health check for an endpoint. Must be a value of 10 or 30</td></tr>
<tr><td><code>threshold_count</code></td><td><code>integer</code></td><td>The number of consecutive health checks required to set the state of the endpoint to unhealthy.</td></tr>
<tr><td><code>endpoint_group_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint group</td></tr>
<tr><td><code>port_overrides</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
listener_arn,
endpoint_group_region,
endpoint_configurations,
traffic_dial_percentage,
health_check_port,
health_check_protocol,
health_check_path,
health_check_interval_seconds,
threshold_count,
endpoint_group_arn,
port_overrides
FROM aws.globalaccelerator.endpoint_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;EndpointGroupArn&gt;'
```
