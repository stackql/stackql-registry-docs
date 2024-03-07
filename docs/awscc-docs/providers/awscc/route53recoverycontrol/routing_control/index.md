---
title: routing_control
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_control
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
Gets an individual <code>routing_control</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>routing_control</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53recoverycontrol.routing_control</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>routing_control_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the routing control.</td></tr>
<tr><td><code>control_panel_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the control panel.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the routing control. You can use any non-white space character in the name.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><code>cluster_arn</code></td><td><code>string</code></td><td>Arn associated with Control Panel</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
routing_control_arn,
control_panel_arn,
name,
status,
cluster_arn
FROM awscc.route53recoverycontrol.routing_control
WHERE region = 'us-east-1'
AND data__Identifier = '{RoutingControlArn}';
```

## Permissions

To operate on the <code>routing_control</code> resource, the following permissions are required:

### Read
```json
route53-recovery-control-config:DescribeRoutingControl
```

### Update
```json
route53-recovery-control-config:UpdateRoutingControl,
route53-recovery-control-config:DescribeRoutingControl,
route53-recovery-control-config:DescribeControlPanel
```

### Delete
```json
route53-recovery-control-config:DescribeRoutingControl,
route53-recovery-control-config:DeleteRoutingControl
```

