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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>routing_control</code> resource, use <code>routing_controls</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Control Routing Control resource schema .</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.routing_control" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="routing_control_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the routing control.</td></tr>
<tr><td><CopyableCode code="control_panel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the control panel.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the routing control. You can use any non-white space character in the name.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>Arn associated with Control Panel</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
routing_control_arn,
control_panel_arn,
name,
status,
cluster_arn
FROM aws.route53recoverycontrol.routing_control
WHERE region = 'us-east-1' AND data__Identifier = '<RoutingControlArn>';
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

