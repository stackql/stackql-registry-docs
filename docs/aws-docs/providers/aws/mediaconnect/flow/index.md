---
title: flow
hide_title: false
hide_table_of_contents: false
keywords:
  - flow
  - mediaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flow</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediaconnect.flow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>flow_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the flow.</td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td>The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.</td></tr>
<tr><td><code>flow_availability_zone</code></td><td><code>string</code></td><td>The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.(ReadOnly)</td></tr>
<tr><td><code>source</code></td><td><code>object</code></td><td>The source of the flow.</td></tr>
<tr><td><code>source_failover_config</code></td><td><code>object</code></td><td>The source failover config of the flow.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
flow_arn,
name,
availability_zone,
flow_availability_zone,
source,
source_failover_config
FROM aws.mediaconnect.flow
WHERE region = 'us-east-1'
AND data__Identifier = '<FlowArn>'
```
