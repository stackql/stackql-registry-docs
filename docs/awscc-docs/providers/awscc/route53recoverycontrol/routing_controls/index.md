---
title: routing_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_controls
  - route53recoverycontrol
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>routing_controls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>routing_controls</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53recoverycontrol.routing_controls</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>routing_control_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the routing control.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
routing_control_arn
FROM awscc.route53recoverycontrol.routing_controls
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>routing_controls</code> resource, the following permissions are required:

### Create
```json
route53-recovery-control-config:CreateRoutingControl,
route53-recovery-control-config:DescribeRoutingControl,
route53-recovery-control-config:DescribeControlPanel,
route53-recovery-control-config:DescribeCluster
```

### List
```json
route53-recovery-control-config:ListRoutingControls
```

